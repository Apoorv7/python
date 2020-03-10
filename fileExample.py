
f = open(r'C:\Users\techvision\Desktop\Python Session - 6th Sep.txt','r')
#print(f)
#print f.read()
#print f.readline()
#print f.readline()

d = f.readlines()

f.close()

#get row count
rc = len(d)
wc = 0
pwc = 0

for l in d:
    w = l.split(' ')
    wc = wc+ len(w)
    for ww in w:
        if ww =='to':
            pwc = pwc+1
            
    print l

print 'no of rows ',rc
print 'no  of words :',wc
print 'to count : ',pwc





