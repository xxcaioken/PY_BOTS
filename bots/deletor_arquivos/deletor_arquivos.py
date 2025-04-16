import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
import shutil
import pyautogui

class DeletorArquivos:
    def __init__(self, root):
        self.root = root
        self.arquivos_selecionados = []
        
        
        self.criar_janela()
        
    def criar_janela(self):
        self.window = tk.Toplevel(self.root)
        self.window.title("Deletor de Arquivos")
        
        
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
                text="Deletor de Arquivos", 
                font=("Arial", 16)).pack(pady=10)
        
        dir_frame = tk.Frame(main_frame)
        dir_frame.pack(fill=tk.X, pady=10)
        
        tk.Label(dir_frame, text="Diretório:").pack(side=tk.LEFT, padx=5)
        self.entrada_diretorio = tk.Entry(dir_frame, width=50)
        self.entrada_diretorio.pack(side=tk.LEFT, padx=5)
        tk.Button(dir_frame, 
                 text="Selecionar", 
                 command=self.escolher_diretorio).pack(side=tk.LEFT, padx=5)
        
        opcoes_frame = tk.Frame(main_frame)
        opcoes_frame.pack(fill=tk.X, pady=10)
        
        tk.Label(opcoes_frame, text="Escolha o tipo de exclusão:").pack(side=tk.LEFT, padx=5)
        self.opcao_escolhida = tk.StringVar()
        self.opcao_escolhida.set("Excluir arquivos de um tipo")
        dropdown = tk.OptionMenu(opcoes_frame, 
                               self.opcao_escolhida, 
                               "Excluir arquivos de um tipo", 
                               "Excluir pasta inteira",
                               command=self.atualizar_interface)
        dropdown.pack(side=tk.LEFT, padx=5)
        
        self.ext_frame = tk.Frame(main_frame)
        self.ext_frame.pack(fill=tk.X, pady=10)
        
        tk.Label(self.ext_frame, text="Extensão (por exemplo, .txt):").pack(side=tk.LEFT, padx=5)
        self.entrada_extensao = tk.Entry(self.ext_frame, width=30)
        self.entrada_extensao.pack(side=tk.LEFT, padx=5)
        
        self.var_pular_avisos = tk.BooleanVar()
        check_pular_avisos = tk.Checkbutton(main_frame, 
                                          text="Pular avisos de arquivos deletados", 
                                          variable=self.var_pular_avisos)
        check_pular_avisos.pack(pady=10)
        
        lista_frame = tk.Frame(main_frame)
        lista_frame.pack(expand=True, fill=tk.BOTH, pady=10)
        
        scrollbar = tk.Scrollbar(lista_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.lista_arquivos = tk.Listbox(lista_frame, 
                                       selectmode=tk.MULTIPLE,
                                       yscrollcommand=scrollbar.set)
        self.lista_arquivos.pack(expand=True, fill=tk.BOTH)
        
        scrollbar.config(command=self.lista_arquivos.yview)
        
        tk.Button(main_frame, 
                 text="Deletar", 
                 command=self.deletar_arquivos,
                 width=15).pack(pady=10)
        
        self.status_bar = tk.Label(main_frame, 
                                 text="Pronto", 
                                 bd=1, 
                                 relief=tk.SUNKEN, 
                                 anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        
        self.atualizar_interface()
        
        
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
        messagebox.showinfo("Sobre", "Deletor de Arquivos v1.0\n\nUm bot para deletar arquivos por extensão ou pastas inteiras.")
        
    def escolher_diretorio(self):
        caminho_diretorio = filedialog.askdirectory()
        self.entrada_diretorio.delete(0, tk.END)
        self.entrada_diretorio.insert(0, caminho_diretorio)
        self.atualizar_lista_arquivos()
        
    def atualizar_interface(self, *args):
        if self.opcao_escolhida.get() == "Excluir arquivos de um tipo":
            self.ext_frame.pack(fill=tk.X, pady=10)
        else:
            self.ext_frame.pack_forget()
        self.atualizar_lista_arquivos()
        
    def atualizar_lista_arquivos(self):
        self.lista_arquivos.delete(0, tk.END)
        diretorio = self.entrada_diretorio.get()
        
        if not diretorio or not os.path.exists(diretorio):
            return
            
        if self.opcao_escolhida.get() == "Excluir arquivos de um tipo":
            extensao = self.entrada_extensao.get()
            for arquivo in os.listdir(diretorio):
                if arquivo.endswith(extensao):
                    caminho_arquivo = os.path.join(diretorio, arquivo)
                    self.lista_arquivos.insert(tk.END, caminho_arquivo)
        else:
            for arquivo in os.listdir(diretorio):
                caminho_arquivo = os.path.join(diretorio, arquivo)
                self.lista_arquivos.insert(tk.END, caminho_arquivo)
                
    def deletar_arquivos(self):
        diretorio = self.entrada_diretorio.get()
        extensao = self.entrada_extensao.get()
        pular_avisos = self.var_pular_avisos.get()
        escolha = self.opcao_escolhida.get()

        try:
            if escolha == "Excluir pasta inteira":
                shutil.rmtree(diretorio)
                messagebox.showinfo("Sucesso", f"A pasta '{diretorio}' foi deletada completamente!")
            elif escolha == "Excluir arquivos de um tipo":
                arquivos_deletados = 0
                for arquivo in os.listdir(diretorio):
                    if arquivo.endswith(extensao):
                        caminho_arquivo = os.path.join(diretorio, arquivo)
                        os.remove(caminho_arquivo)
                        arquivos_deletados += 1
                        if not pular_avisos:
                            messagebox.showinfo("Arquivo Deletado", f"Arquivo deletado: {caminho_arquivo}")

                if arquivos_deletados > 0:
                    messagebox.showinfo("Sucesso", f"Todos os {arquivos_deletados} arquivo(s) foram deletados!")
                else:
                    messagebox.showwarning("Aviso", "Nenhum arquivo foi encontrado para deletar.")
            
            self.atualizar_lista_arquivos()
            
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao deletar arquivos: {str(e)}") 