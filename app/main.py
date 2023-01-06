from tkinter import *
from tkinter import ttk
from tkinter.font import Font, nametofont
import webbrowser

def youtube():
    webbrowser.open("https://www.youtube.com/channel/UCufGbkcf8fxYGFtjalCkyAg")
def git():
    webbrowser.open("https://github.com/ExoticGamerrrYT")

wn = Tk()
wn.title("Exotic GUI")
wn.geometry("600x400+750+200")
wn.resizable(False, False)
wn.config(bg="#EEEEEE")
frm = ttk.Frame(wn, padding=10).grid()

yt_link = ttk.Label(wn, text="My YouTube channel", foreground="blue", background=None, cursor="hand2")
yt_link.bind("<Button-1>", lambda e: youtube())
yt_link.pack()

git_link = ttk.Label(wn, text="My GitHub", foreground="blue", background=None, cursor="hand2")
git_link.bind("<Button-1>", lambda e: git())
git_link.pack()


wn.mainloop()