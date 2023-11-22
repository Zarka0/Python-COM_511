def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index of the target if found
    return -1  # Return -1 if the target is not in the list

def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2  # Find the middle index

        if arr[mid] == target:
            return mid  # Return the index if the target is found
        elif arr[mid] < target:
            left = mid + 1  # Adjust the left boundary
        else:
            right = mid - 1  # Adjust the right boundary

    return -1  # Return -1 if the target is not in the list

# Example list
my_list = [1, 3, 5, 7, 9, 11, 13]

# Example target value
target = 7

# Choose which search method to use (linear or binary)
method = input("Enter 'linear' or 'binary' to choose a search method: ")

if method == 'linear':
    result = linear_search(my_list, target)
    search_method = "Linear Search"
elif method == 'binary':
    result = binary_search(my_list, target)
    search_method = "Binary Search"
else:
    print("Invalid search method entered.")
    result = -1

if result != -1:
    print(f"{search_method}: Element {target} found at index {result}")
else:
    print(f"{search_method}: Element {target} not found in the list"