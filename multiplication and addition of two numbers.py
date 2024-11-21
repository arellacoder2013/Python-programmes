def add(a,b):
    return a+b
def product(a,b):
    return a*b
print("A.Addition , B.Product")
choice=input("Enter A or B")
a = float(input("enter n1"))
b = float(input("enter n2"))
if choice=="A":
 print(add(a,b))
else:
 print(product(a,b))
