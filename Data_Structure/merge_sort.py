def merge_sort(data):

  # Base case: If list has 0 or 1 element, it's already sorted
  if len(data) <= 1:
    return data

  # Divide the list into two halves
  mid = len(data) // 2
  left_half = data[:mid]
  right_half = data[mid:]

  # Sort the two halves recursively
  left_sorted = merge_sort(left_half)
  right_sorted = merge_sort(right_half)

  # Merge the sorted halves back together
  return merge(left_sorted, right_sorted)

def merge(left, right):
  """Merges two sorted lists into a single sorted list."""

  merged_list = []
  i = 0  # Index for left list
  j = 0  # Index for right list

  # Compare elements from both lists and add the smaller one to the merged list
  while i < len(left) and j < len(right):
    if left[i] <= right[j]:
      merged_list.append(left[i])
      i += 1
    else:
      merged_list.append(right[j])
      j += 1

  # Add any remaining elements from either list
  merged_list.extend(left[i:])
  merged_list.extend(right[j:])

  return merged_list

# Example usage
unsorted_data = [64, 34, 25, 12, 22, 11, 90]
sorted_data = merge_sort(unsorted_data)
print("Unsorted:", unsorted_data)
print("Sorted:", sorted_data)
