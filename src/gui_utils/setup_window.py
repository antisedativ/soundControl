import tkinter as tk
from tkinter import ttk
from src.key_capture_entry import KeyCaptureEntry
from src.audio_controller import AudioController
from tkinter import messagebox
from gui_utils.constants import *

class SetupWindow:
    def __init__(self, root, running_window):
        self.root = root
        self.sessions = AudioController().get_sessions()
        self.running_window = running_window
        self.setup_frame = ttk.Frame(self.root, padding=PADDING_LARGE, style="Dark.TFrame")
        self.setup_frame.pack(padx=PADDING_MEDIUM, pady=PADDING_MEDIUM, fill=tk.BOTH, expand=True)
        self.setup_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.root.config(bg=BG_COLOR)

        style = ttk.Style()
        style.configure("Dark.TFrame", background=BG_COLOR)
        style.configure(BUTTON_STYLE, font=(FONT_FAMILY, FONT_SIZE), padding=PADDING_LARGE, background=BG_COLOR, foreground=BLACK_COLOR)
        style.configure(LABEL_STYLE, font=(FONT_FAMILY, FONT_SIZE), foreground=WHITE_COLOR, background=BG_COLOR)
        style.configure(ENTRY_STYLE, font=(FONT_FAMILY, FONT_SIZE), background=INPUT_BG_COLOR, foreground=BLACK_COLOR)

        ttk.Label(self.setup_frame, text="Program:", font=(FONT_FAMILY, FONT_SIZE + 2)).grid(row=0, column=0, padx=PADDING_MEDIUM, pady=PADDING_SMALL, sticky=tk.W)
        self.program_combo = ttk.Combobox(self.setup_frame, values=self.sessions, font=(FONT_FAMILY, FONT_SIZE))
        self.program_combo.grid(row=0, column=1, padx=PADDING_MEDIUM, pady=PADDING_SMALL, sticky=tk.EW)

        ttk.Label(self.setup_frame, text="Mute Key:", font=(FONT_FAMILY, FONT_SIZE + 2)).grid(row=1, column=0, padx=PADDING_MEDIUM, pady=PADDING_SMALL, sticky=tk.W)
        self.mute_key_entry = KeyCaptureEntry(self.setup_frame, font=(FONT_FAMILY, FONT_SIZE))
        self.mute_key_entry.grid(row=1, column=1, padx=PADDING_MEDIUM, pady=PADDING_SMALL, sticky=tk.EW)

        ttk.Label(self.setup_frame, text="Unmute Key:", font=(FONT_FAMILY, FONT_SIZE + 2)).grid(row=2, column=0, padx=PADDING_MEDIUM, pady=PADDING_SMALL, sticky=tk.W)
        self.unmute_key_entry = KeyCaptureEntry(self.setup_frame, font=(FONT_FAMILY, FONT_SIZE))
        self.unmute_key_entry.grid(row=2, column=1, padx=PADDING_MEDIUM, pady=PADDING_SMALL, sticky=tk.EW)

        self.start_button = ttk.Button(self.setup_frame, text="Start", command=self.start_program)
        self.start_button.grid(row=3, columnspan=2, pady=PADDING_LARGE, sticky=tk.EW)

        for child in self.setup_frame.winfo_children():
            child.grid_configure(padx=PADDING_SMALL, pady=PADDING_SMALL)

    def start_program(self):
        program = self.program_combo.get()
        mute_key = self.mute_key_entry.get()
        unmute_key = self.unmute_key_entry.get()
        
        if not program or not mute_key or not unmute_key:
            messagebox.showerror("Error", "All fields are required!")
            return
        
        self.setup_frame.pack_forget()
        self.running_window.start_program(program, mute_key, unmute_key)
