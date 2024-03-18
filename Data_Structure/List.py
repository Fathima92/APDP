# Create a list of fruits
fruits = ["apple", "banana", "orange", "mango"]

# Access elements by index
first_fruit = fruits[0]  # first_fruit will be "apple"
last_fruit = fruits[-1]  # last_fruit will be "mango"

# Print the entire list
print(fruits)  # Output: ["apple", "banana", "orange", "mango"]

# Add elements to the list
fruits.append("grapes")  # Appends "grapes" to the end

# Insert elements at specific positions
fruits.insert(1, "kiwi")  # Inserts "kiwi" at index 1

# Remove elements by value
fruits.remove("banana")  # Removes the first occurrence of "banana"

# Remove elements by index
del fruits[2]  # Removes the element at index 2 (previously "orange")

# Check if an element exists in the list
if "mango" in fruits:
    print("Mango is in the list")

# Get the length of the list
list_length = len(fruits)
print("Number of fruits:", list_length)  # Output: Number of fruits: 4

# Iterate over the list elements
for fruit in fruits:
    print(fruit)  # Prints each fruit on a new line

# List slicing: Extract a sub-list
sliced_fruits = fruits[1:3]  # Extracts elements at index 1 (inclusive) to 3 (exclusive)
print("Sliced fruits:", sliced_fruits)  # Output: Sliced fruits: ["kiwi", "grapes"]
