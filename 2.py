#salary fo male and female total 
f = open(r'C:\Users\HP\Desktop\python\day 3\string and file handling\cog.txt','r')
#print(f)
#print f.read()
#print f.readline()
#print f.readline()

d = f.readlines()

f.close()

rc = len(d)
mc = 0
fc = 0

for l in d:
    w = l.split(',')
    
    if w[2] =='male':
        mc = mc+int(w[3])
    elif w[2]=='female':
        fc = fc+int(w[3])
            
    


print ('no  of male :',mc)
print ('no of female :',fc)

