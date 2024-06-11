from pynput import keyboard
from src.audio_controller import AudioController


def start(target: str):
    KEY_ACTIONS = {keyboard.Key.alt_gr: True, keyboard.Key.ctrl_r: False}
    
    def mute_program(target: str, mute: bool):
        audio_ctrl = AudioController(target)
        audio_ctrl.mute() if mute else audio_ctrl.unmute()

    def on_press(key):
        if key in KEY_ACTIONS:
            mute_program(target, KEY_ACTIONS[key])

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
