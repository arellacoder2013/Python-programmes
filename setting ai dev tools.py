print("Hello! I am AI Bot.")
print("Please enter your name: ")

name = input()


print(f"Nice to meet you, {name}!")


print("How are you feeling today? (good/bad/neutral) : ")
mood = input().lower()

if mood == "good":
    print("I'm glad to hear that!")
elif mood == "bad":
    print("I'm sorry to hear that. Hope things get better soon.")
elif mood == "neutral":
    print("I understand. It's okay to have mixed feelings.")
else:
    print("I see. Sometimes it's hard to put feelings into words.")

print("What is your favorite color? : ")
color = input().lower()

print(f"Your favorite color is {color}!")


print("What is your favorite food? : ")
food = input().lower()
print(f"Your favorite food is {food}!")


print(f"It was nice chatting with you {name}. Goodbye!")