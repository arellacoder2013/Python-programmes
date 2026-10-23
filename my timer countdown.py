
print("MY COUNTDOWN TIMER")

# Countdown recursion
def countdown(number):
    if number == 0:  
        print("Time is up!")
        return

    print(number)
    countdown(number - 1)  

countdown(20)



def factorial(number):
    if number <= 1:
        return 1
    return number * factorial(number - 1)

print("20! =", factorial(20))

print("A base case stops recursion safely.")
