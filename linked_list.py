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
        self.head=head
        self.data=data
        # print(self.head)
        a=list()
        a.append(self.data)
    
mylist= Solution()
T=int(input("Enter number of elements to be inserted in a linked list :"))
head=None
print("Enter elements of a linked list : ")
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head);