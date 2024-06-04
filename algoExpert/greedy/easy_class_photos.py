def classPhotos(redShirtHeights, blueShirtHeights):
    # Define N as the length of redShirtHeights
    n = len(redShirtHeights)
    # Sort blue and red shirt lists by ascending heights
    red, blue = sorted(redShirtHeights), sorted(blueShirtHeights)
    # if heights are the same at index 0, return False
    if red[0] == blue[0]: return False

    # assign backRow to red if "red" is greater than "blue" else "blue"
    backRow = red if red[0] > blue[0] else blue
    # assign frontRow to "red" if red is less than "blue" else "red"
    frontRow = red if red[0] < blue[0] else blue
    # Iterate through n
    for i in range(1, n):
        # If heights are the same or frontRow > backRow: Retur, return False
        if frontRow[i] == backRow[i] or frontRow[i] > backRow[i]: return False
        
    return True
