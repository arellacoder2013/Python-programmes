import math
def check(n):
    count_digits =len(str(n))
    sum = 0
    x = n
    while (x!=0):
        r = x % 10
        sum = (int)  (sum+math.pow(r,count_digits))
        count_digits=count_digits -1
        x = x//10
    if sum==n:
        return 1
    else:
        return 0
n=65
if (check(n) == 1):
    print("Disarium number")
else :
    print("Not a Disarium")