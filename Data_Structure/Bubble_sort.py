def bubble_sort(data):
  """Sorts a list of data in ascending order using bubble sort algorithm.

  Args:
      data: A list of sortable items.

  Returns:
      The sorted list.
  """

  # Loop through all elements of the list n-1 times
  for i in range(len(data) - 1):
    # Flag to track if any swaps occurred during the pass
    swapped = False
    # Inner loop to compare adjacent elements
    for j in range(len(data) - i - 1):
      # Compare elements and swap if they are in the wrong order
      if data[j] > data[j + 1]:
        data[j], data[j + 1] = data[j + 1], data[j]
        swapped = True
    # If no swaps occurred in a pass, the list is already sorted
    if not swapped:
      break

  return data

# Example usage
unsorted_data = [64, 34, 25, 12, 22, 11, 90]
sorted_data = bubble_sort(unsorted_data.copy())  # Avoid modifying the original list
print("Unsorted:", unsorted_data)
print("Sorted:", sorted_data)
