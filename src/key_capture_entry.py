import tkinter as tk
from tkinter import ttk
from pynput import keyboard

class KeyCaptureEntry(ttk.Entry):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self._listener = None
        self.bind("<FocusIn>", self.start_capture)
        self.bind("<FocusOut>", self.stop_capture)

    def start_capture(self, event=None):
        if not self._listener:
            self._listener = keyboard.Listener(on_press=self.on_key_press)
            self._listener.start()

    def stop_capture(self, event=None):
        if self._listener:
            self._listener.stop()
            self._listener = None

    def on_key_press(self, key):
        try:
            key_name = key.char if hasattr(key, 'char') else key.name
            self.delete(0, tk.END)
            self.insert(0, key_name)
        except AttributeError:
            pass
