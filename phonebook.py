import sys
def initial_phonebook():
    rows,cols=int(input("Please enter initial number of contact")),2
    phonebook=[]
    print(phonebook)
    for i in range(rows):
        print("Enter the details in following order")
        temp=[]
        for j in range(cols):
            if j ==0:
                temp.append(input("Enter name"))
                if temp[j]==""or temp[j]==" ":
                    sys.exit("name is mendatory,process exiting due to blank value1")
            if j==1:
                temp.append(int(input("Enter phone no")))
        phonebook.append(temp)
    print(phonebook)
pb=initial_phonebook()
    
