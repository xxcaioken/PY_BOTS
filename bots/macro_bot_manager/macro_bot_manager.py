import tkinter as tk
import threading
import logging
from . import keyboard_listener
from . import shortcut_manager
import tkinter.messagebox as messagebox

class MacroBotManager:
    def __init__(self, root):
        self.root = root
        
        
        self.criar_janela()
        
    def criar_janela(self):
        self.window = tk.Toplevel(self.root)
        self.window.title("MacroBotManager")
        
        
        tamanho_atual = self.root.geometry()
        
        
        self.root.withdraw()
        
        
        self.window.geometry(tamanho_atual)
        
        
        self.criar_menu()
        
        
        self.criar_interface()
        
    def criar_menu(self):
        menubar = tk.Menu(self.window)
        self.window.config(menu=menubar)
        
        
        bots_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Bots", menu=bots_menu)
        
        bots_menu.add_command(label="Teclado Automático", command=self.abrir_teclado_automatico)
        bots_menu.add_command(label="Automador de Botões", command=self.abrir_automador_botoes)
        bots_menu.add_command(label="Deletor de Arquivos", command=self.abrir_deletor_arquivos)
        bots_menu.add_command(label="MacroBotManager", command=self.abrir_macro_bot)
        bots_menu.add_command(label="Removedor de Comentários", command=self.abrir_removedor_comentarios)
        
        
        ajuda_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Ajuda", menu=ajuda_menu)
        ajuda_menu.add_command(label="Sobre", command=self.mostrar_sobre)
        
    def criar_interface(self):
        main_frame = tk.Frame(self.window, padx=20, pady=20)
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
        
        self.center_window(self.window, 400, 300)
        
        
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        
        tamanho_atual = self.window.geometry()
        self.window.destroy()
        self.root.deiconify()  
        self.root.geometry(tamanho_atual)  

    def center_window(self, window, width, height):
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        position_top = int(screen_height / 2 - height / 2)
        position_right = int(screen_width / 2 - width / 2)
       

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
            
    def abrir_teclado_automatico(self):
        try:
            from bots.teclado_automatico.teclado_automatico import TecladoAutomatico
            self.window.destroy()
            app = TecladoAutomatico(self.root)
        except Exception as e:
            self.status_bar.config(text=f"Erro: {str(e)}")
            
    def abrir_automador_botoes(self):
        try:
            from bots.automacao_botao.automacao_botao import AutomacaoBotao
            self.window.destroy()
            app = AutomacaoBotao(self.root)
        except Exception as e:
            self.status_bar.config(text=f"Erro: {str(e)}")
            
    def abrir_deletor_arquivos(self):
        try:
            from bots.deletor_arquivos.deletor_arquivos import DeletorArquivos
            self.window.destroy()
            app = DeletorArquivos(self.root)
        except Exception as e:
            self.status_bar.config(text=f"Erro: {str(e)}")
            
    def abrir_macro_bot(self):
        try:
            from bots.macro_bot_manager.macro_bot_manager import MacroBotManager
            self.window.destroy()
            app = MacroBotManager(self.root)
        except Exception as e:
            self.status_bar.config(text=f"Erro: {str(e)}")
            
    def abrir_removedor_comentarios(self):
        try:
            from bots.removedor_comentarios.removedor_comentarios import RemovedorComentarios
            self.window.destroy()
            app = RemovedorComentarios(self.root)
        except Exception as e:
            self.status_bar.config(text=f"Erro: {str(e)}")
            
    def mostrar_sobre(self):
        messagebox.showinfo("Sobre", "MacroBotManager v1.0\n\nUm bot para gerenciar atalhos de teclado.")
 