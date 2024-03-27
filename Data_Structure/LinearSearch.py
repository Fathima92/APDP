def linear_search(data, target):

  for i in range(len(data)):
    if data[i] == target:
      return i

  return -1

# Example usage
data = [17, 24, 8, 39, 12]
target = 39
found_index = linear_search(data, target)

if found_index != -1:
  print("Target", target, "found at index", found_index)
else:
  print("Target", target, "not found in the list")
