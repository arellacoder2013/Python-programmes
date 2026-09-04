n=4
guess = input("Predict: how items in the list for n=4?")
points=list(range(1,n+1))
print("ÿour guess:",guess,"list:",points,"Items:",len(points))

input("Predict : what happens to list sizw as n grows? Press Enter")
for size in [4,10,100,1000]:
    print(f"n={size:<5} list uses {size>5} items in memory")