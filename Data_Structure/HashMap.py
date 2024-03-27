class HashMap:
  """Simple hash map implementation using a dictionary."""

  def __init__(self):
    """Initializes an empty hash map."""
    self.data = {}  # Use a dictionary to store key-value pairs

  def set(self, key, value):
    """Inserts a key-value pair into the hash map."""
    self.data[key] = value

  def get(self, key):
    """Returns the value associated with a key, or None if not found."""
    return self.data.get(key)

  def remove(self, key):
    """Removes the key-value pair from the hash map if it exists."""
    if key in self.data:
      del self.data[key]

  def has_key(self, key):
    """Checks if a key exists in the hash map."""
    return key in self.data

# Example usage
my_hashmap = HashMap()

# Add key-value pairs
my_hashmap.set("name", "Alice")
my_hashmap.set("age", 30)
my_hashmap.set("city", "New York")

# Get values by key
name = my_hashmap.get("name")
age = my_hashmap.get("age")

# Check for key existence
if my_hashmap.has_key("city"):
  print("City exists in the hash map")

# Remove a key-value pair
my_hashmap.remove("age")

# Print the hash map contents (dictionaries don't guarantee order)
print(my_hashmap.data)
