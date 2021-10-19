if __name__ == '__main__':
    n = int(input().strip())
num=bin(n)
mc=0
maxc=0
for i in num[2:]:
    if i=="1":
        mc+=1
    else:
        if maxc<mc:
            maxc=mc
        mc=0
else:
    if maxc<mc:
            maxc=mc   
print(maxc)
