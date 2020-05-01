class Solution:
    def __init__(self):
        self.stack=list()
        self.queue=list()
    def pushCharacter(self,ss1):
        self.stack.append(ss1)
    def enqueueCharacter(self,ss2):
        self.queue.append(ss2)
    def popCharacter(self):
        return self.stack[0]
    def dequeueCharacter(self):
        return self.queue[len(self.queue)-1]

s=input("Enter a string : ")
obj=Solution()   
l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
#pop the top character from stack dequeue the first character from queue compare both the characters
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")    