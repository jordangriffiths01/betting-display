from tkinter import *
from random import randint

TEXTS = ['aaaa', 'bbbb', 'cccc', '1234']

def move():
    global Dx,Dy
    x1,y1=w.coords(id1)
    if x1+Dx<=0 or x1+Dx>=800:
        Dx=-Dx
    if y1+Dy<=0 or y1+Dy>=800:
        Dy=-Dy
    w.coords(id1,x1+Dx,y1+Dy)
    root.after(50,move)
    
def change_text():
    new_text = TEXTS[randint(0,3)]
    w.itemconfig(id1, text=new_text)
    root.after(500, change_text)
    
    
    

root=Tk()
root.attributes("-fullscreen", True)
w = Canvas(root, width=1000, height=1000,
           borderwidth=0,
           highlightthickness=0,
           background='white')
w.pack(padx=10,pady=10)
button1=Button(root,text='Move')
button1.pack()
button1.bind('<Button-1>',move)
Dx=1
Dy=1

photo = PhotoImage(file='horse.gif')
id2 = w.create_image(0, 0, image=photo, anchor=NW)
photo2 = PhotoImage(file='logo.gif')
id3 = w.create_image(0, 0, image=photo2, anchor=NW)
photo3 = PhotoImage(file='logo2.gif')
id4 = w.create_image(435, 0, image=photo3, anchor=NW)
id1=w.create_text(20,20, text='test', fill='white')

root.after(50,move)
root.after(500, change_text)
root.mainloop()


