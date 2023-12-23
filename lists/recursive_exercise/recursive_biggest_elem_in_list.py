# Find the biggest element in list

lst = [2, 5, -1, 0, 559, 69]


def recursive_biggest_element(lst):
    if len(lst) == 2:
        return lst[0] if lst[0] > lst[1] else lst[1]
    sub_max = recursive_biggest_element(lst[1:])
    return lst[0] if lst[0] > sub_max else sub_max

        
print(recursive_biggest_element(lst))
