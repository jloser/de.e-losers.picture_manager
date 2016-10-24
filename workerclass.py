import configparser
from PIL import Image
import sys, os

class WorkerClass():

    def __init__(self, in_frame, in_startdir):
        self.mf = in_frame
        self.sd = in_startdir
    
    def filewalker(self):
        for dir_name, subdirs, filelist in os.walk(self.sd):
            print("In directory: %s", dir_name)
            for fname in filelist:
                try: 
                    fname = dir_name + "/" + fname
                    im = Image.open(fname)
                    input("weiter?")
                    print("size:", im.size)
                    self.mf.wd_string.set(fname)
                except IOError:
                    print("\t", fname, "is not an image!")
            if len(subdirs) > 0:
                del subdirs[0]
