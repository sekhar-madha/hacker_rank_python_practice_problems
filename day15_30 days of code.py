class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data):
        new = Node(data)
        if head:
            tail = head
            while tail.next:
                tail = tail.next
            tail.next = new
            return head
        else:
            return new

mylist= Solution()
