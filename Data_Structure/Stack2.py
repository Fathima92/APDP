class Stack:
  """Simple stack implementation using a list."""

  def __init__(self):
    """Initializes an empty stack."""
    self.items = []

  def isEmpty(self):
    """Checks if the stack is empty."""
    return len(self.items) == 0

  def push(self, item):
    """Pushes a new item onto the stack."""
    self.items.append(item)

  def pop(self):
    """Pops and returns the top item from the stack.

    Raises IndexError if the stack is empty.
    """
    if self.isEmpty():
      raise IndexError("Stack is empty")
    return self.items.pop()

  def peek(self):
    """Returns the top item from the stack without removing it.

    Raises IndexError if the stack is empty.
    """
    if self.isEmpty():
      raise IndexError("Stack is empty")
    return self.items[-1]

# Example usage
my_stack = Stack()

# Push elements onto the stack
my_stack.push("apple")
my_stack.push("banana")
my_stack.push("cherry")

# Print the top element
print("Top element:", my_stack.peek())

# Pop elements from the stack
print("Popped element:", my_stack.pop())
print("Popped element:", my_stack.pop())
print("Popped element:", my_stack.pop())

# Check if the stack is empty
if my_stack.isEmpty():
  print("Stack is empty")
