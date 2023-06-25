import tkinter as tk
from tkinter.ttk import *

from Util import *

class BaseFrame(Frame):
    def __init__(self, master=None, **kw) -> None:
        super().__init__(master=master, **kw)

        self.init()
        self.initUi()
        self.afterInit()

    def init(self):
        pass

    def afterInit(self):
        pass

    def initUi(self):
        self.initTop()
        self.initMid()
        self.initBottom()

    def initTop(self):
        f = self.top = Frame(self)
        f.pack(side=tk.TOP, fill=tk.X, anchor=tk.W)

    def initMid(self):
        f = self.mid = Frame(self)
        f.pack(side=tk.TOP, fill=tk.X, anchor=tk.W)

    def initBottom(self):
        f = self.bottom = Frame(self)
        f.pack(side=tk.TOP, fill=tk.X, anchor=tk.W)