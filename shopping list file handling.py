file=open("shopping-list.txt","w")
file.write("1.Buy two cartons of milk\n")
file.write("2.Buy carrots\n")
file.write("3.Buy potatoes\n")
file.write("4.Buy bread\n")

file.close()
print("Shopping list saved to shopping-list.txt")

file=open("shopping-list.txt","r")
content = file.read()
print(content)
file.close()

file = open("shopping-list.txt","r")
lines=file.readlines()
print(f"You have {len(lines)} items on your shopping list")
file.close()

file=open("shopping-list.txt","a")
file.write("5. Buy toys for James\n")
file.write("6.Buy butter,tomatoes and fruits\n")
file.write("7.Buy paracetamol")

file.close()
print("\n3 more items added!")

file=open("shopping-list.txt","r")
print("\n===Updated Shopping List ===")
print(file.read())
file.close()


