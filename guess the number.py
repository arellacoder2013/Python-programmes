import random
number = random.randint(1,10)

number_of_guesses = 0
while number_of_guesses<5:
    guess = int(input("Welcome to number game. Enter your guess from numbers 1-10 :"))
    number_of_guesses = number_of_guesses+1
    if guess < number:
        print("Your guess is too low")
    if guess > number:
        print("Your guess is too high")
    if guess ==number:
        break
if guess ==number:
    print('You guessed in' +str(number_of_guesses)+ 'tries!')
else:
    print("You did not guess the number, The number was '", number)
