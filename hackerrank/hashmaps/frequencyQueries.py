def freqQuery(queries):
    hashMap = {}
    outputs = []
    for operation, target in queries:
        if operation == 1:
            if target in hashMap:
                hashMap[target] += 1
            else:
                hashMap[target] = 1
        elif operation == 2:
            if target in hashMap:
                hashMap[target] -= 1
                if hashMap[target] == 0:
                    del hashMap[target]
        elif operation == 3:
            if target in hashMap.values():
                outputs.append(1)
            else:
                outputs.append(0)
    
    return outputs