import tkinter as tk

def send_message():
    user_msg = entry.get().lower()
    chat_box.insert(tk.END, "You: " + user_msg)

    # simple rule-based replies
    if user_msg == "hello":
        bot_reply = "Hi!"
    elif user_msg == "how are you?":
        bot_reply = "I'm fine, thanks!"
    elif user_msg == "bye":
        bot_reply = "Goodbye!"
    elif user_msg == "":
        bot_reply = ""
    else:
        bot_reply = "I don't understand"

    chat_box.insert(tk.END, "Bot: " + bot_reply + "\n")
    entry.delete(0, tk.END)

# GUI
root = tk.Tk()
root.title("Simple Chatbot")
root.geometry("400x400")

chat_box = tk.Listbox(root, width=50, height=15)
chat_box.pack(pady=10)

entry = tk.Entry(root, width=40)
entry.pack(pady=5)

tk.Button(root, text="Send", command=send_message).pack()

root.mainloop()