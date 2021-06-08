if __name__ == '__main__':
    n = int(input())
    x=1
    y=str(x)
    for i in range(n+1):
        if i==0 or i==1:
            continue
        z=str(i)
        y=y+z
    print(y)    
