
from tkinter import *
from operandes import *

tk = Tk()
canvas = Canvas(tk, width=200, height=96)
canvas.pack()
ln1 = []
ln2 = []
in1 = 0
in2 = 0
test = False
operande = ""

def input_number(n):
    global in1,in2,ln1,ln2,operande,test,eq


    if n == "=":
        test = False
        ln1,ln2 = [],[]

        if operande == "+":
            return print(add(in1,in2))
        elif operande == "-":
            return print(subb(in1,in2)) 
        elif operande == "*":
            return print(multiply(in1,in2)) 
        elif operande == "/":
            return print(div(in1,in2)) 
        elif operande == "^":
            return print(exposant(in1,in2)) 
        else:
            return "vous avez oublié une opérande"

    if n == "+" or n == "*" or n == "-" or n == "/" or n == "^" :
        test = True
        operande = n
        n=0

    n=int(n)

    if test == True:
        ln2.append(n)
        in2 = conv_list_to_int(ln2)
    else:
        ln1.append(n)
        in1 = conv_list_to_int(ln1)

    


def supprimer():
    if test == False:
        del ln1[len(ln1)-1]
        in1 = conv_list_to_int(ln1)
    else: 
        del ln2[len(ln2)-1]
        in2 = conv_list_to_int(ln2)




B0 = Button(tk, text = "0", command = lambda : input_number("0"))
B1 = Button(tk, text = "1", command = lambda : input_number("1"))
B2 = Button(tk, text = "2", command = lambda : input_number("2"))
B3 = Button(tk, text = "3", command = lambda : input_number("3"))
B4 = Button(tk, text = "4", command = lambda : input_number("4"))
B5 = Button(tk, text = "5", command = lambda : input_number("5"))
B6 = Button(tk, text = "6", command = lambda : input_number("6"))
B7 = Button(tk, text = "7", command = lambda : input_number("7"))
B8 = Button(tk, text = "8", command = lambda : input_number("8"))
B9 = Button(tk, text = "9", command = lambda : input_number("9"))
BAD = Button(tk, text = "+", command = lambda : input_number("+"))
BMU = Button(tk, text = "*", command = lambda : input_number("*"))
BSU = Button(tk, text = "-", command = lambda : input_number("-"))
BDI = Button(tk, text = "/", command = lambda : input_number("/"))
BEQ = Button(tk, text = "=", command = lambda : input_number("="))
BEX = Button(tk, text = "^", command = lambda : input_number("^"))
#BDEL = Button(tk, text = "Supprimmer", command = supprimer)

BEQ.place(x = 51,y = 75)
B0.place(x = 34,y = 75)
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
#BDEL.place(x = 68, y=50)

tk.mainloop()
