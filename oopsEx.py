class clac:

    def getData(s):
        print('add ',s)
        s.a = int(input('enter dat :'))
        s.b = int(input('enter data :'))
    def show(x):
        c = x.a+x.b
        print(c)
        

#create object
o = clac()

o1 = clac()
print(o)
print(o1)

o.getData()
o.show()

