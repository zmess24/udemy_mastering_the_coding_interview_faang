def nearlySimilarRectangles(sides):
    hashMap = {}
    ans = 0
    
    for side in sides:
        ratio = side[0] / side[1]
        if ratio in hashMap:
            hashMap[ratio] += 1
        else:
            hashMap[ratio] = 1
    
    for frequency in hashMap.values():
        if frequency > 1:
            ans += round(frequency * (frequency -1) / 2)
            
    return ans