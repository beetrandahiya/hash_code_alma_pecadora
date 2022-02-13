n = int(input())

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
        like[i].append(inp1[j])
    for j in range(1,len(inp2)):
        dislike[i].append(inp2[j])
    costumers[i]=[like[i],dislike[i]]
    costm[i]=""


print(like)
print(dislike)


print(costumers)

for i in range(n):
    for j in range(n):
        if(i!=j):
            a_set=set(like[i])
            b_set=set(dislike[j])
            if len(a_set.intersection(b_set)) > 0:
                costm[i]+=str(j)
                costm[j]+=str(i)

print(costm)
for i in range(n):
    costm[i]=removeDupStr(costm[i])
print(costm)









