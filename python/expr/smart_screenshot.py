import win32gui
import win32con
import win32api
import time
import threading
import tkinter as tk
from PIL import ImageGrab

class Overlay:
    def __init__(self):
        self.root = tk.Tk()
        self.root.attributes('-topmost', True)
        self.root.attributes('-alpha', 0.3)
        self.root.overrideredirect(True)
        self.root.configure(bg='red')
        self.label = tk.Label(self.root, text="", bg="red")
        self.label.pack()

    def move_and_resize(self, x, y, w, h):
        self.root.geometry(f"{w}x{h}+{x}+{y}")
        self.root.update()

    def show(self):
        self.root.deiconify()

    def hide(self):
        self.root.withdraw()

    def loop(self):
        self.root.mainloop()

def track_window_rect(overlay):
    overlay.show()
    try:
        while True:
            x, y = win32gui.GetCursorPos()
            hwnd = win32gui.WindowFromPoint((x, y))
            if hwnd:
                rect = win32gui.GetWindowRect(hwnd)
                l, t, r, b = rect
                w, h = r - l, b - t
                overlay.move_and_resize(l, t, w, h)
            time.sleep(0.05)
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    overlay = Overlay()
    threading.Thread(target=track_window_rect, args=(overlay,), daemon=True).start()
    overlay.loop()
