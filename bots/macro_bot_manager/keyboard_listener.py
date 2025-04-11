import time
import keyboard
import threading

running = False 
listener_thread = None
shortcuts = {}

def on_key_event(event):
    
    if event.name in shortcuts:
        keyboard.press_and_release('backspace')
        text = shortcuts[event.name]
        if "\n" in text:
            escrever_mensagem(text)
        else:
            keyboard.write(shortcuts[event.name])

def escrever_mensagem(text):
    
    for linha in text.split("\n"):
        keyboard.write(linha)
        keyboard.press_and_release("shift+enter")
        time.sleep(0.1)

def load_shortcuts():
    
    global shortcuts
    from . import database
    shortcuts = {key: text for key, text in database.get_shortcuts()}

def start_keyboard_listener():
    
    global running, listener_thread
    if running:
        return

    running = True
    load_shortcuts()
    listener_thread = threading.Thread(target=run_keyboard_listener, daemon=True)
    listener_thread.start()

def run_keyboard_listener():
    
    keyboard.on_press(on_key_event)
    while running:
        keyboard.wait()

def stop_keyboard_listener():
    
    global running
    running = False
    keyboard.unhook_all()