class Calculator:
    def power(self,n,p):
        if n>=0 and p>=0:
            return pow(n,p)
        else:
            return "n and p should be non-negative"
myCalculator=Calculator()
