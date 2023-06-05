from tkinter import *
from tkinter import ttk
import webbrowser
import texts

# CONSTANTS
GITHUB = "https://github.com/ExoticGamerrrYT"
YOUTUBE = "https://www.youtube.com/channel/UCujyuyr8XFabeb8JQyEJphA"

def open_github():
    webbrowser.open(GITHUB, 1)


def open_youtube():
    webbrowser.open(YOUTUBE, 1)

wn = Tk()
wn.wm_title(texts.title_txt)
wn.wm_geometry("600x400+640+230")
wn.wm_resizable(False, False)
wn.configure(bg="#141414")

# LABELS
title = ttk.Label(wn, text=texts.title_txt, background="#141414", foreground="white", font="Arial, 34")
title.place(relx=0.5, anchor=N)

# BUTTONS
youtube_btn = ttk.Button(wn, text=texts.youtube_txt, command=open_youtube)
youtube_btn.place(relx=0.5, rely=0.5, anchor=CENTER)

git_btn = ttk.Button(wn, text=texts.github_txt, command=open_github)
git_btn.place(relx=0.5, rely=0.57, anchor=CENTER)

wn.mainloop()
