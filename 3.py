
f = open(r'C:\Users\HP\Desktop\python\day 3\string and file handling\cog.txt','r')


d = f.readlines()

f.close()

rc = len(d)
ind = ""
uk = ""

for r in d:

    w = r.split(',')
    print(w)
    
    if w[4] =='india\n':
        
        f1 = open(r'C:\Users\HP\Desktop\python\day 3\string and file handling\india.txt','a')
        
        f1.write(r)
        f1.close()
        
        
    elif w[4]=='uk\n':
        
        f2 = open(r'C:\Users\HP\Desktop\python\day 3\string and file handling\uk.txt','a')
    
        f2.write(r)
        f2.close()
 
    






