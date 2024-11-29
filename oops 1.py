class fruit:
    def __init__ (self ,name,color):
        self.name=name
        self.color=color
    def intro(self):
        print("hello,I am",self.name)
    grape=fruit('grape','purple')
    grape.intro()