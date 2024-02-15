def runLengthEncoding(string):
    compressed = ""
    window = 0
    n = len(string)

    for i in range(n):
        if i == n - 1:
            if string[i-1] == string[i]:
                window += 1
                compressed += str(window) + string[i]
            else:
                compressed += str(window) + string[i-1] + str(1) + string[i]
        elif i == 0 or window == 0:
            window += 1
        elif string[i-1] == string[i]:
            window += 1

            if window == 9:
                compressed += str(window) + string[i]
                window = 0
        else:
            compressed += str(window) + string[i-1]
            window = 1

        
    return compressed

    
                
