def hasSingleCycle(array):
    # Implement DFS
    # Create a set to store all seen indicies
    seen = set()
    # Create pointer
    pointer = 0
    # Answer
    isSingleCycle = False
    # Use while loop to iterate through array
    while True:
        # If current index not in the seen set
        if pointer not in seen:
            # Add current index to seen set
            seen.add(pointer)
            # Assign current pointer = the value of the current index % array length
            pointer = (pointer + array[pointer]) % len(array)
            
            # If the set length = array length, break and True
            if len(seen) == len(array) and pointer == 0:
                isSingleCycle = True
                break
            
        # If current index in the seen set
        else:
            # Break and return False
            break

    return isSingleCycle
            
    
