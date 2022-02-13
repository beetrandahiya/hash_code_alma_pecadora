import matplotlib.pyplot as plt


n = int(input())
liked=[]
disliked=[]
####################################
like=[]
dislike=[]  #for individual customer
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

all_ing = liked + disliked
all_ing=list(set(all_ing))

likeness=[];
dislikeness=[];


for i in range(len(all_ing)):
    k=0
    dk=0
    for j in range(len(like)):
        if all_ing[i] in like[j]:
            k+=1
    likeness.append(k)
    for j in range(len(dislike)):
        if all_ing[i] in dislike[j]:
            dk+=1
    dislikeness.append(dk)
    

plt.plot(likeness, color = 'b')
plt.plot(dislikeness, color = 'r')
plt.show()

final_ing=[]
for i in range(len(all_ing)):
    if(dislikeness[i]<likeness[i]):
        final_ing.append(all_ing[i])


finalstring=str(len(final_ing))+" "

for i in range(len(final_ing)):
    finalstring+=final_ing[i]+" "


file=open('e.txt','w')
file.write(finalstring)
file.close()





