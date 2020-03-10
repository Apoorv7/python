from tkinter import *
top_widget=Tk()
top_widget.geometry('400x120+650+300')
top_widget.title('Calculate HCF- Arjit')

label1=Label(top_widget,text='Enter First Number',bg='gold',fg='blue').place(x=25,y=25)
label2=Label(top_widget,text='Enter Second Number',bg='gold',fg='blue').place(x=25,y=55)

box1=Entry(top_widget)
box2=Entry(top_widget)

box1.focus()

box1.place(x=155,y=25)
box2.place(x=155,y=55)

def HCF():
    small_number=int(box1.get())
    big_number=int(box2.get())
    mylis=[]
    mtlist=[]
    for i in range(1,small_number+1):
       if small_number%i==0:
           mylis.append(i)
    for j in range(1,big_number+1):
       if big_number%j==0:
           mtlist.append(j)
    myasd=[]
    for c in range(len(mylis)):
       if mylis[c] in mtlist:
           myasd.append(mylis[c])
    print(myasd[-1])

btn=Button(top_widget,text='HCF',command=HCF).place(x=170,y=75)
top_widget.mainloop()
