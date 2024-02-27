import tkinter as tk
from tkinter import colorchooser, scrolledtext, ttk
import speech_recognition as sr
import time

def send_message(message):
    if message:
        if isinstance(message, str):
            chat_area.insert(tk.END, f"You (Text): {message}\n", "user_message")
        else:
            chat_area.insert(tk.END, f"You (Voice): {message}\n", "voice_message")
        entry.delete(0, tk.END)

def pick_color():
    color = colorchooser.askcolor()[1]
    chat_area.config(foreground=color)

def pick_emoji(event):
    selected_emoji = emoji_combobox.get()
    entry.insert(tk.END, selected_emoji)

def record_and_recognize():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            send_message(text)  # Reuse existing send_message function
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Request error; {0}".format(e))

def record_voice():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        while True:
            audio = r.listen(source, timeout=1)  # 1 second chunks
            try:
                text = r.recognize_google(audio)
                send_message(text)
                break  # Stop recording after first successful recognition
            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print("Request error; {0}".format(e))

def record_voice_with_timeout(timeout=15):
    start_time = time.time()
    r = sr.Recognizer()
    with sr.Microphone() as source:
        while True:
            audio = r.listen(source, timeout=1)  # 1 second chunks
            try:
                text = r.recognize_google(audio)
                if text.lower().startswith("exagone"):
                    # Début de l'enregistrement
                    start_time = time.time()
                    print("Début de l'enregistrement")
                    break
                elif text.lower().startswith("fin"):
                    # Fin de l'enregistrement
                    print("Fin de l'enregistrement")
                    break
            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print("Request error; {0}".format(e))

        # Enregistrer le message vocal après le mot d'amorçage "exagone"
        while time.time() - start_time < timeout:
            audio = r.listen(source, timeout=1)
            try:
                text = r.recognize_google(audio)
                if text:
                    send_message(text)
                    break
            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print("Request error; {0}".format(e))

# Add more emojis in the same style as 😊
MORE_EMOJIS = [":smile:", ":blush:", ":grinning:", ":heart_eyes:", ":sweat_smile:", ":wink:", ":yum:", ":sunglasses:",
               ":relieved:", ":innocent:"]

# Combine with the existing COMMON_EMOJIS list
COMMON_EMOJIS = [":)", ":(", ":D", ":P", "<3", ":thumbsup:", ":thumbsdown:", ":star:", ":rocket:", ":heart:", ":bell:",
                 ":speech_balloon:"]
COMMON_EMOJIS += MORE_EMOJIS

# Create the main window
root = tk.Tk()
root.title("Messaging App")
root.geometry("600x400")

# Create a Frame for the chat area
chat_frame = tk.Frame(root)
chat_frame.pack(expand=True, fill=tk.BOTH)

# Create a resizable chat area
chat_area = scrolledtext.ScrolledText(chat_frame, wrap=tk.WORD, width=60, height=20)
chat_area.tag_configure("user_message", foreground="black")  # Set the color for user messages
chat_area.pack(expand=True, fill=tk.BOTH)

# Create a Frame for typing messages
entry_frame = tk.Frame(root)
entry_frame.pack(expand=True, fill=tk.BOTH)

# Create a Text widget for typing messages
entry = tk.Text(entry_frame, wrap=tk.WORD, width=20, height=2)
entry.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

# Create a button to send messages
send_button = tk.Button(entry_frame, text="Send", command=lambda: send_message(entry.get("1.0", tk.END).strip()))
send_button.pack(side=tk.RIGHT, padx=5)

# Create a button for choosing colors
color_button = tk.Button(root, text="Choose Color", command=pick_color)
color_button.pack(pady=5)

# Create a dropdown menu (combobox) for choosing emojis
emoji_combobox = ttk.Combobox(root, values=COMMON_EMOJIS, state="readonly")
emoji_combobox.set("Choose Emoji")
emoji_combobox.bind("<<ComboboxSelected>>", pick_emoji)
emoji_combobox.pack(pady=5)

voice_button = tk.Button(root, text="Record Voice (15s)", command=record_voice_with_timeout)
voice_button.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()

