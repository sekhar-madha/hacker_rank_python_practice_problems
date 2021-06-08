if __name__ == '__main__':
    n = int(input())
    if n%2==0 and 2<=n and n<=5 :
        print("Not Weird")      
    elif n%2!=0 :
        print("Weird")
    elif n%2==0 and 6<=n and n<=20 :
        print("Weird")   
    elif n%2==0and n>20 :
        print("Not Weird")
