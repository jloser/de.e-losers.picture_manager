#!/usr/bin/python3.5

import pictureselect as ps
import tkinter as tk

def show_dialog(in_root):
   app = ps.PictureSelect(master=in_root)
   app.master.title("Picture Select")
   app.master.minsize(width=720, height=580)
   app.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    show_dialog(root)

