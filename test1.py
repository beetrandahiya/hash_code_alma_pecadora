n = int(input())
liked=[]
disliked=[]
for i in range(n):
    inp1=input()
    inp2=input()
    inp1=inp1.split()
    inp2=inp2.split()
    for j in range(1,len(inp1)):
        liked.append(inp1[j])
    for j in range(1,len(inp2)):
        disliked.append(inp2[j])


for i in range(len(disliked)):
    if(disliked[i] in liked):
        index=liked.index(disliked[i])
        liked.pop(index)
        
finalstring=str(len(liked))+" "

for i in range(len(liked)):
    finalstring+=liked[i]+" "

print(finalstring)