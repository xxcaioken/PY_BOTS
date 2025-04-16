import pyautogui
import time
import tkinter as tk
from tkinter import messagebox, ttk, filedialog
import os
import sys
import subprocess
import threading

def verificar_dependencias():
    try:
        import cv2
        return True
    except ImportError:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "opencv-python"])
            return True
        except:
            return False

class AutomacaoBotao:
    def __init__(self, root):
        if not verificar_dependencias():
            messagebox.showerror("Erro", "Não foi possível instalar o OpenCV. O programa não funcionará corretamente.")
            sys.exit(1)
            
        self.root = root
        self.window = tk.Toplevel(root)
        self.window.title("Automador de Botões")
        self.window.geometry(root.geometry())
        
        
        self.centralizar_janela()
        
        self.rodando_loop = False
        self.thread_loop = None
        
        
        self.criar_menu()
        
        self.criar_interface()
        
        
        self.root.withdraw()
        
    def centralizar_janela(self):
        
        self.window.update_idletasks()
        
        
        largura_tela = self.window.winfo_screenwidth()
        altura_tela = self.window.winfo_screenheight()
        
        
        largura_janela = self.window.winfo_width()
        altura_janela = self.window.winfo_height()
        
        
        x = (largura_tela - largura_janela) // 2
        y = (altura_tela - altura_janela) // 2
        
        
       
        
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
                text="Automador de Botões", 
                font=("Arial", 24, "bold")).pack(pady=10)
        
        
        image_frame = tk.Frame(main_frame)
        image_frame.pack(fill=tk.X, pady=10)
        
        tk.Label(image_frame, 
                text="Imagem do botão:", 
                font=("Arial", 12)).pack(side=tk.LEFT, padx=5)
        
        self.image_path = tk.StringVar()
        self.image_entry = tk.Entry(image_frame, 
                                  textvariable=self.image_path,
                                  width=40,
                                  font=("Arial", 12))
        self.image_entry.pack(side=tk.LEFT, padx=5)
        
        browse_btn = tk.Button(image_frame, 
                             text="Procurar", 
                             command=self.selecionar_imagem,
                             font=("Arial", 12))
        browse_btn.pack(side=tk.LEFT, padx=5)
        
        
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
                                 command=self.iniciar_automacao,
                                 width=20, height=2,
                                 font=("Arial", 12))
        self.start_btn.pack(side=tk.LEFT, padx=10)
        
        self.stop_btn = tk.Button(buttons_frame, 
                                text="Parar", 
                                command=self.parar_automacao,
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
        self.window.destroy()
        self.root.deiconify()  
        
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
        messagebox.showinfo("Sobre", "Automador de Botões v1.0\n\nUm bot para automatizar cliques em botões usando reconhecimento de imagem.")
    
    def selecionar_imagem(self):
        filetypes = (
            ('Imagens', '*.png *.jpg *.jpeg *.bmp'),
            ('Todos os arquivos', '*.*')
        )
        filename = filedialog.askopenfilename(
            title='Selecione a imagem do botão',
            filetypes=filetypes
        )
        if filename:
            self.image_path.set(filename)
            
    def encontrar_e_clicar_no_botao(self, imagem_do_botao=None):
        try:
            if imagem_do_botao is None:
                imagem_do_botao = self.image_path.get()
                
            if not os.path.exists(imagem_do_botao):
                raise FileNotFoundError(f"Arquivo de imagem '{imagem_do_botao}' não encontrado")
            
            self.status_bar.config(text="Status: Procurando botão...")
            self.window.update()
            
            localizacao = pyautogui.locateCenterOnScreen(imagem_do_botao, confidence=0.8)
            
            if localizacao:
                pyautogui.moveTo(localizacao, duration=1)
                pyautogui.click()
                self.status_bar.config(text="Status: Botão clicado com sucesso!")
                if not self.rodando_loop:
                    messagebox.showinfo("Sucesso", "Botão clicado com sucesso!")
            else:
                self.status_bar.config(text="Status: Botão não encontrado")
                if not self.rodando_loop:
                    messagebox.showwarning("Aviso", "Botão não encontrado na tela. Verifique a imagem ou a posição.")
        except Exception as e:
            self.status_bar.config(text=f"Status: Erro - {str(e)}")
            if not self.rodando_loop:
                messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")
    
    def loop_automacao(self):
        while self.rodando_loop:
            self.encontrar_e_clicar_no_botao()
            time.sleep(int(self.intervalo_var.get()))
    
    def toggle_loop(self):
        if not self.rodando_loop:
            self.rodando_loop = True
            self.stop_btn.config(text="Parar Loop", bg="red")
            self.start_btn.config(state=tk.DISABLED)
            self.progress.start()
            self.thread_loop = threading.Thread(target=self.loop_automacao)
            self.thread_loop.daemon = True
            self.thread_loop.start()
        else:
            self.rodando_loop = False
            self.stop_btn.config(text="Modo Loop", bg="SystemButtonFace")
            self.start_btn.config(state=tk.NORMAL)
            self.progress.stop()
    
    def iniciar_automacao(self):
        self.encontrar_e_clicar_no_botao()

    def parar_automacao(self):
        self.rodando_loop = False
        self.stop_btn.config(text="Parar", bg="SystemButtonFace")
        self.start_btn.config(state=tk.NORMAL)
        self.progress.stop()