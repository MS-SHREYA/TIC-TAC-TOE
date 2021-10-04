
from tkinter import *
import tkinter.messagebox as msg

rose = Tk()
rose.title("TIC-TAC-TOE")
Label(rose,text = "Player 1 : X", font = 'calibri 16'). grid(row = 0, column = 1)
Label(rose,text = "Player 2 : O", font = 'calibri 16'). grid(row = 0, column = 2)

button_1 = Button(rose,width = 16, height = 8, font = "calibri 16")
button_1.grid(row = 1, column = 1)
button_2 = Button(rose,width = 16, height = 8, font = "calibri 16")
button_2.grid(row = 1, column = 2)
button_3 = Button(rose,width = 16, height = 8, font = "calibri 16")
button_3.grid(row = 1, column = 3)
button_4 = Button(rose,width = 16, height = 8, font = "calibri 16")
button_4.grid(row = 2, column = 1)
button_5 = Button(rose,width = 16, height = 8, font = "calibri 16")
button_5.grid(row = 2, column = 2)
button_6 = Button(rose,width = 16, height = 8, font = "calibri 16")
button_6.grid(row = 2, column = 3)
button_7 = Button(rose,width = 16, height = 8, font = "calibri 16")
button_7.grid(row = 3, column = 1)
button_8 = Button(rose,width = 16, height = 8, font = "calibri 16")
button_8.grid(row = 3, column = 2)
button_9 = Button(rose,width = 16, height = 8, font = "calibri 16")
button_9.grid(row = 3, column = 3)
rose.mainloop() # tells the events (above) to run

digits = [1,2,3,4,5,6,7,8,9] 
mark = '' # will be used to play the X and O
count = 0 # counting the number of clicks
panels = ['panel'] * 10
