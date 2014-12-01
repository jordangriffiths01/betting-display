from tkinter import *
from random import randint

TEXTS = ['aaaa', 'bbbb', 'cccc', '1234']

def move():
    global Dx,Dy
    x1,y1=w.coords(id1)
    if x1+Dx<=0 or x1+Dx>=190:
        Dx=-Dx
    if y1+Dy<=0 or y1+Dy>=190:
        Dy=-Dy
    w.coords(id1,x1+Dx,y1+Dy)
    root.after(50,move)
    
def change_text():
    new_text = TEXTS[randint(0,3)]
    w.itemconfig(id1, text=new_text)
    root.after(500, change_text)
    
    
    

root=Tk()
w = Canvas(root, width=200, height=200,
           borderwidth=0,
           highlightthickness=0,
           background='white')
w.pack(padx=10,pady=10)
button1=Button(root,text='Move')
button1.pack()
button1.bind('<Button-1>',move)
Dx=1
Dy=1
id1=w.create_text(20,20, text='test')
root.after(50,move)
root.after(500, change_text)
root.mainloop()


