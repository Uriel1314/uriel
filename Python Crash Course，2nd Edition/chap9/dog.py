class Dog:
    """A simple attempt to model a dog."""  
  
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name # attribute
        self.age = age # attribute
        
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

my_dog = Dog('Willie', 6)
print(f"My dog's name is {my_dog.name.title()}")
print(f"My dog is {my_dog.age} years old.")

# A method is called
my_dog.sit()
my_dog.roll_over()

print("#"*34)
your_dog = Dog('Lucy', 3)
print(f"Your dog's name is {your_dog.name.title()}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()