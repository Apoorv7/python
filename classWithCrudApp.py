class emp:

     def newemp(s):
          s.eid = input('enter eid :')
          s.name = input('enter name :')
          s.sal = int(input('enter basic sal :'))          

     def compute(s):
          s.hra = s.sal*.40
          s.da = s.sal*.20
          s.msal = s.sal+s.hra+s.da
          s.ysal  = s.msal * 12
          
          if s.ysal < 300000 :
               s.tax = 0
          elif s.ysal<500000:
               s.tax = (s.ysal-300000)*.05
          elif s.ysal<1000000:
               s.tax = 10000+(s.ysal-500000)*.20
          else:
               s.tax = 110000+(s.ysal-1000000)*.30
     def __init__(s):
          print(s,' is created')
          
     def __del__(s):
          print(s,' is deleted  ')
          
     def show(add):
          print('*************Employee Details****************')
          print('Employee Id : ',add.eid)
          print('Employee Name : ',add.name)
          print('Employee Monthly Sal : ',add.msal)
          print('Employee Yearly Sal : ',add.ysal)
          print('Employee Tax : ',add.tax)
     
          
          
##create object
ee = emp()


ee.newemp()
ee.compute()

del ee  # remove object


'''
emps = []
for i in range(0,500):     
     e = emp()
     e.newemp()
     e.compute()
     emps.append(e)
     
print(emps)

for o in emps:     
     o.show()
'''  

          
