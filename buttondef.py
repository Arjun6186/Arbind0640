import fungetindex as f12
import figure as df
from tkinter import *
from winsound import *
hiddenword=" "
printword=" "
def init(h,p):
    hiddenword=h
    printword=p
def aword(t1,b1,can):
    global hiddenword
    global printword
    if "a" in hiddenword:
        l=f12.getindex(hiddenword,"a")
        l1=list(printword)
        for i in l:
            l1[i]="a"
        printword=''.join(l1)
        t1.delete('1.0',END)
        t1.insert(END,printword)
        t1.place(x=100,y=10)
        b1["bg"]="green"
        Beep(300,500)
    else:
        b1.destroy()
        df.drawfigure(can,t1)
def bword(t1,b2,can):
    global hiddenword
    global printword
    if "b" in hiddenword:
        l=f12.getindex(hiddenword,"b")
        l1=list(printword)
        for i in l:
            l1[i]="b"
        printword=''.join(l1)
        t1.delete('1.0',END)
        t1.insert(END,printword)
        t1.place(x=100,y=10)
        b2["bg"]="green"
        Beep(300,500)
    else:
        b2.destroy()
        df.drawfigure(can,t1)
def cword(t1,b3,can):
    global hiddenword
    global printword
    if "c" in hiddenword:
        l=f12.getindex(hiddenword,"c")
        l1=list(printword)
        for i in l:
            l1[i]="c"
        printword=''.join(l1)
        t1.delete('1.0',END)
        t1.insert(END,printword)
        t1.place(x=100,y=10)
        b3["bg"]="green"
        Beep(300,500)
    else:
        b3.destroy()
        df.drawfigure(can,t1)
def dword(t1,b4,can):
    global hiddenword
    global printword
    if "d" in hiddenword:
        l=f12.getindex(hiddenword,"d")
        l1=list(printword)
        for i in l:
            l1[i]="d"
        printword=''.join(l1)
        t1.delete('1.0',END)
        t1.insert(END,printword)
        t1.place(x=100,y=10)
        b4["bg"]="green"
        Beep(300,500)
    else:
        b4.destroy()
        df.drawfigure(can,t1)
def eword(t1,b5,can):
    global hiddenword
    global printword
    if "e" in hiddenword:
        l=f12.getindex(hiddenword,"e")
        l1=list(printword)
        for i in l:
            l1[i]="e"
        printword=''.join(l1)
        t1.delete('1.0',END)
        t1.insert(END,printword)
        t1.place(x=100,y=10)
        b5["bg"]="green"
        Beep(300,500)
    else:
        b5.destroy()
        df.drawfigure(can,t1)
def fword(t1,b6,can):
    global hiddenword
    global printword
    if "f" in hiddenword:
        l=f12.getindex(hiddenword,"f")
        l1=list(printword)
        for i in l:
            l1[i]="f"
        printword=''.join(l1)
        t1.delete('1.0',END)
        t1.insert(END,printword)
        t1.place(x=100,y=10)
        b6["bg"]="green"
        Beep(300,500)
    else:
        b6.destroy()
        df.drawfigure(can,t1)
def gword(t1,b7,can):
    global hiddenword
    global printword
    if "g" in hiddenword:
        l=f12.getindex(hiddenword,"g")
        l1=list(printword)
        for i in l:
            l1[i]="g"
        printword=''.join(l1)
        t1.delete('1.0',END)
        t1.insert(END,printword)
        t1.place(x=100,y=10)
        b7["bg"]="green"
        Beep(300,500)
    else:
        b7.destroy()
        df.drawfigure(can,t1)
def hword(t1,b8,can):
    global hiddenword
    global printword
    if "h" in hiddenword:
        l=f12.getindex(hiddenword,"h")
        l1=list(printword)
        for i in l:
            l1[i]="h"
        printword=''.join(l1)
        t1.delete('1.0',END)
        t1.insert(END,printword)
        t1.place(x=100,y=10)
        b8["bg"]="green"
        Beep(300,500)
    else:
        b8.destroy()
        df.drawfigure(can,t1)
