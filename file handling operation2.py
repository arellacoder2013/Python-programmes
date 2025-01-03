new_file =open("newfile.txt",'x')
new_file.close()
import os
print("Checking if my_file exists or not....")
if os.path.exists('my_file.txt'):
    os.remove("my_file.txt")
else:
    print("This file doesnt exist")
my_file=open('my_file.txt','w')
my_file.write("Hi!! how are you doing?")
my_file.close()
os.remove("newfile.txt")
os.rmdir('folder')