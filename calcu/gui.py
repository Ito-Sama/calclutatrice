
from tkinter import *
from tkinter import messagebox

tk = Tk()
canvas = Canvas(tk, width=200, height=96)
canvas.pack()

def input_number0():
    return True
def input_number1():
    return True
def input_number2():
    return True
def input_number3():
    return True
def input_number4():
    return True
def input_number5():
    return True
def input_number6():
    return True
def input_number7():
    return True
def input_number8():
    return True
def input_number9():
    return True
def input_number_ad():
    return True
def input_number_mu():
    return True
def input_number_di():
    return True
def input_number_su():
    return True
def input_number_exp():
    return True
def input_number_eq():
    return True


B0 = Button(tk, text = "0", command = input_number0)
B1 = Button(tk, text = "1", command = input_number1)
B2 = Button(tk, text = "2", command = input_number2)
B3 = Button(tk, text = "3", command = input_number3)
B4 = Button(tk, text = "4", command = input_number4)
B5 = Button(tk, text = "5", command = input_number5)
B6 = Button(tk, text = "6", command = input_number6)
B7 = Button(tk, text = "7", command = input_number7)
B8 = Button(tk, text = "8", command = input_number8)
B9 = Button(tk, text = "9", command = input_number9)
BAD = Button(tk, text = "+", command = input_number_ad)
BMU = Button(tk, text = "*", command = input_number_mu)
BSU = Button(tk, text = "-", command = input_number_su)
BDI = Button(tk, text = "/", command = input_number_di)
BEQ = Button(tk, text = "=", command = input_number_exp)
BEX = Button(tk, text = "puis", command = input_number_eq)

BEQ.place(x = 68,y = 75)
B0.place(x = 51,y = 75)
B1.place(x = 17,y = 50)
B2.place(x = 34,y = 50)
B3.place(x = 51,y = 50)
B4.place(x = 17,y = 25)
B5.place(x = 34,y = 25)
B6.place(x = 51,y = 25)
B7.place(x = 17,y = 0)
B8.place(x = 34,y = 0)
B9.place(x = 51,y = 0)
BAD.place(x = 0,y = 0)
BSU.place(x = 0,y = 25)
BMU.place(x = 0,y = 50)
BDI.place(x = 0,y = 75)
BEX.place(x = 17,y = 75)


tk.mainloop()
