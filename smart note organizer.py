q=("how many lines to you want to organize?")
n=int(input(q))
file=open("notes for today.txt","r")
print(file.read(n))
file.close()
print()

file=open("notes for today.txt","r")
lines=file.readlines()
file.close()
print("Total lines:", len(lines))

for i in range(len(lines)):
    print(i+2,"->",lines[i].strip())
print()


word=input("Skip lines starting with:")
file=open("notes for today.txt","r")
for line in file:
    if  line.startswith(word):
        print("skip->",line.strip())
file.close()
print()

file=open("notes for today.txt","r")
lines=file.readlines()
file.close()
out=open("skipped-lines.txt","w")
for i in range(0, len(lines), 2):
    out.write(lines[i])
out.close()
print("Skipped lines saved to skipped-lines.txt")

file=open("skipped-lines.txt","r")
print(file.read())
file.close()


