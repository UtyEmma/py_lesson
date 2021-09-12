# Create Classes
class User:
    def __init__(self, name, email, age) :
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f"My Name is {self.name} and I amd {self.age}"

    def has_birthday(self):
        self.age += 4


class Customer(User):
    def __init__(self, name, email, age) :
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def setBalance(self, balance):
        self.balance = balance

# brad = User("Brad Traversy", "brad@gmail.com", 5)
# print(brad.email)

# brad.has_birthday()
# print(brad.greeting())

janet = Customer("Janet", "jane@jane.com", 20)
janet.setBalance(900)
print(janet.balance)