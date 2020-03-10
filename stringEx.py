s ="  this is python code. this is not a java code"

print (s.upper())
print (s.lower())
print (s.title())
print (s.strip())
print (s.replace('is','are').replace('code','programing language'))


a = list(s)
print (a)
'''
#slicer
print s[2]
print s[2:5]
print s[:6]

print s[-1]
print s[::-1]

##split
s = s.strip()
w = s.split(' ')
print w

#show count of words
print len(w)

#count of is word
c =0
for a in w:
    if a =='is':        
        c=c+1
        print 'are',
    else:
        print a,


print 'is count ',c
'''


        
    














