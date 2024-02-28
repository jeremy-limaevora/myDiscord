import tkinter as tk
from tkinter import messagebox
from tkinter.font import Font
from tkinter import ttk
import speech_recognition as sr

def login():
    username = username_entry.get()
    password = password_entry.get()

    # Vérifiez si le nom d'utilisateur et le mot de passe sont corrects (c'est juste un exemple simple)
    if username == "john" and password == "password":
        messagebox.showinfo("Connexion réussie", "Bienvenue, {}".format(username))
        open_chat_window()  # Ouvre la fenêtre de chat en cas de connexion réussie
    else:
        messagebox.showerror("Erreur de connexion", "Nom d'utilisateur ou mot de passe incorrect")

def open_chat_window():
    chat_window = tk.Toplevel(root)
    chat_window.title("Chat")

    # Ajoutez les éléments nécessaires pour la fenêtre de chat
    chat_label = tk.Label(chat_window, text="Bienvenue dans le chat, {}!".format(username_entry.get()))
    chat_label.pack(padx=20, pady=20)

    # Vous pouvez ajouter d'autres éléments pour le chat ici

# Fonction pour créer un compte
def submit_account():
    new_username = new_username_entry.get()
    new_password = new_password_entry.get()

    # Vous pouvez ajouter une logique pour enregistrer le nouveau compte ici
    messagebox.showinfo("Compte créé", "Le compte pour {} a été créé avec succès!".format(new_username))

    # Ajout d'une fonction pour revenir à la page de connexion après la création du compte
    return_to_login_page()

# Fonction pour revenir à la page de connexion
def return_to_login_page():
    create_account_frame.grid_forget()  # Masquer la frame de création de compte
    frame.grid(row=0, column=0, rowspan=4, columnspan=2, sticky=tk.N+tk.S+tk.E+tk.W)  # Afficher la frame de connexion

# Fonction pour afficher la frame de création de compte
def show_create_account_frame():
    frame.grid_forget()  # Masquer la frame de connexion
    create_account_frame.grid(row=0, column=0, rowspan=4, columnspan=2, sticky=tk.N+tk.S+tk.E+tk.W)  # Afficher la frame de création de compte

# Créez la fenêtre principale
root = tk.Tk()
root.title("Connexion")

# Obtenez les dimensions de l'écran
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculez les coordonnées pour centrer la fenêtre
window_width = 500
window_height = 400
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2

# Définissez la position de la fenêtre
root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_position, y_position))

# Utilisez une police de caractères moderne
font_style = Font(family="Helvetica", size=12)

# Couleurs de style iOS
bg_color = "#f4f4f4"
fg_color = "#000000"
button_bg_color = "#007AFF"  # Couleur du bouton bleu iOS
button_fg_color = "#ffffff"  # Texte blanc pour le bouton

# Configuration des couleurs
root.configure(bg=bg_color, bd=4, relief=tk.SOLID)

# Utilisez ttk.Frame pour le conteneur principal
frame = ttk.Frame(root, style="TFrame")
frame.grid(row=0, column=0, rowspan=4, columnspan=2, sticky=tk.N+tk.S+tk.E+tk.W)

# Ajoutez les éléments au conteneur ttk.Frame
username_label = tk.Label(frame, text="Nom d'utilisateur:", font=font_style, bg=bg_color, fg=fg_color)
password_label = tk.Label(frame, text="Mot de passe:", font=font_style, bg=bg_color, fg=fg_color)
username_entry = tk.Entry(frame, font=font_style, bg=bg_color, fg=fg_color, highlightbackground=bg_color)
password_entry = tk.Entry(frame, show="*", font=font_style, bg=bg_color, fg=fg_color, highlightbackground=bg_color)
login_button = tk.Button(frame, text="Connexion", command=login, font=font_style, bg=button_bg_color, fg=button_fg_color, padx=10, pady=5)
create_account_button = tk.Button(frame, text="Créer un compte", command=show_create_account_frame, font=font_style, bg=button_bg_color, fg=button_fg_color, padx=10, pady=5)

# Placez les widgets dans le conteneur en les centrant
username_label.grid(row=0, column=0, sticky=tk.E, pady=10, padx=10)
username_entry.grid(row=0, column=1, pady=10, padx=10)
password_label.grid(row=1, column=0, sticky=tk.E, pady=10, padx=10)
password_entry.grid(row=1, column=1, pady=10, padx=10)
login_button.grid(row=2, column=1, columnspan=2, pady=20, padx=10, sticky=tk.W)
create_account_button.grid(row=3, column=1, columnspan=2, pady=10, padx=10, sticky=tk.W)

# Centrez les colonnes et les lignes dans le conteneur ttk.Frame
for i in range(2):
    frame.columnconfigure(i, weight=1)

for i in range(4):
    frame.rowconfigure(i, weight=1)

# Ajoutez des coins arrondis avec ttk.Style
style = ttk.Style()
style.configure("TFrame", borderwidth=4, relief="solid", background=bg_color)

# Créez une nouvelle frame pour la création de compte
create_account_frame = ttk.Frame(root, style="TFrame")

# Ajoutez les éléments à la frame de création de compte
new_username_label = tk.Label(create_account_frame, text="Nouveau nom d'utilisateur:", font=font_style, bg=bg_color, fg=fg_color)
new_password_label = tk.Label(create_account_frame, text="Nouveau mot de passe:", font=font_style, bg=bg_color, fg=fg_color)
new_username_entry = tk.Entry(create_account_frame, font=font_style, bg=bg_color, fg=fg_color, highlightbackground=bg_color)
new_password_entry = tk.Entry(create_account_frame, show="*", font=font_style, bg=bg_color, fg=fg_color, highlightbackground=bg_color)
submit_button = tk.Button(create_account_frame, text="Créer le compte", command=submit_account, font=font_style, bg=button_bg_color, fg=button_fg_color, padx=10, pady=5)

# Placez les widgets dans la frame de création de compte en les centrant
new_username_label.grid(row=0, column=0, sticky=tk.E, pady=10, padx=10)
new_username_entry.grid(row=0, column=1, pady=10, padx=10)
new_password_label.grid(row=1, column=0, sticky=tk.E, pady=10, padx=10)
new_password_entry.grid(row=1, column=1, pady=10, padx=10)
submit_button.grid(row=2, column=1, columnspan=2, pady=20, padx=10, sticky=tk.W)

# Centrez les colonnes et les lignes dans la frame de création de compte
for i in range(2):
    create_account_frame.columnconfigure(i, weight=1)

for i in range(3):
    create_account_frame.rowconfigure(i, weight=1)

# Masquez la frame de création de compte au démarrage
create_account_frame.grid_forget()

# Lancez la boucle principale
root.mainloop()
