#one odd occurring number

input("XOR numbers-pairs cancek,the odd one stay.Press enter")
print(" list:;[2,3,4,3,2]")
print("odd occurring:",2^3^4^3^2)

n =int(input("Enter a number(try 7 or 11):"))
nums=[3,n,5,3,5]
guess=input("Which number in"+str(nums)+"appears once")
result = 0

for x in nums:
    result^=x
input("XOR cancels pairs-the odd one survives press enter")
print(" list:",nums," odd occurring:",result,"your guess :",guess)