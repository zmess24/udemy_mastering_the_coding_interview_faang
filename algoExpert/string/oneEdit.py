# ZAC SOLUTION
def oneEdit(stringOne, stringTwo):
    # Base Cases
    if stringOne == stringTwo: return True
    if abs(len(stringOne) - len(stringTwo)) > 1: return False

    oneSorted = sorted(stringOne)
    twoSorted = sorted(stringTwo)
    editsLeft = 1
    
    if len(twoSorted) == len(oneSorted):
        for i in range(len(oneSorted)):
            if oneSorted[i] != twoSorted[i] and editsLeft > 0:
                editsLeft -= 1
            elif oneSorted[i] != twoSorted[i] and editsLeft == 0:
                return False

        return True
    else:
        shortest = oneSorted if len(oneSorted) < len(twoSorted) else twoSorted
        longest = twoSorted if len(oneSorted) < len(twoSorted) else oneSorted
        for i in range(len(shortest)):
            if shortest[i] in longest:
                index = longest.index(shortest[i])
                longest.pop(index)

        if len(longest) > 1: return False

    return True
