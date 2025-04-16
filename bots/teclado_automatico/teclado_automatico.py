import threading
import tkinter as tk
import time
import pyautogui
from random import randrange
from tkinter import ttk, messagebox

class TecladoAutomatico:
    def __init__(self, root):
        self.root = root
        self.rodando_loop = False
        self.thread_loop = None
        self.alfabeto = [chr(i) for i in range(ord('a'), ord('z')+1)]
        self.esta_ativo = False
        
        
        self.criar_janela()
        
    def criar_janela(self):
        self.window = tk.Toplevel(self.root)
        self.window.title("Teclado Automático")
        
        
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
                text="Teclado Automático", 
                font=("Arial", 24, "bold")).pack(pady=10)
        
        
        text_frame = tk.Frame(main_frame)
        text_frame.pack(fill=tk.X, pady=10)
        
        tk.Label(text_frame, 
                text="Texto para digitar:", 
                font=("Arial", 12)).pack(side=tk.LEFT, padx=5)
        
        self.texto_var = tk.StringVar()
        self.texto_entry = tk.Entry(text_frame, 
                                  textvariable=self.texto_var,
                                  width=40,
                                  font=("Arial", 12))
        self.texto_entry.pack(side=tk.LEFT, padx=5)
        
        
        config_frame = tk.Frame(main_frame)
        config_frame.pack(fill=tk.X, pady=10)
        
        
        tk.Label(config_frame, 
                text="Intervalo (segundos):", 
                font=("Arial", 12)).pack(side=tk.LEFT, padx=5)
        
        self.intervalo_var = tk.StringVar(value="5")
        self.intervalo_entry = tk.Entry(config_frame, 
                                      textvariable=self.intervalo_var,
                                      width=5,
                                      font=("Arial", 12))
        self.intervalo_entry.pack(side=tk.LEFT, padx=5)
        
        
        self.repetir_var = tk.BooleanVar(value=True)
        tk.Checkbutton(config_frame, 
                      text="Repetir", 
                      variable=self.repetir_var,
                      font=("Arial", 12)).pack(side=tk.LEFT, padx=20)
        
        
        tk.Label(config_frame, 
                text="Vezes:", 
                font=("Arial", 12)).pack(side=tk.LEFT, padx=5)
        
        self.vezes_var = tk.StringVar(value="1")
        self.vezes_entry = tk.Entry(config_frame, 
                                  textvariable=self.vezes_var,
                                  width=5,
                                  font=("Arial", 12))
        self.vezes_entry.pack(side=tk.LEFT, padx=5)
        
        
        buttons_frame = tk.Frame(main_frame)
        buttons_frame.pack(pady=20)
        
        self.start_btn = tk.Button(buttons_frame, 
                                 text="Iniciar", 
                                 command=self.iniciar_digitacao,
                                 width=20, height=2,
                                 font=("Arial", 12))
        self.start_btn.pack(side=tk.LEFT, padx=10)
        
        self.stop_btn = tk.Button(buttons_frame, 
                                text="Parar", 
                                command=self.parar_digitacao,
                                width=20, height=2,
                                font=("Arial", 12))
        self.stop_btn.pack(side=tk.LEFT, padx=10)
        
        
        self.status_bar = tk.Label(main_frame, 
                                 text="Pronto", 
                                 bd=1, 
                                 relief=tk.SUNKEN, 
                                 anchor=tk.W,
                                 font=("Arial", 12))
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        
        
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
        
    def on_closing(self):
        
        tamanho_atual = self.window.geometry()
        self.window.destroy()
        self.root.deiconify()  
        self.root.geometry(tamanho_atual)  
        
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
        messagebox.showinfo("Sobre", "Teclado Automático v1.0\n\nUm bot para digitar automaticamente.")

    def iniciar_digitacao(self):
        self.rodando_loop = True
        self.thread_loop = threading.Thread(target=self.executar)
        self.thread_loop.daemon = True
        self.thread_loop.start()
        self.start_btn.config(state=tk.DISABLED)
        self.stop_btn.config(state=tk.NORMAL)
        self.status_bar.config(text="Digitando...")

    def parar_digitacao(self):
        self.rodando_loop = False
        self.start_btn.config(state=tk.NORMAL)
        self.stop_btn.config(state=tk.DISABLED)
        self.status_bar.config(text="Pronto")

    def executar(self):
        while self.rodando_loop:
            time.sleep(float(self.intervalo_var.get()))
            tecla = self.alfabeto[randrange(len(self.alfabeto))]
            pyautogui.press(tecla) 