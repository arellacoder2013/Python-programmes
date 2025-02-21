class Dog:
    species = "Dog"
    def __init__(self,color,age,breed,name):
        self.color=color
        self.age = age
        self.breed = breed
        self.name = name
daisy = Dog("white","5","Golden retriever","Daisy")
luna = Dog("black","7","German shepherd","Luna")
print("Hi i am a ",daisy.species,"and my name is ",daisy.name)
print("My color is",daisy.color)
print("My age is ",daisy.age)
print("My breed is ",daisy.breed)
print("Hi i am a ",luna.species,"and my name is",luna.name)
print("My color is",luna.color)
print("My age is ",luna.age)
print("My breed is ",luna.breed)



    
    
