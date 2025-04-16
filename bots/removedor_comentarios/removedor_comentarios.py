import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
import re

class RemovedorComentarios:
    def __init__(self, root):
        self.root = root
        
        
        self.linguagens = {
            "Java": {
                "extensao": ".java",
                "padroes": [
                    (r'//.*$', ''),  
                    (r'/\*[\s\S]*?\*/', '')  
                ]
            },
            "Python": {
                "extensao": ".py",
                "padroes": [
                    (r'
                    (r'', ''),  
                    (r"", '')  
                ]
            },
            "JavaScript": {
                "extensao": ".js",
                "padroes": [
                    (r'//.*$', ''),  
                    (r'/\*[\s\S]*?\*/', '')  
                ]
            },
            "C/C++": {
                "extensao": [".c", ".cpp", ".h", ".hpp"],
                "padroes": [
                    (r'//.*$', ''),  
                    (r'/\*[\s\S]*?\*/', '')  
                ]
            }
        }
        
        
        self.linguagem_var = tk.StringVar()
        self.modo_var = tk.StringVar(value="Arquivo Único")
        self.path_var = tk.StringVar()
        self.backup_var = tk.BooleanVar(value=True)
        
        
        self.criar_janela()
        
    def criar_janela(self):
        self.window = tk.Toplevel(self.root)
        self.window.title("Removedor de Comentários")
        
        
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
                text="Removedor de Comentários", 
                font=("Arial", 24, "bold")).pack(pady=10)
        
        
        lang_frame = tk.Frame(main_frame)
        lang_frame.pack(fill=tk.X, pady=10)
        
        tk.Label(lang_frame, 
                text="Linguagem:", 
                font=("Arial", 12)).pack(side=tk.LEFT, padx=5)
        
        self.linguagem_var = tk.StringVar(value="Java")
        lang_dropdown = ttk.Combobox(lang_frame, 
                                   textvariable=self.linguagem_var,
                                   values=list(self.linguagens.keys()),
                                   state="readonly",
                                   font=("Arial", 12))
        lang_dropdown.pack(side=tk.LEFT, padx=5)
        
        
        mode_frame = tk.Frame(main_frame)
        mode_frame.pack(fill=tk.X, pady=10)
        
        tk.Label(mode_frame, 
                text="Modo:", 
                font=("Arial", 12)).pack(side=tk.LEFT, padx=5)
        
        self.modo_var = tk.StringVar(value="Arquivo Único")
        mode_dropdown = ttk.Combobox(mode_frame, 
                                   textvariable=self.modo_var,
                                   values=["Arquivo Único", "Pasta Inteira"],
                                   state="readonly",
                                   font=("Arial", 12))
        mode_dropdown.pack(side=tk.LEFT, padx=5)
        
        
        path_frame = tk.Frame(main_frame)
        path_frame.pack(fill=tk.X, pady=10)
        
        tk.Label(path_frame, 
                text="Caminho:", 
                font=("Arial", 12)).pack(side=tk.LEFT, padx=5)
        
        self.path_var = tk.StringVar()
        path_entry = tk.Entry(path_frame, 
                            textvariable=self.path_var,
                            width=40,
                            font=("Arial", 12))
        path_entry.pack(side=tk.LEFT, padx=5)
        
        browse_btn = tk.Button(path_frame, 
                             text="Procurar", 
                             command=self.selecionar_caminho,
                             font=("Arial", 12))
        browse_btn.pack(side=tk.LEFT, padx=5)
        
        
        options_frame = tk.Frame(main_frame)
        options_frame.pack(fill=tk.X, pady=10)
        
        self.backup_var = tk.BooleanVar(value=True)
        backup_check = tk.Checkbutton(options_frame, 
                                    text="Criar backup antes de remover",
                                    variable=self.backup_var,
                                    font=("Arial", 12))
        backup_check.pack(side=tk.LEFT, padx=5)
        
        
        remove_btn = tk.Button(main_frame, 
                             text="Remover Comentários", 
                             command=self.remover_comentarios,
                             width=20, height=2,
                             font=("Arial", 12))
        remove_btn.pack(pady=20)
        
        
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
        messagebox.showinfo("Sobre", "Removedor de Comentários v1.0\n\nUm bot para remover comentários de código fonte.")
        
    def obter_extensoes(self):
        linguagem = self.linguagem_var.get()
        if not linguagem:  
            linguagem = "Java"  
            self.linguagem_var.set(linguagem)
            
        extensoes = self.linguagens[linguagem]["extensao"]
        
        
        if isinstance(extensoes, list):
            return [("Arquivos " + linguagem, ext) for ext in extensoes]
        
        
        return [("Arquivos " + linguagem, extensoes)]
        
    def selecionar_caminho(self):
        if self.modo_var.get() == "Arquivo Único":
            
            filetypes = self.obter_extensoes() + [("Todos os arquivos", "*.*")]
            caminho = filedialog.askopenfilename(
                title="Selecione o arquivo",
                filetypes=filetypes
            )
        else:
            caminho = filedialog.askdirectory(
                title="Selecione a pasta"
            )
            
        if caminho:
            self.path_var.set(caminho)
            
    def remover_comentarios(self):
        caminho = self.path_var.get()
        if not caminho:
            messagebox.showerror("Erro", "Selecione um arquivo ou pasta")
            return
            
        linguagem = self.linguagem_var.get()
        padroes = self.linguagens[linguagem]["padroes"]
        
        try:
            if self.modo_var.get() == "Arquivo Único":
                self.processar_arquivo(caminho, padroes)
            else:
                self.processar_pasta(caminho, padroes)
                
            self.status_bar.config(text="Comentários removidos com sucesso!")
            messagebox.showinfo("Sucesso", "Comentários removidos com sucesso!")
        except Exception as e:
            self.status_bar.config(text=f"Erro: {str(e)}")
            messagebox.showerror("Erro", f"Erro ao remover comentários: {str(e)}")
            
    def processar_arquivo(self, caminho, padroes):
        if self.backup_var.get():
            self.criar_backup(caminho)
            
        with open(caminho, 'r', encoding='utf-8') as f:
            conteudo = f.read()
            
        for padrao, substituicao in padroes:
            conteudo = re.sub(padrao, substituicao, conteudo, flags=re.MULTILINE)
            
        with open(caminho, 'w', encoding='utf-8') as f:
            f.write(conteudo)
            
    def processar_pasta(self, caminho, padroes):
        linguagem = self.linguagem_var.get()
        extensoes = self.linguagens[linguagem]["extensao"]
        if not isinstance(extensoes, list):
            extensoes = [extensoes]
            
        arquivos_processados = 0
        for root, _, files in os.walk(caminho):
            for file in files:
                if any(file.endswith(ext) for ext in extensoes):
                    arquivo_path = os.path.join(root, file)
                    self.processar_arquivo(arquivo_path, padroes)
                    arquivos_processados += 1
                    
        if arquivos_processados == 0:
            raise Exception(f"Nenhum arquivo {linguagem} encontrado na pasta selecionada")
            
    def criar_backup(self, caminho):
        backup_path = caminho + ".backup"
        with open(caminho, 'r', encoding='utf-8') as f:
            conteudo = f.read()
        with open(backup_path, 'w', encoding='utf-8') as f:
            f.write(conteudo) 