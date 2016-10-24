import configparser
import sys, os

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
