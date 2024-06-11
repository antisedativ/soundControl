import tkinter as tk
from tkinter import ttk
from src.key_listener import start_listener
from src.audio_controller import AudioController

class RunningWindow:
    def __init__(self, root, setup_frame):
        self.root = root
        self.setup_frame = setup_frame

        self.running_frame = ttk.Frame(self.root, padding="20")

        style = ttk.Style()
        style.configure("TButton", font=("Segoe UI", 12), padding=10)
        style.configure("TLabel", font=("Segoe UI", 12))

        self.label_status = ttk.Label(self.running_frame, text="Running...", font=("Segoe UI", 14))
        self.label_status.pack(padx=10, pady=10)

        self.label_info = ttk.Label(self.running_frame, text="", font=("Segoe UI", 12))
        self.label_info.pack(padx=10, pady=10)

        self.stop_button = ttk.Button(self.running_frame, text="Stop", command=self.stop_program)
        self.stop_button.pack(pady=20)

        self.listener = None

    def start_program(self, program, mute_key, unmute_key):
        self.running_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        self.label_info.config(text=f"Program: {program}\nMute Key: {mute_key}\nUnmute Key: {unmute_key}")

        self.listener = start_listener(program, mute_key, unmute_key)

    def stop_program(self):
        if self.listener:
            self.listener.stop()
            self.listener = None
        
        self.running_frame.pack_forget()
        self.setup_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
