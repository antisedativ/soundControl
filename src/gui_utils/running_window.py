import tkinter as tk
from tkinter import ttk
from src.key_listener import KeyListener
from gui_utils.constants import *

class RunningWindow:
    def __init__(self, root, setup_frame):
        self.root = root
        self.setup_frame = setup_frame

        self.running_frame = ttk.Frame(self.root, padding=PADDING_LARGE, style="Dark.TFrame")

        style = ttk.Style()
        style.configure("Dark.TFrame", background=BG_COLOR)
        style.configure("Treeview.Treeview", rowheight=30)
        style.configure(BUTTON_STYLE, font=(FONT_FAMILY, FONT_SIZE), padding=PADDING_LARGE)
        style.configure(LABEL_STYLE, font=(FONT_FAMILY, FONT_SIZE))

        style.configure("Treeview.Heading", font=(FONT_FAMILY, FONT_SIZE), padding=PADDING_MEDIUM)
        style.configure("Treeview", font=(FONT_FAMILY, FONT_SIZE), padding=PADDING_MEDIUM)

        self.label_status = ttk.Label(self.running_frame, text=RUNNING_TEXT, font=(FONT_FAMILY, FONT_SIZE + 2))
        self.label_status.pack(padx=PADDING_MEDIUM, pady=PADDING_MEDIUM)

        self.tree = ttk.Treeview(self.running_frame, columns=("Parameter", "Value"), show="headings", height=3, style="Treeview.Treeview")
        self.tree.heading("Parameter", text="Parameter")
        self.tree.heading("Value", text="Value")
        self.tree.pack(padx=PADDING_SMALL, pady=PADDING_SMALL)

        self.stop_button = ttk.Button(self.running_frame, text="Stop", command=self.stop_program)
        self.stop_button.pack(pady=PADDING_MEDIUM, anchor=tk.CENTER)

        self.listener = None


    def start_program(self, program, mute_key, unmute_key):
        self.tree.insert("", "end", values=("Program", program))
        self.tree.insert("", "end", values=("Mute Key", mute_key))
        self.tree.insert("", "end", values=("Unmute Key", unmute_key))
        self.running_frame.pack(padx=PADDING_SMALL, pady=PADDING_SMALL, fill=tk.BOTH, expand=True)
        self.listener = KeyListener(program, mute_key, unmute_key)


    def stop_program(self):
        if self.listener:
            self.listener.stop()
            self.listener = None
        
        self.running_frame.pack_forget()
        self.setup_frame.pack(padx=PADDING_MEDIUM, pady=PADDING_MEDIUM, fill=tk.BOTH, expand=True)
