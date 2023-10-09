a=open(r'C:\Users\prake\Desktop\AIML\diabetes_data_upload.csv','r')
b=a.readlines()
a.close()
c=[]
for i in b:
    c.append(i.split(','))
d={}
for i in c[1:]:
    if i[1] not in d.keys():
        d[i[1]]={}
        if i[-1] not in d[i[1]].keys():
            d[i[1]][i[-1]]=1
        else:
            d[i[1]][i[-1]]+=1
    else:
         if i[-1] not in d[i[1]].keys():
            d[i[1]][i[-1]]=1
         else:
            d[i[1]][i[-1]]+=1
for i in d:
    print(i,d[i])
        
##f=0
##m=0
##fpve=0
##fnev=0
##mpve=0
##mnev=0
##for i in c:# to exclude 1st col c[1:]
##        if i[1] in 'Female':
##            f+=1
##            if i[-1] in 'Positive\n':
##                fpve+=1
##            else:
##                fnev+=1
##        else:
##            m+=1
##            if i[-1] in 'Positive\n':
##                mpve+=1
##            else:
##                mnev+=1
##print("Female",f)
##print("Positive",fpve)
##print("Negative",fnev)
##print("Male",m)
##print("Positive",mpve)
##print("Negative",mnev)
##

##Male {'Positive\n': 147, 'Negative\n': 181}
##Female {'Positive\n': 173, 'Negative\n': 19}
