from tkinter import *
c=0
hd=" "
def init(str1):
    global c
    global hd
    c=1
    hd=str1
def drawfigure(can,t1):
    global c
    if c==1:
        can.create_line(10,290,90,290,fill="black",width=3)
        can.create_line(50,290,50,40,fill="black",width=3)
        c+=1
    elif c==2:
        can.create_line(50,40,450,40,fill="black",width=3)
        can.create_line(50,90,100,40,fill="black",width=3)
        c+=1
    elif c==3:
        can.create_line(450,40,450,100,fill="black",width=3)
        c+=1
    elif c==4:
        can.create_oval(435,100,465,130,outline="black",width=3)
        c+=1
    elif c==5:
        can.create_line(450,130,450,220,fill="black",width=3)
        c+=1
    elif c==6:
        can.create_line(450,145,420,165,fill="black",width=3)
        can.create_line(450,145,480,165,fill="black",width=3)
        c+=1
    else:
        can.create_line(450,220,420,240,fill="black",width=3)
        can.create_line(450,220,480,240,fill="black",width=3)
        t1.delete("1.0",END)
        t1.insert(END,hd)
        
        
