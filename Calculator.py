from tkinter import *

value=""

def inp(num):
    global value
    value=value+str(num)
    value1.set(value)
    
def FullClear():
    global value
    value=""
    value1.set(value)

def PressEqual():
    global value
    total=expresion_field.get()
    value=str(eval(total))
    value1.set(value)

def ClearEnd():
    global value
    value=value[:-1]
    value1.set(value)
    

if __name__=="__main__":

    win=Tk()

    win.geometry("245x170")

    win.title("Standard Calculator")

    value1=StringVar()
    
    expresion_field=Entry(win,textvariable=value1)
    expresion_field.grid(row=0,columnspan=4,ipadx=60)
    value1.set("Enter the expression")

    l=Label(text="WELCOME")
    l.grid(columnspan=4)

    mod=Button(text="CE",width=7,height=1,command= lambda: ClearEnd())
    mod.grid(row=2,column=0)

    div=Button(text="C",width=7,height=1,command= lambda: FullClear())
    div.grid(row=2,column=1)

    multi=Button(text="x",width=7,height=1,command= lambda: inp("*"))
    multi.grid(row=2,column=2)

    b1=Button(text="/",width=7,height=1,command= lambda : inp("/"))
    b1.grid(row=2,column=3)

    b1=Button(text="7",width=7,height=1,command= lambda: inp(7))
    b1.grid(row=3,column=0)

    b1=Button(text="8",width=7,height=1,command= lambda: inp(8))
    b1.grid(row=3,column=1)

    b1=Button(text="9",width=7,height=1,command= lambda: inp(9))
    b1.grid(row=3,column=2)

    minus=Button(text="-",width=7,height=1,command= lambda: inp("-"))
    minus.grid(row=3,column=3)

    b1=Button(text="4",width=7,height=1,command= lambda: inp(4))
    b1.grid(row=4,column=0)

    b1=Button(text="5",width=7,height=1,command= lambda: inp(5))
    b1.grid(row=4,column=1)

    b1=Button(text="6",width=7,height=1,command= lambda: inp(6))
    b1.grid(row=4,column=2)

    plus=Button(text="+",width=7,height=1,command= lambda: inp("+"))
    plus.grid(row=4,column=3)

    b1=Button(text="1",width=7,height=1,command= lambda: inp(1))
    b1.grid(row=5,column=0)

    b1=Button(text="2",width=7,height=1,command= lambda: inp(2))
    b1.grid(row=5,column=1)

    b1=Button(text="3",width=7,height=1,command= lambda: inp(3))
    b1.grid(row=5,column=2)

    b1=Button(text="%",width=7,height=1,command= lambda: inp('%'))
    b1.grid(row=5,column=3)

    b1=Button(text="0",width=7,height=1,command= lambda: inp(0))
    b1.grid(row=6,columnspan=2,ipadx=31)

    point=Button(text=".",width=7,height=1,command= lambda: inp("."))
    point.grid(row=6,column=2)

    equal=Button(text="=",width=7,height=1,command= lambda: PressEqual())
    equal.grid(row=6,column=3)
    
    win.mainloop()
