# Variables and Data Types
name = "Alice"
age = 25
height = 5.6  # in feet
is_student = True

# Conditional Statements
if age < 18:
    print("You are a minor.")
elif age < 60:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

# Loops
for i in range(5):
    print(f"Loop iteration: {i}")

# Functions
def greet(user_name):
    return f"Hello, {user_name}!"

print(greet(name))

# Lists
fruits = ["Apple", "Banana", "Cherry"]
for fruit in fruits:
    print(f"I like {fruit}")

# Dictionary
person = {"name": "Alice", "age": 25, "city": "New York"}
print(f"Name: {person['name']}, Age: {person['age']}")

# While loop
count = 0
while count < 3:
    print(f"Count is {count}")
    count += 1
