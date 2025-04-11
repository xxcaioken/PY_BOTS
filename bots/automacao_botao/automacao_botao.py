import pyautogui
import time
import tkinter as tk
from tkinter import messagebox, ttk
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
    def __init__(self):
        if not verificar_dependencias():
            messagebox.showerror("Erro", "Não foi possível instalar o OpenCV. O programa não funcionará corretamente.")
            sys.exit(1)
            
        self.root = tk.Tk()
        self.root.title("Automador de Botões")
        self.root.geometry("500x400")
        
        self.rodando_loop = False
        self.thread_loop = None
        
        self.criar_interface()
        
    def criar_interface(self):
        
        main_frame = tk.Frame(self.root, padx=20, pady=20)
        main_frame.pack(expand=True)
        
        
        tk.Label(main_frame, text="Automador de Botões", font=("Arial", 16)).pack(pady=10)
        tk.Label(main_frame, text="Escolha o modo de operação:").pack(pady=5)
        
        
        modo_frame = tk.Frame(main_frame)
        modo_frame.pack(pady=10)
        
        
        self.botao_unico = tk.Button(modo_frame, text="Modo Único", 
                                   command=self.iniciar_automacao,
                                   width=15, height=2)
        self.botao_unico.pack(side=tk.LEFT, padx=5)
        
        
        self.botao_loop = tk.Button(modo_frame, text="Modo Loop", 
                                  command=self.toggle_loop,
                                  width=15, height=2)
        self.botao_loop.pack(side=tk.LEFT, padx=5)
        
        
        self.loop_frame = tk.Frame(main_frame)
        self.loop_frame.pack(pady=10)
        
        
        tk.Label(self.loop_frame, text="Intervalo (segundos):").pack(side=tk.LEFT, padx=5)
        self.intervalo = tk.Spinbox(self.loop_frame, from_=1, to=60, width=5)
        self.intervalo.pack(side=tk.LEFT, padx=5)
        self.intervalo.delete(0, tk.END)
        self.intervalo.insert(0, "5")
        
        
        self.status_label = tk.Label(main_frame, text="Status: Aguardando...")
        self.status_label.pack(pady=10)
        
        
        self.progress = ttk.Progressbar(main_frame, length=300, mode='indeterminate')
        self.progress.pack(pady=10)
        
    def encontrar_e_clicar_no_botao(self, imagem_do_botao):
        try:
            if not os.path.exists(imagem_do_botao):
                raise FileNotFoundError(f"Arquivo de imagem '{imagem_do_botao}' não encontrado")
            
            self.status_label.config(text="Status: Procurando botão...")
            self.root.update()
            
            localizacao = pyautogui.locateCenterOnScreen(imagem_do_botao, confidence=0.8)
            
            if localizacao:
                pyautogui.moveTo(localizacao, duration=1)
                pyautogui.click()
                self.status_label.config(text="Status: Botão clicado com sucesso!")
                if not self.rodando_loop:
                    messagebox.showinfo("Sucesso", "Botão clicado com sucesso!")
            else:
                self.status_label.config(text="Status: Botão não encontrado")
                if not self.rodando_loop:
                    messagebox.showwarning("Aviso", "Botão não encontrado na tela. Verifique a imagem ou a posição.")
        except Exception as e:
            self.status_label.config(text=f"Status: Erro - {str(e)}")
            if not self.rodando_loop:
                messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")
    
    def loop_automacao(self):
        while self.rodando_loop:
            self.encontrar_e_clicar_no_botao("bots/automacao_botao/Botao.png")
            time.sleep(int(self.intervalo.get()))
    
    def toggle_loop(self):
        if not self.rodando_loop:
            self.rodando_loop = True
            self.botao_loop.config(text="Parar Loop", bg="red")
            self.botao_unico.config(state=tk.DISABLED)
            self.progress.start()
            self.thread_loop = threading.Thread(target=self.loop_automacao)
            self.thread_loop.daemon = True
            self.thread_loop.start()
        else:
            self.rodando_loop = False
            self.botao_loop.config(text="Modo Loop", bg="SystemButtonFace")
            self.botao_unico.config(state=tk.NORMAL)
            self.progress.stop()
    
    def iniciar_automacao(self):
        self.encontrar_e_clicar_no_botao("bots/automacao_botao/Botao.png")
    
    def iniciar(self):
        self.root.mainloop() 