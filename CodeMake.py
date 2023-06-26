import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
import os
import sys

from BaseFrame import BaseFrame
from CodeMgr import *
from TemplateFrame import TemplateFrame, getFrame

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_PATH = ROOT_PATH + '/templates'
sys.path.append(TEMPLATE_PATH)

CODE = 'code '


class CodeMake(BaseFrame):
    def __init__(self, master=None, **kw) -> None:
        super().__init__(master=master, **kw)

    def afterInit(self):
        super().afterInit()

        f = self.top

        ttk.Label(f, text='Template ').pack(side=tk.LEFT)

        cb = self.tList = ttk.Combobox(
            f, values=self.getTemplates(), state='readonly', width=30, font='宋体 15')
        cb.current(0)
        cb.pack(side=tk.LEFT, fill=tk.Y)

        ttk.Button(f, text='show', command=self.show).pack(
            side=tk.LEFT, padx=5)

        ttk.Button(f, text='edit', command=self.edit).pack(
            side=tk.LEFT, padx=(25, 5))

        ttk.Button(f, text='clear', command=self.clear).pack(
            side=tk.LEFT, padx=5)

        ttk.Button(f, text='reload', command=self.reloadTemplates).pack(
            side=tk.LEFT, padx=5)

    def getTemplates(self):
        return [x for x in os.listdir(TEMPLATE_PATH) if x.endswith('.py')]

    def reloadTemplates(self):
        cb = self.tList
        cb.config(state='normal')
        cb.delete(0, len(cb.get()))

        cb['value'] = self.getTemplates()
        cb.config(state='readonly')

    def show(self):
        cb = self.tList

        if len(cb.get()) == 0:
            return

        temp = getTemplate(cb.get())

        if temp is None:
            toast(f'{cb.get()} is not valid template')
            return

        self.showTemplate(cb.get())

    def showTemplate(self, name: str):
        f = self.mid

        ft = getFrame(name, f)
        ft.pack(side=tk.TOP, anchor=tk.W)

    def clear(self):
        clearFrame(self.mid)

    def edit(self):
        cmd = f'{CODE} {TEMPLATE_PATH}/{self.tList.get()}'
        os.popen(cmd)
