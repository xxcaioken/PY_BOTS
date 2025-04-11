import tkinter as tk
from tkinter import messagebox
from . import database
from . import keyboard_listener

def center_window(window, width, height):
    
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    position_top = int(screen_height / 2 - height / 2)
    position_right = int(screen_width / 2 - width / 2)
    window.geometry(f'{width}x{height}+{position_right}+{position_top}')

def add_shortcut():
    
    key = entry_key.get()
    text = text_content.get("1.0", tk.END).strip()

    if key and text:
        database.add_shortcut(key, text)
        update_list()
        keyboard_listener.load_shortcuts()
        entry_key.delete(0, tk.END)
        text_content.delete("1.0", tk.END)
    else:
        messagebox.showwarning("Erro", "Preencha todos os campos!")

def update_shortcut():
    
    selected = listbox.curselection()
    if selected:
        key = listbox.get(selected[0]).split(" -> ")[0]
        new_text = text_content.get("1.0", tk.END).strip()

        if new_text:
            database.update_shortcut(key, new_text)
            update_list()
            keyboard_listener.load_shortcuts()
        else:
            messagebox.showwarning("Erro", "Digite um novo texto para o atalho.")
    else:
        messagebox.showwarning("Erro", "Selecione um atalho para editar.")

def delete_shortcut():
    
    selected = listbox.curselection()
    if selected:
        key = listbox.get(selected[0]).split(" -> ")[0]
        database.delete_shortcut(key)
        update_list()
        keyboard_listener.load_shortcuts()
    else:
        messagebox.showwarning("Erro", "Selecione um atalho para remover.")

def update_list():
    
    listbox.delete(0, tk.END)
    for key, text in database.get_shortcuts():
        display_text = text.replace("\n", " | ")
        listbox.insert(tk.END, f"{key} -> {display_text}")

def open_shortcut_manager():
    
    global entry_key, text_content, listbox

    manager_window = tk.Toplevel()
    manager_window.title("Gerenciador de Atalhos")
    
    center_window(manager_window, 400, 400)

    tk.Label(manager_window, text="Tecla:").pack()
    entry_key = tk.Entry(manager_window)
    entry_key.pack()

    tk.Label(manager_window, text="Texto (com quebra de linha):").pack()
    text_content = tk.Text(manager_window, height=5, width=40)
    text_content.pack()

    tk.Button(manager_window, text="Adicionar", command=add_shortcut).pack(pady=5)
    tk.Button(manager_window, text="Editar", command=update_shortcut).pack(pady=5)
    tk.Button(manager_window, text="Remover", command=delete_shortcut).pack(pady=5)

    listbox = tk.Listbox(manager_window)
    listbox.pack(fill=tk.BOTH, expand=True)
    update_list()
    
    tk.Button(manager_window, text="Fechar", command=manager_window.destroy).pack(pady=5)
