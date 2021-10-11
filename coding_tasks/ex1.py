def count_connections(list1: list, list2: list) -> int:
    count = 0
    arr = dict()

    for i in list1:
        if i in arr:
            arr[i] = arr[i]+1
        else:
            arr[i] = 1

    for i in list2:
       if i in arr:
           count = count + arr[i]

    return count

