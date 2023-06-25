import json
import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import *
import os

from BaseFrame import BaseFrame
from Util import *
from utils_theme import Theme
from CodeMgr import *

TEMP_FONT = 'Arial 12'
CODE_FONT = 'Arial 15'


class TemplateFrame(BaseFrame):

    def __init__(self, name: str, master=None, **kw) -> None:
        super().__init__(master=master, **kw)

        self.name = name
        self.getTemplate()

        self.initArgsView()
        self.initCodeView()

    def initArgsView(self):
        top = ttk.Frame(self.top)
        top.pack(side=tk.TOP, anchor=tk.W, fill=tk.X, expand=True)

        ttk.Label(top, text=self.name, font='Arial 20').pack(
            side=tk.LEFT, pady=5, padx=10)

        ttk.Button(top, text='preview', command=self.preview).pack(
            side=tk.LEFT, pady=5, padx=(0, 10))

        ttk.Button(top, text='generate', command=self.generate).pack(
            side=tk.LEFT, pady=5, padx=(0, 10))

        ttk.Button(top, text='reload', command=self.reload).pack(
            side=tk.LEFT, pady=5, padx=(0, 10))

        top = ttk.Frame(self.top)
        top.pack(side=tk.TOP, anchor=tk.W)

        for k in self.args:
            f = ttk.Frame(top)
            f.pack(side=tk.TOP, anchor=tk.W)

            ttk.Label(f, text=k, font=("Calibri", 15, 'bold')
                      ).pack(side=tk.LEFT, padx=5)
            ttk.Entry(f, textvariable=self.args[k]).pack(side=tk.LEFT, padx=5)

    def initCodeView(self):

        mid = self.mid

        h = 20

        f1 = ttk.LabelFrame(mid, text='Template')
        f1.grid(column=0, row=0, sticky=tk.NW)

        t1 = self.tempText = ScrolledText(
            f1, height=h, bg=Theme.MainBg, fg=Theme.MainFg, font=TEMP_FONT, width=30)
        t1.pack()
        t1.insert(tk.END, getPatt(self.template))

        f2 = ttk.LabelFrame(mid, text='Code')
        f2.grid(column=1, row=0, sticky=tk.NW)

        t2 = self.codeText = ScrolledText(
            f2, height=h, bg=Theme.MainBg, fg=Theme.MainFg, font=CODE_FONT)
        t2.grid(column=1, row=0, sticky=tk.NW)

    def preview(self):
        self.codeText.delete('1.0', tk.END)

        tempBuilt = build(
            self.template, {x: self.args[x].get() for x in self.args})

        if tempBuilt is None:
            return

        if tempBuilt['type'] == TemplateType.Create.value:
            self.codeText.insert(tk.END, getPatt(tempBuilt))
        elif tempBuilt['type'] == TemplateType.Modify.value:
            self.tempText.delete('1.0', tk.END)
            self.tempText.insert(tk.END, getPatt(tempBuilt))

    def getTemplate(self):
        temp = self.template = getTemplate(self.name)
        self.args = {x: tk.StringVar(value='') for x in temp['args']}

    def reload(self):
        clearFrame(self.top)
        clearFrame(self.mid)
        clearFrame(self.bottom)

        self.getTemplate()
        self.initArgsView()
        self.initCodeView()

    def generate(self):
        pass


def getFrame(name: str, master) -> TemplateFrame:
    return TemplateFrame(name, master)
