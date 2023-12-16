# log(n)

lst = [20, 30, 50, 10, 165, 1, 54]

def linear_search(lst, item):
    for i in range(len(lst)):
        if lst[i] == item:
            return i

    return -1

linear_search(lst, 10)
