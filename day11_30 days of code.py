if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
#for first order rows
fs=[]
ms=[]
ls=[]
for i in arr[0:len(arr)-2]:
    l=[sum(i[k:k+3]) for k in range(len(i)) if k<4]
    fs.append(l)
#for middle order rows
for i in arr[1:len(arr)-1]:
    l=[k for k in i[1:len(i)-1]]
    ms.append(l)
#last order rows
for i in arr[2:]:
    l=[sum(i[k:k+3]) for k in range(len(i)) if k<4]
    ls.append(l)
maxs=[]
i,j=0,0
temp=0
while i!=len(fs[0]) and j!=len(fs):
    temp=fs[j][i]+ms[j][i]+ls[j][i]
    i+=1
    if i==len(fs[0]):
        j+=1
        i=0
    #if maxs<temp:
    maxs.append(temp)
print(max(maxs))
