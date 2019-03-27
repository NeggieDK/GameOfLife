import tkinter as tk
import os
from tkinter import filedialog
from JsonParser import JsonParser

class FileHelper:

    @staticmethod
    def OpenFile():
        root = tk.Tk()
        root.withdraw()
        configPath = "config"
        path = os.path.join(os.path.dirname(__file__),configPath)
        return filedialog.askopenfilename(initialdir = path)

    @staticmethod
    def SaveFile(text):
        jsonText = JsonParser.CreateJson(text)
        root = tk.Tk()
        root.withdraw()  
        path = filedialog.asksaveasfile(mode='w',defaultextension=".txt")
        if(path != None):
            f = open(path.name, "w")
            f.write(jsonText)
        else:
            print("Not saved because no file was selected!")
         