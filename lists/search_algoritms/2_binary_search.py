# Works only with sorted list
# log(n2)

lst = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 600]

def binary_search(lst, item):
    start = 0
    end = len(lst)
    found = False

    while found == False and start <= end:
        middle = round((start + end) /2)
        if lst[middle] == item:
            return middle
        if lst[middle] > item:
            end = middle - 1
        else:
            start = middle + 1

    return -1



binary_search(lst, 600)
