my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def search(your_list, iteam):
    your_list.sort()
    low = 0
    hight = len(your_list)-1
    while low <= hight:
        midle = (low + hight) // 2
        guess = your_list[midle]
        if guess == iteam:
            return guess
        elif guess > iteam:
            hight = midle - 1
        else:
            low = midle + 1
    return None

print(search(my_list, 7))
