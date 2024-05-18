# https://www.algoexpert.io/questions/move-element-to-end
def moveElementToEnd(array, toMove):
    left = 0
    right = len(array) - 1

    while left < right:
        # Iterate right index until not target number
        while left < right and array[right] == toMove: 
            right -= 1
        if array[left] == toMove:
            # Swap elements
            array[left], array[right] = array[right], array[left]
        left += 1

    return array
