# n * log(n)

lst = [1, 5, 4, 15, 20, -5, -10, -15, 0]

def quick_sort(lst):
    if len(lst) < 2:
        return lst
    
    pivot = lst[0]
    less = [i for i in lst if i < pivot]
    greater = [i for i in lst if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)

print(quick_sort(lst))
