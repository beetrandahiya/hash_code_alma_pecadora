n = int(input())
liked=[]
disliked=[]
####################################
like=[]
dislike=[]  #for individual customer

costumers={}
costm={}

def removeDupStr(str): 

    return "".join(set(str)) 

####################################
for i in range(n):
    inp1=input()
    inp2=input()
    inp1=inp1.split()
    inp2=inp2.split()
    like.append([])
    dislike.append([])
    for j in range(1,len(inp1)):
        liked.append(inp1[j])
        like[i].append(inp1[j])
    for j in range(1,len(inp2)):
        disliked.append(inp2[j])
        dislike[i].append(inp2[j])
    costumers[i]=[like[i],dislike[i]]
    costm[i]=""


all_ing = liked + disliked
all_ing=list(set(all_ing))


for i in range(n):
    for j in range(n):
        if(i!=j):
            a_set=set(like[i])
            b_set=set(dislike[j])
            if len(a_set.intersection(b_set)) > 0:
                costm[i]+=str(j)
                costm[j]+=str(i)


n_conflict=[]

for i in range(n):
    costm[i]=removeDupStr(costm[i])
    n_conflict.append(len(costm[i]))

data=[]
def Convert(string):
    list1=[]
    list1[:0]=string
    return list1

nodeState=[]

for i in range(n):
    nodeState.append(1)
    a=Convert(costm[i])
    data.append([])
    for j in range(len(a)):
        data[i].append(int(a[j]))
        data[i].sort()


for i in range(n):
    for j in range(len(data[i])):
        k = int(data[i][j])
        a=len(data[i])
        b=len(data[k])

        if(a>b):
            data[i]=[]
            nodeState[i]=0
            for l in range(n):
                if(l!=i):
                    if i in data[l]:
                        data[l].remove(i)
            
            break

        elif(b>a):
            data[k]=[]
            nodeState[k]=0
            for l in range(n):
                if(l!=k):
                    if k in data[l]:
                        data[l].remove(k)
            break

for i in range(n):
    if(len(data[i])==1):
        a=i
        b=data[i][0]
        if(a>b):
            data[a]=[]
            data[b]=[]
            nodeState[a]=0
        else:
            data[b]=[]
            data[a]=[]
            nodeState[b]=0

finalstr=""
finalarr=[]
an=0
for i in range(n):
    if(nodeState[i]==1):
        for j in range(len(dislike[i])):
            if(dislike[i][j] in all_ing):
                all_ing.remove(dislike[i][j])
            


finalarr=list(set(all_ing))  
finalstr+= str(len(finalarr))+" "
for i in range(len(finalarr)):
    finalstr+=str(finalarr[i])+" "


file=open('e.txt','w')
file.write(finalstr)
file.close()











