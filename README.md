# Gerenciador de Bots

Uma interface unificada para gerenciar diferentes bots de automação.

## Bots Disponíveis

1. **Teclado Automático**
   - Simula pressionamento aleatório de teclas
   - Interface simples com botão de start/stop

2. **Automador de Botões**
   - Procura e clica em botões na tela usando reconhecimento de imagem
   - Suporta modo único e modo loop
   - Configurável intervalo entre tentativas

3. **Deletor de Arquivos**
   - Interface para gerenciar deleção de arquivos
   - Duas opções de exclusão:
     - **Excluir arquivos de um tipo**: Deleta arquivos com uma extensão específica
     - **Excluir pasta inteira**: Remove todo o conteúdo de um diretório
   - Lista de arquivos para visualização
   - Opção para pular avisos de arquivos deletados
   - Feedback visual de sucesso/falha
   - Atualização automática da lista após deleção

4. **MacroBotManager**
   - Interface gráfica para gerenciamento de macros
   - Suporte para criação e execução de macros personalizadas
   - Interface intuitiva e fácil de usar
   - Compilação para executável disponível

## Requisitos

- Python 3.8 ou superior
- Dependências listadas em `requirements.txt` 

## Instalação
(como admin no windows)
1. Clone o repositório
2. Crie um ambiente virtual:
   ```bash
   python -m venv .venv
   ```
3. Ative o ambiente virtual:
   - Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - Linux/Mac:
     ```bash
     source .venv/bin/activate
     ```
4. Instale as dependências:
   ```bash
   pip install -r bots/requirements.txt
   ```

## Uso

Execute o programa principal:
```bash
python main.py
```

Para compilar o MacroBotManager como executável:
```bash
pyinstaller --onefile --noconsole main.py
```

## Estrutura do Projeto

```
bots/
├── teclado_automatico/
│   ├── __init__.py
│   └── teclado_automatico.py
├── automacao_botao/
│   ├── __init__.py
│   └── automacao_botao.py
├── deletor_arquivos/
│   ├── __init__.py
│   └── deletor_arquivos.py
├── macro_bot_manager/
│   ├── __init__.py
│   └── gui.py
├── __init__.py
├── main.py
├── requirements.txt
└── README.md
``` 