sales  = [] #declare empty list


while True:
     ch = input('press 1 for add 2 for show 3 for delete 4 for sort 5 for exit ')

     if ch =='1':
          d = int(input('enter data :'))
          sales.append(d)
     elif ch =='2':
          print(sales)
     elif ch =='3':
          d = int(input('enter data to remove  :'))
          if d in sales:
               sales.remove(d)
          else:
               print(d,' is not found ')
     elif ch =='4':
          sales.sort()
     elif ch =='5':
          break
     else:
          print('invalid choice ')
          
          
