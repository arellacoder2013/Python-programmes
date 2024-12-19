import sys
def initial_slambook():
    rows,cols=int(input("Please enter initial number of contact number ")),4
    slam_book=[]
    print(slam_book)
    for i in range(rows):
        print("Hello friends welcome to our Slambook")
        print("You may now proceed and fill in details about your friends")
        temp=[]
        for j in range(cols):
            if j ==0:
                temp.append(input("Enter name"))
                if temp[j]==""or temp[j]==" ":
                    sys.exit("name is mendatory,process exiting due to blank value1")
            if j==1:
                temp.append(int(input("Enter phone no")))
            if j==2:
                temp.append(str(input("Enter date of birth(dd/mm/yy):")))
                if temp[j]==""or temp[j]==" ":
                    temp[j]=None
            if j==3:
                temp.append(str(input("Enter category(Family/Friends/Work/Others):")))
                if temp[j]==""or temp[j]==" ":
                    temp[j]=None
       
def thanks():
    print("Thank you for using our slambook!. ")
    print("Please visit again!!")
    sys.exit("Goodbye,Have a nice day ahead")
    ch = 1
    pb =initial_slambook()
    while ch in((1,2,3,4,5)):
        ch=menu()
        if ch ==1:
            pb = add_contact(pb)
        else :
            thanks()
    phonebook.append(temp)
    print(phonebook)
pb=initial_slambook()
    

    
    