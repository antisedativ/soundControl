import sys
import os

# Добавляем путь к корневой директории проекта в sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from gui import start_gui

if __name__ == "__main__":
    start_gui()
