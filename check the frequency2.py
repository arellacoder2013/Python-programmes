restaurant_orders={'Belle': 3,'John':1,'Jordan':2,'Tom':4,'Jane':3,'Peter':3,'Lucy':2}
print("The original dictionary : "+ str(restaurant_orders))
K = 3
res = 0
for key in restaurant_orders:
    if restaurant_orders[key] == K:
        res = res + 1
print("The number or orders of  K is : "+str(res))