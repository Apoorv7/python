f = open(r'C:\Users\HP\Desktop\python\day 3\string and file handling\cog.txt','r')
#print(f)
#print f.read()
#print f.readline()
#print f.readline()

d = f.readlines()

f.close()

rc = len(d)#calculate the lenght of the data 
print (rc)
mc = 0
fc = 0

for l in d:
    w = l.split(',')#split is used to break the string by ',' operator
    for ww in w:
        if ww =='male':
            mc = mc+1
        elif ww=='female':
            fc=fc+1
            
    


print ('no  of male :',mc)
print ('no of female : ',fc)






