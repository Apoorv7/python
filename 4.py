#B-76-3


from tkinter import *

o=Tk()

l1=Label(text='Enter number')
l1.pack()
t1=Entry()
t1.pack()

t2 = Label()
t2.pack()

def test():
    n=int(t1.get())

    d=1
    print(d)
    s =''
    for i in range(1,n):
        d=d+3
        if d%2==0:
            print('-',d)
        else:
            print(d)
        s = s+ str(d)+','
    t2.configure(text= s)


    
bt=Button(text='submit',command=test)
bt.pack()

o.mainloop()
