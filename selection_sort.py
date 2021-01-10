
def find_smallest(arry):
    smallest = arry[0]
    smallest_index = 0
    for i in range(1, len(arry)):
        if arry[i] < smallest:
            smallest = arry[i]
            smallest_index = i
        return smallest

def selection_sort(arry):
    new_arry = []
    for i in range(len(arry)):
        smallest = find_smallest(arry)
        new_arry.append(arry.pop(smallest))
    return new_arry

