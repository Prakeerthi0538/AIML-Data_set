a=open(r'C:\Users\prake\Desktop\AIML\diabetes_data_upload.csv','r')
b=a.readlines()
a.close()
s=[]
for i in b:
    s.append(i.split(','))

##for i in range(len(s)):
##    for j in range(len(s[i])):
##        if s[i][j]=='':
##            print('row is:{},column is:{}'.format(i,j))

w={}
for i in range(len(s[0])):
    w[i]=0
print(w)
for i in s:
    for j in range(len(i)):
        if i[j]=='':
               w[j]+=1
print(w)
    
