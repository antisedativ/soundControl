import tkinter as tk
from tkinter import ttk
from gui_utils.setup_window import SetupWindow
from gui_utils.running_window import RunningWindow
from gui_utils.constants import SIZE, TITLE

def start_gui():
    root = tk.Tk()
    root.title(TITLE)
    root.geometry(SIZE)

    setup_window = SetupWindow(root, None)
    running_window = RunningWindow(root, setup_window.setup_frame)
    setup_window.running_window = running_window
    
    root.mainloop()
