from pynput import keyboard
from audio_controller import AudioController

def start_listener(target: str, mute_key, unmute_key):
    KEY_ACTIONS = {mute_key: True, unmute_key: False}

    def mute_program(target: str, mute: bool):
        audio_ctrl = AudioController(target)
        audio_ctrl.mute() if mute else audio_ctrl.unmute()

    def on_press(key):
        try:
            key_name = key.char if hasattr(key, 'char') else key.name
            if key_name in KEY_ACTIONS:
                mute_program(target, KEY_ACTIONS[key_name])
        except AttributeError:
            pass

    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    # Возвращаем слушателя, чтобы можно было его остановить
    return listener
