#Power set, binary mask as a subset selector

input("a set with n elements has 2^n subsets.Press enter")
print(" 3 elements 2^3=",2**3,"subsets")
print(" mask 5 =binary", bin(5)[2:])

n=int(input("ENter number of elements (try 4 or 5):"))
guess = input("How may subsets does a set have?"+ str(n) + "elements have?")
input("Each element is in or out-2 choices per elements.Press enter")
print(" ",n, "elements subsets:",2**n,"your guess:",guess)