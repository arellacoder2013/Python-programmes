import sys
def initial_slambook():
    rows,cols=int(input("Please enter initial number of contact number ")),4
    slam_book=[]
    print(slam_book)
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
            if j==2:
                temp.append(str(input("Enter date of birth(dd/mm/yy):")))
                if temp[j]==""or temp[j]==" ":
                    temp[j]=None
            if j==3:
                temp.append(str(input("Enter category(Family/Friends/Work/Others):")))
                if temp[j]==""or temp[j]==" ":
                    temp[j]=None
        slam_book.append(temp)
    print(slam_book)
pb=initial_slambook()