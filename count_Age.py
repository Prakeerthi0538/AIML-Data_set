a=open(r'C:\Users\prake\Desktop\AIML\diabetes_data_upload.csv','r')
b=a.readlines()
a.close()
c=[]
for i in b:
    c.append(i.split(','))
d={}
ct=0
pev=0
nev=0
for i in c:# to exclude 1st col c[1:]
    if i[0]>='40':
        ct+=1
        if i[-1] in 'Negative\n':#having diabatis or not
            nev+=1
        else:
            pev+=1
print(ct)
print(pev)
print(nev)
##output: 45
