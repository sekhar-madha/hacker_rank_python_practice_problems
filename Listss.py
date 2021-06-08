if __name__ == '__main__':
    N = int(input())
    lst=[]
    while True:
        try:
            data=list(map(str,input().split()))
            if data[0]=="insert":
                lst.insert(int(data[1]),int(data[2]))
                data.clear()
                continue
            elif data[0]=="print":
                data.clear()
                print(lst)
            elif data[0]=="remove":
                lst.remove(int(data[1]))
                data.clear()
                continue
            elif data[0]=="append":
                lst.append(int(data[1]))
                data.clear()
                continue
            elif data[0]=="sort":
                data.clear()
                lst.sort()
                continue
            elif data[0]=="pop":
                lst.pop()
                data.clear()
                continue
            elif data[0]=="reverse":
                lst.reverse()
                data.clear()
                continue
        except:
            break
        
