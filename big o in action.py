n=10

guess = input("Double loop at n=10 checks n x n pairs . How many?")

input("Formula :one calculation ,done.Press enter to run")
steps =1
print("steps=",steps,"->O(1) constant time -> steps never change ")

input("Loop:one step per item.Press enter to run")
steps = 0
for i in range(n):
    steps += 1
print("steps=",steps,"->O(n) linear time -> steps grow with n")

input("Double loop :checks every pair .Press Enter to run.")
steps=0
for i in range(n):
    for j in range(n):
        steps+=1
print("steps =",steps,"your guess;",guess,"-> O(n^2) quadratic time")

input("Two more notations.Press enter")
print("Big Omega  Ω -> best case lower bound")

print(" Big Theta Θ -> exact bound (worst = best)")
