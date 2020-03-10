#import tkinter
from tkinter import * # import all class, methods/functions

o = Tk()

l1 = Label(text='Enter First Name :')
l1.pack()
t1 = Entry()
t1.pack()


l2 = Label(text='Enter Last Name :')
l2.pack()
t2 = Entry()
t2.pack()

def test():
     
     fn = t1.get()
     ln = t2.get()
     n = fn+' '+ln
     print('you have entered :  ',n)
     
     
btn = Button(text='Submit',command=test)
btn.pack()

o.mainloop()






