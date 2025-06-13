def OddOccurring(arr):
#initialize result
    res = 0
#traverse the array
    for element in arr:
#
        res = res ^ element
    return res
arr = []
n = int(input("Enter array size"))
while(n):
    num = int(input("Enter your number :"))
    arr.append(num)
    n-=1
print("\n\nOdd occuring number is :",OddOccurring(arr))

   