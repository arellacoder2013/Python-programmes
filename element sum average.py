L = [4,5,1,2,9,7,10,8]
print("Original List :",L)
count = 0
for i in L:
    count +=i
avg = count/len(L)
print("sum = ",count)
print("average =%.2f " % avg)
max_value = max(L)
print(max_value)
min_value = min(L)
print(min_value)
new_List=L[:2]
print(new_List)
L_square=[i**2 for i in L]
print(L_square)
