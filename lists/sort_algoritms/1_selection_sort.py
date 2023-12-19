# n^2

lst = [1, 5, 10, 15, 20, 60, -5, 0, -1, 1, 515, 919, 2045, 13, -125, -20, -15]

def find_smallest(lst):
    smallest = lst[0]
    index = 0
    for i in range(1, len(lst)):
        if lst[i] < smallest:
            smallest = lst[i]
            index = i
    return index

def selection_sort(lst):
    sortedLst = []
    for i in range(len(lst)):
        smallest = find_smallest(lst)
        sortedLst.append(lst.pop(smallest))

    return sortedLst


print(selection_sort(lst))

