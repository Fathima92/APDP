def binary_search(data, target, low=0, high=None):
  """Searches for a target value in a sorted list using binary search.

  Args:
      data: A sorted list of items.
      target: The value to search for.
      low: The starting index for the search (defaults to 0).
      high: The ending index for the search (defaults to None, meaning the entire list).

  Returns:
      The index of the target element if found, otherwise -1.
  """

  if high is None:
    high = len(data) - 1

  # Base case: If list is empty or target is not within the search range
  if low > high:
    return -1

  # Find the middle index
  mid = (low + high) // 2

  # Check if target is at the middle index
  if data[mid] == target:
    return mid

  # If target is less than the middle element, search in the left half
  elif data[mid] > target:
    return binary_search(data, target, low, mid - 1)

  # If target is greater than the middle element, search in the right half
  else:
    return binary_search(data, target, mid + 1, high)

# Example usage
sorted_data = [12, 34, 56, 78, 90]
target = 56
found_index = binary_search(sorted_data, target)

if found_index != -1:
  print("Target", target, "found at index", found_index)
else:
  print("Target", target, "not found in the list")
