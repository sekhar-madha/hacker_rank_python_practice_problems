class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self,firstName,lastName,idNumber,scores):
        self.firstName=firstName
        self.lastName=lastName
        self.idNumber=idNumber
        self.scores=scores

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        a=sum(self.scores)//len(self.scores)
        if a>=90 and a<=100:
            return "O"
        elif a>=80 and a<90:
            return "E"
        elif a>=70 and a<80:
            return "A"
        elif a>=55 and a<70:
            return "P"
        elif a>=40 and a<55:
            return "D"
        else:
            return "T"
            
line = input().split()