def iword(t1,b9,can):
    global hiddenword
    global printword
    if "i" in hiddenword:
        l=f12.getindex(hiddenword,"i")
        l1=list(printword)
        for i in l:
            l1[i]="i"
        printword=''.join(l1)
        t1.delete('1.0',END)
        t1.insert(END,printword)
        t1.place(x=100,y=10)
        b9["bg"]="green"
        Beep(300,500)
    else:
        b9.destroy()
        df.drawfigure(can,t1)
def jword(t1,b10,can):
    global hiddenword
    global printword
    if "j" in hiddenword:
        l=f12.getindex(hiddenword,"j")
        l1=list(printword)
        for i in l:
            l1[i]="j"
        printword=''.join(l1)
        t1.delete('1.0',END)
        t1.insert(END,printword)
        t1.place(x=100,y=10)
        b10["bg"]="green"
        Beep(300,500)
    else:
        b10.destroy()
        df.drawfigure(can,t1)
def kword(t1,b11,can):
    global hiddenword
    global printword
    if "k" in hiddenword:
        l=f12.getindex(hiddenword,"k")
        l1=list(printword)
        for i in l:
            l1[i]="k"
        printword=''.join(l1)
        t1.delete('1.0',END)
        t1.insert(END,printword)
        t1.place(x=100,y=10)
        b11["bg"]="green"
        Beep(300,500)
    else:
        b11.destroy()
        df.drawfigure(can,t1)
def lword(t1,b12,can):
    global hiddenword
    global printword
    if "l" in hiddenword:
        l=f12.getindex(hiddenword,"l")
        l1=list(printword)
        for i in l:
            l1[i]="l"
        printword=''.join(l1)
        t1.delete('1.0',END)
        t1.insert(END,printword)
        t1.place(x=100,y=10)
        b12["bg"]="green"
        Beep(300,500)
    else:
        b12.destroy()
        df.drawfigure(can,t1)
def mword(t1,b13,can):
    global hiddenword
    global printword
    if "m" in hiddenword:
        l=f12.getindex(hiddenword,"m")
        l1=list(printword)
        for i in l:
            l1[i]="m"
        printword=''.join(l1)
        t1.delete('1.0',END)
        t1.insert(END,printword)
        t1.place(x=100,y=10)
        b13["bg"]="green"
        Beep(300,500)
    else:
        b13.destroy()
        df.drawfigure(can,t1)
def nword(t1,b14,can):
    global hiddenword
    global printword
    if "n" in hiddenword:
        l=f12.getindex(hiddenword,"n")
        l1=list(printword)
        for i in l:
            l1[i]="n"
        printword=''.join(l1)
        t1.delete('1.0',END)
        t1.insert(END,printword)
        t1.place(x=100,y=10)
        b14["bg"]="green"
        Beep(300,500)
    else:
        b14.destroy()
        df.drawfigure(can,t1)
def oword(t1,b15,can):
    global hiddenword
    global printword
    if "o" in hiddenword:
        l=f12.getindex(hiddenword,"o")
        l1=list(printword)
        for i in l:
            l1[i]="o"
        printword=''.join(l1)
        t1.delete('1.0',END)
        t1.insert(END,printword)
        t1.place(x=100,y=10)
        b15["bg"]="green"
        Beep(300,500)
    else:
        b15.destroy()
        df.drawfigure(can,t1)
def pword(t1,b16,can):
    global hiddenword
    global printword
    if "p" in hiddenword:
        l=f12.getindex(hiddenword,"p")
        l1=list(printword)
        for i in l:
            l1[i]="p"
        printword=''.join(l1)
        t1.delete('1.0',END)
        t1.insert(END,printword)
        t1.place(x=100,y=10)
        b16["bg"]="green"
        Beep(300,500)
    else:
        b16.destroy()
        df.drawfigure(can,t1)
def qword(t1,b17,can):
    global hiddenword
    global printword
    if "q" in hiddenword:
        l=f12.getindex(hiddenword,"q")
        l1=list(printword)
        for i in l:
            l1[i]="q"
        printword=''.join(l1)
        t1.delete('1.0',END)
        t1.insert(END,printword)
        t1.place(x=100,y=10)
        b17["bg"]="green"
        Beep(300,500)
    else:
        b17.destroy()
        df.drawfigure(can,t1)
