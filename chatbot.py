import tkinter as tk

# ===============================
# Chatbot Logic Function
# ===============================
def get_response(user_input):
    user_input = user_input.lower()

    if user_input == "hello":
        return "Hi! 😊"
    elif user_input == "how are you":
        return "I'm fine, thanks! How about you?"
    elif user_input == "bye":
        return "Goodbye! 👋"
    elif user_input == "your name":
        return "I am a simple Python Chatbot 🤖"
    else:
        return "Sorry, I don't understand that."

# ===============================
# Send Message Function
# ===============================
def send_message(event=None):
    user_text = entry.get()
    
    if user_text == "":
        return

    chat_area.config(state="normal")
    chat_area.insert(tk.END, "You: " + user_text + "\n")
    
    response = get_response(user_text)
    chat_area.insert(tk.END, "Bot: " + response + "\n\n")
    
    chat_area.config(state="disabled")
    entry.delete(0, tk.END)
    chat_area.see(tk.END)

# ===============================
# GUI Design
# ===============================
root = tk.Tk()
root.title("Basic Chatbot 🤖")
root.geometry("500x550")
root.configure(bg="#1e1e2f")

title = tk.Label(root,
                 text="🤖 Basic Rule-Based Chatbot",
                 font=("Arial", 16, "bold"),
                 bg="#1e1e2f",
                 fg="white")
title.pack(pady=10)

# Chat Display Area
chat_area = tk.Text(root,
                    height=20,
                    width=55,
                    state="disabled",
                    bg="#2b2b3c",
                    fg="white",
                    font=("Arial", 11))
chat_area.pack(pady=10)

# Input Field
entry = tk.Entry(root,
                 width=40,
                 font=("Arial", 12))
entry.pack(pady=5)

# Send Button
send_button = tk.Button(root,
                        text="Send",
                        font=("Arial", 12, "bold"),
                        bg="#4CAF50",
                        fg="white",
                        command=send_message)
send_button.pack(pady=5)

# Allow Enter key to send
root.bind("<Return>", send_message)

root.mainloop()