
class Account:
 
    def __init__(self, owner, pin):
        self.owner = owner
        self.__pin = pin
 
    
    def show_pin_status(self):
        print("Account Owner:", self.owner)
        print("PIN is safely stored inside the class.")
 

    def set_pin(self, new_pin):
        if len(new_pin) == 6 and new_pin.isdigit():
            self.__pin = new_pin
            print("PIN successfully updated✅.")
        else:
            print("❌Invalid PIN. PIN must be exactly 6 digits.")
 
    
    def check_pin(self, entered_pin):
        if entered_pin == self.__pin:
            print("Access granted.")
        else:
            print("Access denied.")
 
    
    def __str__(self):
        return "Account holder: " + self.owner
 
 

my_account = Account("John Doe", "345672")
 

print(my_account)
 

my_account.show_pin_status()
 

my_account.__pin = "676769"
print("Tried changing PIN directly from outside.")
 
my_account.check_pin("676769")
my_account.check_pin("345672")
 

my_account.set_pin("676769")


my_account.check_pin("676769")
