import fshelpers as fs
import tkinter as tk
# import the filedialog - for P3 import only filedialog
from tkinter import filedialog
import sys
import workerclass as w

class GuiClass(tk.Frame):
    
    def __init__(self, master=None):
        super().__init__(master)
        self.pack(expand=1, fill="both")
        self.create_frames()
        self.create_widgets()

    def create_frames(self):
        # create top left frame
        self.f_top = tk.Frame(self)
        self.f_top["height"] = 2
        self.f_top["borderwidth"] = 2
        self.f_top["relief"] = "sunken"
        # create middle frame
        self.f_middle = tk.Frame(self)
        self.f_middle["height"] = 2
        self.f_middle["borderwidth"] = 2
        self.f_middle["relief"] = "sunken"
        # create lower_left frame
        self.f_lleft = tk.Frame(self)
        self.f_lleft["height"] = 2
        self.f_lleft["borderwidth"] = 2
        # create lower_middle frame
        self.f_lmiddle = tk.Frame(self)
        self.f_lmiddle["height"] = 2
        self.f_lmiddle["borderwidth"] = 2
        # create lower_right frame
        self.f_lright = tk.Frame(self)
        self.f_lright["height"] = 2
        self.f_lright["borderwidth"] = 2
        # pack the frame - fill x = fill horizontally
        self.f_top.pack(side="top", fill="x", padx=5, pady=5)
        self.f_middle.pack(expand=1, fill="both", padx=5, pady=5)
        self.f_lleft.pack(side="left", padx=5, pady=5)
        self.f_lmiddle.pack(side="left", fill="x", expand=1, padx=5, pady=5)
        self.f_lright.pack(side="right", padx=5, pady=5)

        
    def create_widgets(self):
        # create a string variable to store changing directories
        self.wd_string = tk.StringVar()
        # create the label for the text 
        self.l_dir = tk.Label(self.f_top)
        self.l_dir["text"] = "Working Directory:"
        self.l_dir.pack(side="left")
        # create the label that contains the working dir
        self.l_current_dir = tk.Label(self.f_top)
        self.wd_string.set(fs.get_last_dir())
        self.l_current_dir["textvariable"] = self.wd_string
        self.l_current_dir.pack(side="left")
        # create the label as container for the image
        self.pic = tk.Label(self.f_middle)
        self.pic["text"] = "This is the picture"
        self.pic.pack()
        # create the Quit Button
        self.quit = tk.Button(self.f_lleft)
        self.quit["text"] = "Quit"
        self.quit["command"] = self.close_win
        self.quit.pack(side="left")
        # create the GO Button
        self.go = tk.Button(self.f_lmiddle)
        self.go["text"] = "Go Kahuna!"
        self.go["command"] = self.gok
        self.go.pack(side="bottom")
        # create the select button
        self.open = tk.Button(self.f_lright)
        self.open["text"] = "Select Dir"
        self.open["command"] = self.open_dir_selector
        self.open.pack(side="left")
        
    def gok(self):
        # create a new worker
        selected_dir = fs.get_last_dir()
        worker = w.WorkerClass(self, selected_dir)
        worker.filewalker()
        
    def close_win(self):
        self.master.destroy()

    def open_dir_selector(self):

        # fill options with the last selected directory
        options = {"initialdir": fs.get_last_dir()}
        # open a filedialog
        selected_dir = filedialog.askdirectory(**options)
        # change the string variable for the label
        self.wd_string.set(selected_dir)
        fs.put_last_dir(selected_dir)

