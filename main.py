import tkinter as tk
from tkinter import  messagebox
import os
from bots.teclado_automatico.teclado_automatico import TecladoAutomatico
from bots.removedor_comentarios.removedor_comentarios import RemovedorComentarios
from bots.automacao_botao.automacao_botao import AutomacaoBotao
from bots.deletor_arquivos.deletor_arquivos import DeletorArquivos
from bots.macro_bot_manager.macro_bot_manager import MacroBotManager

class BotManager:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Gerenciador de Bots")
        self.root.geometry("1250x850")
        
        self.root.iconbitmap("icon.ico") if os.path.exists("icon.ico") else None
        
        self.criar_interface()
        
    def criar_interface(self):
        main_frame = tk.Frame(self.root, padx=20, pady=20)
        main_frame.pack(expand=True, fill=tk.BOTH)
        
        title_frame = tk.Frame(main_frame)
        title_frame.pack(fill=tk.X, pady=10)
        
        tk.Label(title_frame, 
                text="Gerenciador de Bots", 
                font=("Arial", 24, "bold")).pack()
        
        tk.Label(title_frame, 
                text="Selecione um bot para executar", 
                font=("Arial", 12)).pack()
        
        bots_frame = tk.Frame(main_frame)
        bots_frame.pack(expand=True, fill=tk.BOTH, pady=20)
        
        teclado_btn = tk.Button(bots_frame, 
                              text="Teclado Automático", 
                              command=self.abrir_teclado_automatico,
                              width=25, height=3,
                              font=("Arial", 12))
        teclado_btn.pack(pady=10)
        
        automador_btn = tk.Button(bots_frame, 
                                text="Automador de Botões", 
                                command=self.abrir_automador_botoes,
                                width=25, height=3,
                                font=("Arial", 12))
        automador_btn.pack(pady=10)
        
        deletor_btn = tk.Button(bots_frame, 
                              text="Deletor de Arquivos", 
                              command=self.abrir_deletor_arquivos,
                              width=25, height=3,
                              font=("Arial", 12))
        deletor_btn.pack(pady=10)
        
        macro_btn = tk.Button(bots_frame, 
                            text="MacroBotManager", 
                            command=self.abrir_macro_bot,
                            width=25, height=3,
                            font=("Arial", 12))
        macro_btn.pack(pady=10)
        
        removedor_btn = tk.Button(bots_frame, 
                                text="Removedor de Comentários", 
                                command=self.abrir_removedor_comentarios,
                                width=25, height=3,
                                font=("Arial", 12))
        removedor_btn.pack(pady=10)
        
        self.status_bar = tk.Label(main_frame, 
                                 text="Pronto", 
                                 bd=1, 
                                 relief=tk.SUNKEN, 
                                 anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        
    def abrir_teclado_automatico(self):
        try:
            self.root.withdraw()
            app = TecladoAutomatico(self.root)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao abrir teclado automático: {str(e)}")
    
    def abrir_automador_botoes(self):
        try:
            self.root.withdraw()
            app = AutomacaoBotao(self.root)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao abrir automador de botões: {str(e)}")
    
    def abrir_deletor_arquivos(self):
        try:
            self.root.withdraw()
            app = DeletorArquivos(self.root)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao abrir deletor de arquivos: {str(e)}")
    
    def abrir_macro_bot(self):
        try:
            self.root.withdraw()
            app = MacroBotManager(self.root)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao abrir macro bot: {str(e)}")
            
    def abrir_removedor_comentarios(self):
        try:
            self.root.withdraw()
            app = RemovedorComentarios(self.root)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao abrir removedor de comentários: {str(e)}")
    
    def iniciar(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = BotManager()
    app.iniciar()