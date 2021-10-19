class Difference:
    def __init__(self, a):
        self.__elements = a
    # Add your code here
    maximumDifference=0
    def computeDifference(self):
        i,j=0,1
        l=self.__elements
        m=0
        while i<len(l)-1:
            if abs(l[i]-l[j])>m:
                m=(abs(l[i]-l[j]))
            j+=1
            if j==len(l):
                i+=1
                j=i+1
        Difference.maximumDifference=m
        
    
# End of Difference class
