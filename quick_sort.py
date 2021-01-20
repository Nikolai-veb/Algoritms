def quicksort(arry):
    if len(arry) < 2:
        return arry
    else:
        pivot = [0]
        less = [i for i in arry[1:] if i <= pivot]
        greater = [i for i in arry[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
