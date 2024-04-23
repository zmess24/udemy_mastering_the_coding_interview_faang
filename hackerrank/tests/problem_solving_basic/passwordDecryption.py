def decryptPassword(s):
    p = 0
    arr = list(s)
    
    while p < len(arr):
        index = len(arr) - p - 1
        if arr[index] == "0":
            arr[index] = arr[0]
            arr.pop(0)
            p += 1
        elif arr[index] == "*":
            temp = arr[index-2]
            arr[index-2] = arr[index-1]
            arr[index-1] = temp
            arr.pop(index)
            p += 2
        else:
            p += 1
        
    return "".join(arr)