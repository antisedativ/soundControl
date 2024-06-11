from pynput import keyboard
from src.audio_controller import AudioController

class KeyListener:
    def __init__(self, target: str, mute_key, unmute_key):
        self.target = target
        self.key_actions = {mute_key: True, unmute_key: False}
        self.audio_ctrl = AudioController(target)
        self.listener = keyboard.Listener(on_press=self.on_press)
        self.listener.start()

    def on_press(self, key):
        try:
            key_name = key.char if hasattr(key, 'char') else key.name
            if key_name in self.key_actions:
                self.mute_program(self.key_actions[key_name])
        except AttributeError:
            pass

    def mute_program(self, mute: bool):
        if mute:
            self.audio_ctrl.mute()
        else:
            self.audio_ctrl.unmute()

    def stop(self):
        self.listener.stop()
