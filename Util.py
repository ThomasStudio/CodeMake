from tkinter.ttk import Frame

def toast(s: str):
    print(s)

def log(s:str):
    print(s)

def clearFrame(f:Frame):
    for x in f.winfo_children():
        x.destroy()        