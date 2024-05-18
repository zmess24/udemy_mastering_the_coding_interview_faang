def firstDuplicateValue(array):
    hashMap = set()
    
    for num in array:
        if num in hashMap:
            return num
        else:
            hashMap.add(num)

    return -1
