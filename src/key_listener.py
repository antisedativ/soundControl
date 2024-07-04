from pynput import keyboard
from src.audio_controller import AudioController

class KeyListener:
    def __init__(self, target: str, mute_key, unmute_key, volume_up_key, volume_down_key):
        self.target = target
        self.key_actions = {
            mute_key: self.mute,
            unmute_key: self.unmute,
            volume_up_key: self.volume_up,
            volume_down_key: self.volume_down
        }
        self.audio_ctrl = AudioController(target)
        self.listener = keyboard.Listener(on_press=self.on_press)
        self.listener.start()

    def on_press(self, key):
        try:
            key_name = key.char if hasattr(key, 'char') else key.name
            if key_name in self.key_actions:
                self.key_actions[key_name]()
        except AttributeError:
            pass

    def mute(self):
        self.audio_ctrl.mute()

    def unmute(self):
        self.audio_ctrl.unmute()

    def volume_up(self):
        self.audio_ctrl.increase_volume()  

    def volume_down(self):
        self.audio_ctrl.decrease_volume()  

    def stop(self):
        self.listener.stop()
