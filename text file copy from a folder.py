import os
import shutil
r=''
data=os.listdir(r"C:\Users\HP\Desktop\acp")
w = open(r"C:\Users\HP\Desktop\out.txt",'a')
for file in data:
    
    if file.endswith(".txt"):

        path =r"C:\Users\HP\Desktop\acp\\"+file
        f = open(path,'r')
        
        w.write(f.read())#or readlines can also be used if do not WANT TO USE LOOP

        #shutil.copyfile(r,r"C:\Users\HP\Desktop\acp\all.txt")this i also used to copu file with same extension
    


w.close()



