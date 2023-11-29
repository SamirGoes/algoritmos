list = list(range(0, 33))
item = 26


def search(list, item):
    floor = 0
    high = len(list) - 1

    while(floor <= high):
        middle = round((floor + high) / 2)
        test = list[middle]

        if(test == item):
            return middle
        if(test > item):
            high = middle - 1
        else:
            floor = middle + 1
    return None  


search(list, item)