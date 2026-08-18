import os
print("===History notes===")
with open("history notes.txt","r") as f:
    for line in f:
        print(line.strip())
print()

print("===Word count===")
with open("math notes.txt","r") as f:
    for line in f:
        words = line.split()
        print(len(words), "words->",line.strip())
print()

print("===Merging notes===")
if os.path.exists("all-study-notes.txt"):
    print("all-study-notes.txt already exists-overwriting...")
else:
    print("all-study-notes.txt not found-creating now...")

content=""
with open("history notes.txt","r")as f:
    content+= "---history notes.txt---\n"
    content+=f.read() + "\n"
with open("math notes.txt","r")as f:
    content+= "---math notes.txt---\n"
    content+=f.read() + "\n"

with open("all-study-notes.txt","w")as out:
    out.write(content)
print("Saved to all-study-notes.txt")
print()

if os.path.exists("all-study-notes.txt"):
    os.remove("all-study-notes.txt")
    print("all-study-notes.txt deleted")
else:
    print("all-study-notes.txt does not exist")



