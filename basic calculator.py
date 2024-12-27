def add(x,y):
    return x+y
def product(x,y):
    return x*y
def minus(x,y):
   return x-y
print("A.Addition , B.Product,C.Difference")
choice=input("Enter A or B or C")
x = float(input("enter n1:"))
y = float(input("enter n2:"))
if choice=="A":
   print(add(x,y))
if choice=="B":
   print(product(x,y))
if choice=="C":
   print(minus(x,y))