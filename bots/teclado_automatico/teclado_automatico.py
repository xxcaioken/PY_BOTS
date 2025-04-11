import threading
import tkinter as tk
import time
import pyautogui
from random import randrange

class TecladoAutomatico:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Teclado Automático")
        self.root.geometry("200x100")
        self.root.geometry("+800+350")

        self.alfabeto = [chr(i) for i in range(ord('a'), ord('z')+1)]
        self.esta_ativo = False

        self.criar_interface()
        
    def criar_interface(self):
        self.label = tk.Label(self.root, text="👀")
        self.label.pack()

        self.button = tk.Button(self.root, text="Start")
        self.button.pack()

        self.button.configure(command=self.alternar_estado)

    def alternar_estado(self):
        self.esta_ativo = not self.esta_ativo
        if self.esta_ativo:
            self.button.config(text="Stop", bg="red")
            thread = threading.Thread(target=self.executar)
            thread.daemon = True
            thread.start()
        else:
            self.button.config(text="Start", bg="SystemButtonFace")

    def executar(self):
        while self.esta_ativo:
            time.sleep(randrange(10))
            tecla = self.alfabeto[randrange(len(self.alfabeto))]
            pyautogui.press(tecla)

    def iniciar(self):
        self.root.mainloop() 