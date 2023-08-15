import webbrowser
import time
import tkinter
import tkinter_page
from tkinter import *

window = Tk()
window.title("")


url1 = input("web site url: " )
def olv():
    
    while True:

        webbrowser.open_new_tab(url1)

        time.sleep(2)

verb = Entry(window)
verb.pack()

butt = Button(window, text = "OLV", command = OLV)
butt.pack()

jav = []
for x in range(6):
    jav.append(Label(window))

window.mainloop()
