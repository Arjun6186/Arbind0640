from tkinter import *
import fungetindex as f12
import buttondef as bf
import randword as rw
import figure as df1
def guess():
    root1=Tk()
    root1.geometry("600x600")
    root1.title("guess a fruit name")
    can=Canvas(root1,bg="Hotpink1",height=300,width=600)
    can.place(x=0,y=0)
    global hd
    df1.init(hd)
    f2=Frame(root1,bg="cyan",height=200,width=600)
    f2.place(x=0,y=400)
    f3=Frame(root1,bg="blue",height=100,width=600)
    f3.place(x=0,y=300)
    t1=Text(f3,bg="blue")
    labelfont=('times',40,'bold')
    t1.config(font=labelfont)
    global pd
    bf.hiddenword=hd
    bf.printword=pd
    t1.insert(END,pd)
    t1.place(x=100,y=10)
    b1=Button(f2,text="A",bg="dark goldenrod",width=8,height=3,command=lambda:bf.aword(t1,b1,can))
    b2=Button(f2,text="B",bg="dark goldenrod",width=8,height=3,command=lambda:bf.bword(t1,b2,can))
    b3=Button(f2,text="C",bg="dark goldenrod",width=8,height=3,command=lambda:bf.cword(t1,b3,can))
    b4=Button(f2,text="D",bg="dark goldenrod",width=8,height=3,command=lambda:bf.dword(t1,b4,can))
    b5=Button(f2,text="E",bg="dark goldenrod",width=8,height=3,command=lambda:bf.eword(t1,b5,can))
    b6=Button(f2,text="F",bg="dark goldenrod",width=8,height=3,command=lambda:bf.fword(t1,b6,can))
    b7=Button(f2,text="G",bg="dark goldenrod",width=8,height=3,command=lambda:bf.gword(t1,b7,can))
    b8=Button(f2,text="H",bg="dark goldenrod",width=8,height=3,command=lambda:bf.hword(t1,b8,can))
    b9=Button(f2,text="I",bg="dark goldenrod",width=8,height=3,command=lambda:bf.iword(t1,b9,can))
    b10=Button(f2,text="J",bg="dark goldenrod",width=8,height=3,command=lambda:bf.jword(t1,b10,can))
    b11=Button(f2,text="K",bg="dark goldenrod",width=8,height=3,command=lambda:bf.kword(t1,b11,can))
    b12=Button(f2,text="L",bg="dark goldenrod",width=8,height=3,command=lambda:bf.lword(t1,b12,can))
    b13=Button(f2,text="M",bg="dark goldenrod",width=8,height=3,command=lambda:bf.mword(t1,b13,can))
    b14=Button(f2,text="N",bg="dark goldenrod",width=8,height=3,command=lambda:bf.nword(t1,b14,can))
    b15=Button(f2,text="O",bg="dark goldenrod",width=8,height=3,command=lambda:bf.oword(t1,b15,can))
    b16=Button(f2,text="P",bg="dark goldenrod",width=8,height=3,command=lambda:bf.pword(t1,b16,can))
    b17=Button(f2,text="Q",bg="dark goldenrod",width=8,height=3,command=lambda:bf.qword(t1,b17,can))
    b18=Button(f2,text="R",bg="dark goldenrod",width=8,height=3,command=lambda:bf.rword(t1,b18,can))             
    b19=Button(f2,text="S",bg="dark goldenrod",width=8,height=3,command=lambda:bf.sword(t1,b19,can))
    b20=Button(f2,text="T",bg="dark goldenrod",width=8,height=3,command=lambda:bf.tword(t1,b20,can))
    b21=Button(f2,text="U",bg="dark goldenrod",width=8,height=3,command=lambda:bf.uword(t1,b21,can))
    b22=Button(f2,text="V",bg="dark goldenrod",width=8,height=3,command=lambda:bf.vword(t1,b22,can))
    b23=Button(f2,text="W",bg="dark goldenrod",width=8,height=3,command=lambda:bf.wword(t1,b23,can))
    b24=Button(f2,text="X",bg="dark goldenrod",width=8,height=3,command=lambda:bf.xword(t1,b24,can))
    b25=Button(f2,text="Y",bg="dark goldenrod",width=8,height=3,command=lambda:bf.yword(t1,b25,can))
    b26=Button(f2,text="Z",bg="dark goldenrod",width=8,height=3,command=lambda:bf.zword(t1,b26,can))
    b1.place(x=0,y=0)
    b2.place(x=60,y=0)
    b3.place(x=116,y=0)
    b4.place(x=174,y=0)
    b5.place(x=232,y=0)
    b6.place(x=290,y=0)
    b7.place(x=348,y=0)
    b8.place(x=406,y=0)
    b9.place(x=464,y=0)
    b10.place(x=0,y=52)
    b11.place(x=58,y=52)
    b12.place(x=116,y=52)
    b13.place(x=174,y=52)
    b14.place(x=232,y=52)
    b15.place(x=290,y=52)
    b16.place(x=348,y=52)
    b17.place(x=406,y=52)
    b18.place(x=464,y=52)
    b19.place(x=0,y=104)
    b20.place(x=58,y=104)
    b21.place(x=116,y=104)
    b22.place(x=174,y=104)
    b23.place(x=232,y=104)
    b24.place(x=290,y=104)
    b25.place(x=348,y=104)
    b26.place(x=406,y=104)
   
root=Tk()
root.title("Hangman")
root.geometry("600x600")
f=Frame(root,height=600,bg="orange",width=600)
f.pack()
t=Text(f,bg="orange")
labelfont=('times',30,'bold')
t.config(font=labelfont)
t.insert(END,"welcome in hangman game ")
t.place(x=100,y=100)
hd=rw.fruits()
l=[]
for i in hd:
    l.append("-")
pd=''.join(l)
b=Button(f,text="play",height=1,width=10,font=labelfont,bg="red",command=guess)
b.place(x=250,y=300)

