def quicksort(data, low=0, high=None):

  if high is None:
    high = len(data) - 1
  # Base case: If list has 0 or 1 element, it's already sorted
  if low < high:
    # Choose a pivot element (here, the last element)

    pivot_index = partition(data, low, high)
    # Recursively sort the left and right sub-arrays
    quicksort(data, low, pivot_index - 1)
    quicksort(data, pivot_index + 1, high)

  return data

def partition(data, low, high):

  pivot = data[high]
  i = low - 1  # Index for elements less than pivot

  # Partition the list
  for j in range(low, high):
    if data[j] <= pivot:
      i += 1
      data[i], data[j] = data[j], data[i]

  # Put the pivot element in its final position
  data[i + 1], data[high] = data[high], data[i + 1]

  return i + 1  # Return the final index of the pivot

# Example usage
unsorted_data = [85, 24, 63, 42, 17, 98, 59, 31]
sorted_data = quicksort(unsorted_data.copy())
print("Unsorted:", unsorted_data)
print("Sorted:", sorted_data)
