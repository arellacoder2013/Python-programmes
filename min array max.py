def minElement(a,size):
    temp=a[0]#index 0 will be stored as a variable
    for i in range(1,size):
        temp=min(temp,a[i])
    return temp

def maxElement(a,size):
    temp=a[0]#index 0 will be stored as a variable
    for i in range(1,size):
        temp=max(temp,a[i])
    return temp

a = [12,1234,45,66,1]
size=len(a)

print("Minimum element of array:",minElement(a,size))
print("Minimum element of array:",maxElement(a,size))