def rword(t1,b18,can):
    global hiddenword
    global printword
    if "r" in hiddenword:
        l=f12.getindex(hiddenword,"r")
        l1=list(printword)
        for i in l:
            l1[i]="r"
        printword=''.join(l1)
        t1.delete('1.0',END)
        t1.insert(END,printword)
        t1.place(x=100,y=10)
        b18["bg"]="green"
        Beep(300,500)
    else:
        b18.destroy()
        df.drawfigure(can,t1)
def sword(t1,b19,can):
    global hiddenword
    global printword
    if "s" in hiddenword:
        l=f12.getindex(hiddenword,"s")
        l1=list(printword)
        for i in l:
            l1[i]="s"
        printword=''.join(l1)
        t1.delete('1.0',END)
        t1.insert(END,printword)
        t1.place(x=100,y=10)
        b19["bg"]="green"
        Beep(300,500)
    else:
        b19.destroy()
        df.drawfigure(can,t1)
def tword(t1,b20,can):
    global hiddenword
    global printword
    if "t" in hiddenword:
        l=f12.getindex(hiddenword,"t")
        l1=list(printword)
        for i in l:
            l1[i]="t"
        printword=''.join(l1)
        t1.delete('1.0',END)
        t1.insert(END,printword)
        t1.place(x=100,y=10)
        b20["bg"]="green"
        Beep(300,500)
    else:
        b20.destroy()
        df.drawfigure(can,t1)
def uword(t1,b21,can):
    global hiddenword
    global printword
    if "u" in hiddenword:
        l=f12.getindex(hiddenword,"u")
        l1=list(printword)
        for i in l:
            l1[i]="u"
        printword=''.join(l1)
        t1.delete('1.0',END)
        t1.insert(END,printword)
        t1.place(x=100,y=10)
        b21["bg"]="green"
        Beep(300,500)
    else:
        b21.destroy()
        df.drawfigure(can,t1)
def vword(t1,b22,can):
    global hiddenword
    global printword
    if "v" in hiddenword:
        l=f12.getindex(hiddenword,"v")
        l1=list(printword)
        for i in l:
            l1[i]="v"
        printword=''.join(l1)
        t1.delete('1.0',END)
        t1.insert(END,printword)
        t1.place(x=100,y=10)
        b22["bg"]="green"
        Beep(300,500)
    else:
        b22.destroy()
        df.drawfigure(can,t1)
def wword(t1,b23,can):
    global hiddenword
    global printword
    if "w" in hiddenword:
        l=f12.getindex(hiddenword,"w")
        l1=list(printword)
        for i in l:
            l1[i]="w"
        printword=''.join(l1)
        t1.delete('1.0',END)
        t1.insert(END,printword)
        t1.place(x=100,y=10)
        b23["bg"]="green"
        Beep(300,500)
    else:
        b23.destroy()
        df.drawfigure(can,t1)
def xword(t1,b24,can):
    global hiddenword
    global printword
    if "x" in hiddenword:
        l=f12.getindex(hiddenword,"x")
        l1=list(printword)
        for i in l:
            l1[i]="x"
        printword=''.join(l1)
        t1.delete('1.0',END)
        t1.insert(END,printword)
        t1.place(x=100,y=10)
        b24["bg"]="green"
        Beep(300,500)
    else:
        b24.destroy()
        df.drawfigure(can,t1)
def yword(t1,b25,can):
    global hiddenword
    global printword
    if "y" in hiddenword:
        l=f12.getindex(hiddenword,"y")
        l1=list(printword)
        for i in l:
            l1[i]="y"
        printword=''.join(l1)
        t1.delete('1.0',END)
        t1.insert(END,printword)
        t1.place(x=100,y=10)
        b25["bg"]="green"
        Beep(300,500)
    else:
        b25.destroy()
        df.drawfigure(can,t1)
def zword(t1,b26,can):
    global hiddenword
    global printword
    if "z" in hiddenword:
        l=f12.getindex(hiddenword,"z")
        l1=list(printword)
        for i in l:
            l1[i]="z"
        printword=''.join(l1)
        t1.delete('1.0',END)
        t1.insert(END,printword)
        t1.place(x=100,y=10)
        b26["bg"]="green"
        Beep(300,500)
    else:
        b26.destroy()
        df.drawfigure(can,t1)
