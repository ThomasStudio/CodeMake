from CodeMake import CodeMake
import tkinter as tk
from utils_theme import Theme

if __name__ == '__main__':
    root = tk.Tk()
    f = CodeMake(master=root)
    f.pack(side=tk.TOP, fill=tk.BOTH, expand=True,)

    Theme.InitTheme(root)

    root.mainloop()
