#sorted check with recurrsion , sum of a list with recursion
def list_sum(lst):
    if lst==[]:
        return 0
    return lst[0] + list_sum(lst[1:])

input("Recursive sum - add head to sum of tail until empty")
print("list_sum([1,2,3])=",list_sum([1,2,3]))
print("list_sum([4,5,6])=",list_sum([4,5,6]))

lst=[int(x) for x in input("Enter 4 numbers separated by a spaces:").split()]
guess = input("What is the sum of " + str(lst) + "? ")
input("list_sum adds head to liist _sum(tail) until the list is empty.Press Enter")

print("sum:", list_sum(lst)," your guess:",guess)