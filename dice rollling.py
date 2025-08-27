import random

def roll_dice():
    roll = random.randint(1, 6)
    print(f"You rolled a {roll}")
    
    if roll == 6:
        print(" Well done !You rolled the highest number.")
    elif roll == 1:
        print("Maybe next time but you can try again.")

def play_game():
    while True:
        roll_dice()
        again = input("Roll again? (yes/no): ").lower()
        if again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play_game()