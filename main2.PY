import tkinter as tk
from tkinter import colorchooser, scrolledtext
from tkinter import ttk  # Import ttk for combobox

def send_message():
    message = entry.get()
    if message:
        chat_area.insert(tk.END, f"You: {message}\n", "user_message")
        entry.delete(0, tk.END)

def pick_color():
    color = colorchooser.askcolor()[1]
    chat_area.config(foreground=color)

def pick_emoji(event):
    selected_emoji = emoji_combobox.get()
    entry.insert(tk.END, selected_emoji)

# Add more emojis in the same style as 😊
MORE_EMOJIS = [":smile:", ":blush:", ":grinning:", ":heart_eyes:", ":sweat_smile:", ":wink:", ":yum:", ":sunglasses:", ":relieved:", ":innocent:"]

# Combine with the existing COMMON_EMOJIS list
COMMON_EMOJIS = [":)", ":(", ":D", ":P", "<3", ":thumbsup:", ":thumbsdown:", ":star:", ":rocket:", ":heart:", ":bell:", ":speech_balloon:"]
COMMON_EMOJIS += MORE_EMOJIS

# Create the main window
root = tk.Tk()
root.title("Messaging App")
root.geometry("600x400")

# Create a PanedWindow
paned_window = tk.PanedWindow(root, orient=tk.HORIZONTAL, sashwidth=5, sashrelief=tk.SUNKEN)
paned_window.pack(expand=True, fill=tk.BOTH)

# Create a resizable chat area on the left
chat_area = scrolledtext.ScrolledText(paned_window, wrap=tk.WORD, width=40, height=10)
chat_area.tag_configure("user_message", foreground="black")  # Set the color for user messages
paned_window.add(chat_area)

# Create an entry widget for typing messages on the right
entry = tk.Entry(paned_window, width=30)
paned_window.add(entry)

# Set a minimum size for the chat area (adjust as needed)
paned_window.paneconfig(chat_area, minsize=200)

# Create a button to send messages
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(pady=5)

# Create a button for choosing colors
color_button = tk.Button(root, text="Choose Color", command=pick_color)
color_button.pack(pady=5)

# Create a dropdown menu (combobox) for choosing emojis
emoji_combobox = ttk.Combobox(root, values=COMMON_EMOJIS, state="readonly")
emoji_combobox.set("Choose Emoji")
emoji_combobox.bind("<<ComboboxSelected>>", pick_emoji)
emoji_combobox.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()
