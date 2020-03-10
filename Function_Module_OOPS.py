'''
Function : is set of command and instructions which is reusable
-------
There are following types of functions:
-no argument , no return
-no argument , with return
-argument , with no return
-argument , with return
-function with default argument
-function with dynamic arguments

Module: is collection of functions, and classes which is reusable
---------------
import module
from module import funname,funname
import module as m

OOPS: object oriented programing structure/system
---------------------
Advantage :
-Reusability of source code
-Support to modular programing , large/complex task can be written in small set of instructions
-Easy to manage the source code

There are following fundamenal of oops:
-class          : is wrapper of data member and function 
-object         : is an instance of class 


'''

#no argument, no return
def wel():
    print('welcome to fun world...')

#no argument, with return
def getData():
    n = int(input('etner num :'))
    name  = int(input('enter num :'))


    return n,name

#argument with no return
def add(a,b):
    c =a+b
    print(c)
    
#argument with return
def sub(a,b):
    c =a-b
    return c

#function with default argument
def addNum(a,b,c=0,d=0):
    n =a+b+c+d
    print(n)
#function with dynamic arguments
def add2(*arg):
    print(arg)
    print(len(arg))
    s = 0
    for a in arg:
        s = s+a

    print(s)
    


    
#call to function
wel()
wel()

a,b = getData()
print(a,b)

print(getData())

a,b =1,2

add(11,2)


a = sub(33,4)
print(a)

add(a,33)

addNum(1,2)
addNum(1,2,3)
addNum(1,2,3,4)


add2(1,2,43,4,5,5,)
add2(1,2,3,4,4,5,4,4,3,3,3,3,3,3)


    
