def twoStrings(s1, s2):
    if s1 == "" and s2 == "": 
        return "YES"
    
    hashMap = {}
    
    for char in s1:
        if char in hashMap:
            hashMap[char] += 1
        else:
            hashMap[char] = 1
    
    for char in s2:
        if char in hashMap:
            return "YES"
    
    return "NO"