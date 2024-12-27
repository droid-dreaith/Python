#write a python program to find the second largest number in a list

def find_SecondLargest(arr):
    # Ensure the list has at least two unique elements
    if len(arr) < 2:
        return None

    # Remove duplicates by converting to a set, then back to a list
    unique_arr = list(set(arr))

    # Sort the unique list
    unique_arr.sort()

    # Return the second largest element
    return unique_arr[-2]
print(find_SecondLargest([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print("The second largest number in the list is: ",(find_SecondLargest))