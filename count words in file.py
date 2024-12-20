with open("C:/Users/Owner/Downloads/Python programmes/myfile.txt",'w')as file1:
    file1.write("Hello How are you\nGood morning Happy")
file1.close()
with  open("C:/Users/Owner/Downloads/Python programmes/myfile.txt",'r')as file1:
    data=file1.readlines()
    print("The words in the file are")
    for line in data:
        word=line.split()
        print(word)
file1.close()