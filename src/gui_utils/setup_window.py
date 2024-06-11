import tkinter as tk
from tkinter import ttk
from src.key_capture_entry import KeyCaptureEntry
from tkinter import messagebox

class SetupWindow:
    def __init__(self, root, running_window):
        self.root = root
        self.running_window = running_window
        self.setup_frame = ttk.Frame(self.root, padding="20")
        self.setup_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        style = ttk.Style()
        style.configure("TButton", font=("Segoe UI", 12), padding=10)
        style.configure("TLabel", font=("Segoe UI", 12))
        style.configure("TEntry", font=("Segoe UI", 12))

        ttk.Label(self.setup_frame, text="Program:", font=("Segoe UI", 14)).grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        self.entry_program = ttk.Entry(self.setup_frame, font=("Segoe UI", 12))
        self.entry_program.grid(row=0, column=1, padx=10, pady=5, sticky=tk.EW)

        ttk.Label(self.setup_frame, text="Mute Key:", font=("Segoe UI", 14)).grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        self.mute_key_entry = KeyCaptureEntry(self.setup_frame, font=("Segoe UI", 12))
        self.mute_key_entry.grid(row=1, column=1, padx=10, pady=5, sticky=tk.EW)

        ttk.Label(self.setup_frame, text="Unmute Key:", font=("Segoe UI", 14)).grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        self.unmute_key_entry = KeyCaptureEntry(self.setup_frame, font=("Segoe UI", 12))
        self.unmute_key_entry.grid(row=2, column=1, padx=10, pady=5, sticky=tk.EW)

        self.start_button = ttk.Button(self.setup_frame, text="Start", command=self.start_program)
        self.start_button.grid(row=3, columnspan=2, pady=20, sticky=tk.EW)

        for child in self.setup_frame.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def start_program(self):
        program = self.entry_program.get()
        mute_key = self.mute_key_entry.get()
        unmute_key = self.unmute_key_entry.get()
        
        if not program or not mute_key or not unmute_key:
            messagebox.showerror("Error", "All fields are required!")
            return
        
        self.setup_frame.pack_forget()
        self.running_window.start_program(program, mute_key, unmute_key)
