def insertion_sort(data):
    """Sorts a list of data in ascending order using the insertion sort algorithm."""

    for i in range(1, len(data)):
        current_value = data[i]
        j = i - 1

        # Move elements greater than current_value one position ahead
        while j >= 0 and data[j] > current_value:
            data[j + 1] = data[j]
            j -= 1

        # Insert current_value at its correct position
        data[j + 1] = current_value

    return data

# Example usage
unsorted_data = [54, 26, 93, 17, 77, 31, 44, 55, 20]
sorted_data = insertion_sort(unsorted_data)
print("Unsorted:", unsorted_data)
print("Sorted:", sorted_data)
