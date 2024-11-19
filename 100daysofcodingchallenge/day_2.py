#introduction to oops
class Newclass:
    def newfunction(self):
        print("hello")
        
obj = Newclass()
obj.newfunction()

#__init__
class bookshop:
    def __init__(self,title):
        self.Title = title
    def displaytitle(self):
        print("The title name is",self.Title)
obj = bookshop("python")
obj.displaytitle()

# Write a program to reverse an integer in Python.
n = int(input())
rev = 0
while n != 0:
    rev = rev * 10 + n % 10
    n = n // 10
    
print("After the reverse ",rev)

#to check if prime or not
n = int(input("enter a number greater  than 1: "))

if n>1:
    for i in range(2,n):
        if n % i == 0:
            print("not prime")
            break
    else:
        print("it is prime")
