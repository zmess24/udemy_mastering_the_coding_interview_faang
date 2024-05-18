# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
def productSum(array, depth: int = 1):
    sum = 0
    # Iterate over array
    for element in array:
        sum += element if type(element) is int else productSum(element, depth+1)

    return depth * sum