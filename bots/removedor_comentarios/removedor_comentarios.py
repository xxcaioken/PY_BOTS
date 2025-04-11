import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
import re

class RemovedorComentarios:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Removedor de Comentários")
        self.root.geometry("600x400")
        
        
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
                    (r'#.*$', ''),
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
        
        self.criar_interface()
        
    def criar_interface(self):
        
        main_frame = tk.Frame(self.root, padx=20, pady=20)
        main_frame.pack(expand=True, fill=tk.BOTH)
        
        
        tk.Label(main_frame, 
                text="Removedor de Comentários", 
                font=("Arial", 16, "bold")).pack(pady=10)
        
        
        lang_frame = tk.Frame(main_frame)
        lang_frame.pack(fill=tk.X, pady=10)
        
        tk.Label(lang_frame, text="Linguagem:").pack(side=tk.LEFT, padx=5)
        lang_dropdown = ttk.Combobox(lang_frame, 
                                   textvariable=self.linguagem_var,
                                   values=list(self.linguagens.keys()),
                                   state="readonly")
        lang_dropdown.pack(side=tk.LEFT, padx=5)
        
        
        lang_dropdown.bind('<<ComboboxSelected>>', lambda e: self.linguagem_var.set(lang_dropdown.get()))
        
        
        mode_frame = tk.Frame(main_frame)
        mode_frame.pack(fill=tk.X, pady=10)
        
        tk.Label(mode_frame, text="Modo:").pack(side=tk.LEFT, padx=5)
        mode_dropdown = ttk.Combobox(mode_frame, 
                                   textvariable=self.modo_var,
                                   values=["Arquivo Único", "Pasta Inteira"],
                                   state="readonly")
        mode_dropdown.pack(side=tk.LEFT, padx=5)
        
        
        mode_dropdown.bind('<<ComboboxSelected>>', lambda e: self.modo_var.set(mode_dropdown.get()))
        
        
        path_frame = tk.Frame(main_frame)
        path_frame.pack(fill=tk.X, pady=10)
        
        tk.Label(path_frame, text="Caminho:").pack(side=tk.LEFT, padx=5)
        path_entry = tk.Entry(path_frame, textvariable=self.path_var, width=40)
        path_entry.pack(side=tk.LEFT, padx=5)
        
        browse_btn = tk.Button(path_frame, 
                             text="Procurar", 
                             command=self.selecionar_caminho)
        browse_btn.pack(side=tk.LEFT, padx=5)
        
        
        options_frame = tk.Frame(main_frame)
        options_frame.pack(fill=tk.X, pady=10)
        
        backup_check = tk.Checkbutton(options_frame, 
                                    text="Criar backup antes de remover",
                                    variable=self.backup_var)
        backup_check.pack(side=tk.LEFT, padx=5)
        
        
        remove_btn = tk.Button(main_frame, 
                             text="Remover Comentários", 
                             command=self.remover_comentarios,
                             width=20, height=2)
        remove_btn.pack(pady=20)
        
        
        self.status_bar = tk.Label(main_frame, 
                                 text="Pronto", 
                                 bd=1, 
                                 relief=tk.SUNKEN, 
                                 anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        
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
            
    def iniciar(self):
        self.root.mainloop() 