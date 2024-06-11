import tkinter as tk
from src.gui_utils.setup_window import SetupWindow
from src.gui_utils.running_window import RunningWindow
from src.gui_utils.constants import SIZE, TITLE

def start_gui():
    root = tk.Tk()
    root.title(TITLE)
    root.geometry(SIZE)

    setup_window = SetupWindow(root, None)
    running_window = RunningWindow(root, setup_window.setup_frame)
    setup_window.running_window = running_window
    
    root.mainloop()
