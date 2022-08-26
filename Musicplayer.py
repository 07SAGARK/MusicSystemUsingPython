#from importlib import import_module
#from tracemalloc import stop
import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os
#from tkinter.ttk import Button
#from tkinter import Tk,mainloop,TOP

musicplayer=tkr.Tk() # it creates an instance of tkinter frame, helps to display the root windo
musicplayer.title("Music Player")
musicplayer.geometry('450x500') # to set the initial size of the window

directory=askdirectory()
os.chdir(directory) # chdir is used to change the current working directory, it takes single argument as new directory path
songlist=os.listdir()  # listdir returns the list containing the names of the entries in the directorygiven by path
playlist=tkr.Listbox(musicplayer,font="Helvetica 12 bold",bg="cyan",selectmode=tkr.SINGLE)
 # listbox is used to display the list to the user we can place only text items in the listbox and all text items contain the same font and color
for item in songlist:
    pos=0
    playlist.insert(pos,item)
    pos=pos+1

pygame.init()
pygame.mixer.init()

def play():
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
    var.set(playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()

def ExitMusicPlayer() :
    pygame.mixer.music.stop()

def pause():
    pygame.mixer.music.pause()

def unpause():
    pygame.mixer.music.unpause()

Button1=tkr.Button(musicplayer,width=5,height=3 ,font="helvetivca 12 bold" , text="PLAY",command=play , bg="green", fg="white") 
Button2=tkr.Button(musicplayer,width=5,height=3 ,font="helvetivca 12 bold" , text="STOP",command=ExitMusicPlayer , bg="red", fg="white") 
Button3=tkr.Button(musicplayer,width=5,height=3 ,font="helvetivca 12 bold" , text="Pause",command=pause , bg="orange", fg="white") 
Button4=tkr.Button(musicplayer,width=5,height=3 ,font="helvetivca 12 bold" , text="Unpause",command=unpause , bg="purple", fg="white") 


var=tkr.StringVar()
songtitle=tkr.Label(musicplayer,font="Helvetica 12 bold",textvariable=var)

songtitle.pack()
Button1.pack(fill="x")
Button2.pack(fill="x")
Button3.pack(fill="x")
Button4.pack(fill="x")
playlist.pack(fill="both",expand="yes")

musicplayer.mainloop()