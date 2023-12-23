# Write recursive function which sum's list

arr = [1, 5, 6]

def sum_recursive(arr):
    if not arr:
        return 0
    return arr.pop(0) + sum_recursive(arr)

sum_recursive(arr)
