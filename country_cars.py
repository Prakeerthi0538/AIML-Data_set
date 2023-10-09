## Brand and country...
##a=open(r"C:\Users\prake\Desktop\AIML\cars_country.csv",'r')
##b=a.readlines()
##a.close()
##c=[]
##for i in b:
##    c.append(i.split(','))
##d={}
##for i in c[1:]:
##    if i[0] not in d.keys():
##        d[i[0]]={}
##        if i[-1] not in d[i[0]].keys():
##            d[i[0]][i[-1]]=1
##        else:
##            d[i[0]][i[-1]]+=1
##    else:
##        if i[-1] not in d[i[0]].keys():
##            d[i[0]][i[-1]]=1
##        else:
##            d[i[0]][i[-1]]+=1
##for i in d:
##    print(i,d[i])


## Country and brand...
a=open(r"C:\Users\prake\Desktop\AIML\cars_country.csv",'r')
b=a.readlines()
a.close()
c=[]
for i in b:
    c.append(i.split(','))
d={}
for i in c[1:]:
    if i[-1] not in d.keys():
        d[i[-1]]={}
        if i[0] not in d[i[-1]].keys():
            d[i[-1]][i[0]]=1
        else:
            d[i[-1]][i[0]]+=1
    else:
        if i[0] not in d[i[-1]].keys():
            d[i[-1]][i[0]]=1
        else:
            d[i[-1]][i[0]]+=1
for i in d:
    print(i,d[i])
