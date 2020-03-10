class calc: #prent class


     def add(s,a,b):
          print(a+b)


     def sub(s,a,b):
          print(a-b)


class newcal(calc):  #newcal is child class
     def mul(a,b,c):
          print(b*c)


###create object of child class, child class object can access to parent class member
o = newcal()
o.sub(11,3)
o.mul(1,2)
o.add(11,2)


          
     
