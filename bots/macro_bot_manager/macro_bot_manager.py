import tkinter as tk
import threading
import logging
from . import keyboard_listener
from . import shortcut_manager

class MacroBotManager:
    def __init__(self, root):
        self.root = root
        self.root.title("MacroBotManager")
        self.root.geometry("400x300")
        self.criar_interface()
        
    def criar_interface(self):
        main_frame = tk.Frame(self.root, padx=20, pady=20)
        main_frame.pack(expand=True, fill=tk.BOTH)
        
        
        tk.Label(main_frame, 
                text="Controle do Bot de Teclado", 
                font=("Arial", 16)).pack(pady=10)
        
        
        botoes_frame = tk.Frame(main_frame)
        botoes_frame.pack(expand=True, fill=tk.BOTH, pady=20)
        
        
        tk.Button(botoes_frame, 
                 text="Iniciar Bot", 
                 command=self.start_script,
                 width=20).pack(pady=5)
        
        
        tk.Button(botoes_frame, 
                 text="Parar Bot", 
                 command=self.stop_script,
                 width=20).pack(pady=5)
        
        
        tk.Button(botoes_frame, 
                 text="Gerenciar Atalhos", 
                 command=self.abrir_gerenciador_atalhos,
                 width=20).pack(pady=5)
        
        
        self.status_bar = tk.Label(main_frame, 
                                 text="Pronto", 
                                 bd=1, 
                                 relief=tk.SUNKEN, 
                                 anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        
        
        self.center_window(self.root, 400, 300)

    def center_window(self, window, width, height):
        
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        position_top = int(screen_height / 2 - height / 2)
        position_right = int(screen_width / 2 - width / 2)
        window.geometry(f'{width}x{height}+{position_right}+{position_top}')

    def start_script(self):
        
        try:
            thread = threading.Thread(target=keyboard_listener.start_keyboard_listener, daemon=True)
            thread.start()
            self.status_bar.config(text="Bot iniciado")
        except Exception as e:
            self.status_bar.config(text=f"Erro: {str(e)}")
    
    def stop_script(self):
        
        try:
            keyboard_listener.stop_keyboard_listener()
            self.status_bar.config(text="Bot parado")
        except Exception as e:
            self.status_bar.config(text=f"Erro: {str(e)}")

    def abrir_gerenciador_atalhos(self):
        
        try:
            shortcut_manager.open_shortcut_manager()
        except Exception as e:
            self.status_bar.config(text=f"Erro: {str(e)}")
 