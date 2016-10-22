#!/usr/bin/python3.5

import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import configparser
import sys, os

class PictureSelect(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):

        # create the select button
        self.open = tk.Button(self)
        self.open["text"] = "Select Dir"
        self.open["command"] = self.open_dir_selector
        self.open.pack(side = "top")
        self.open.pack(expand=1)
        
        # create the Quit Button
        self.quit = tk.Button(self, text="Quit", command = root.destroy)
        self.quit.pack(side = "bottom")
        self.quit.pack(expand=1)
    
        # create the label as container for the imagte
        self.label = tk.Label(image=photo)
        self.label.pack(side = "bottom")
        
    def open_dir_selector(self):
        options = {"initialdir": get_last_dir()}
        selected_dir = filedialog.askdirectory(**options)
        put_last_dir(selected_dir)
        filewalker(selected_dir)

def put_last_dir(in_dir):
    config = configparser.ConfigParser()
    config["DEFAULT"] = {"lastdir": in_dir}
    with open('.config', 'w') as config_file:
        config.write(config_file)


def get_last_dir():
    config = configparser.ConfigParser()
    lastdir =""
    try:
        config.read(".config")  
        return config["DEFAULT"]["lastdir"]
    except:
        print("Error: ", sys.exc_info()[0])
        return lastdir

def filewalker(in_dir):
    for dir_name, subdirs, filelist in os.walk(in_dir):
        print("In directory: %s", dir_name)
        for fname in filelist:
            try: 
                fname = dir_name + "/" + fname
                im = Image.open(fname)
                photo = ImageTk.PhotoImage(im)
                input("weiter?")
                print("size:", im.size)
            except IOError:
                print("\t", fname, "is not an image!")
        if len(subdirs) > 0:
            del subdirs[0]
    None

def show_dialog(in_root):
   app = PictureSelect(master = in_root)
   app.master.title("Picture Select")
   app.master.minsize(width=30, height=200)
   app.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    show_dialog(root)

