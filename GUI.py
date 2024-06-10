from tkinter import *
from PIL import Image,ImageTk,ImageSequence
import pygame
from pygame import mixer
import os
import time
mixer.init()

root=Tk()
root.geometry("1000x500")

def play_gif():
    root.lift()
    root.attributes("-topmost",True)
    global image_names
    image_names=Image.open("images\loading.gif")
    lbl= Label(root)
    lbl.place(x=0,y=0)
    i=0
    for image_names in ImageSequence.Iterator(image_names):
        image_names=image_names.resize((1000,500))
        image_names = ImageTk.PhotoImage(image_names)
        lbl.config(image=image_names)
        time.sleep(0.05)
    root.destroy()

play_gif()
root.mainloop()