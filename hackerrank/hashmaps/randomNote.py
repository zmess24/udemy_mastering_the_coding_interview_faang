def checkMagazine(magazine, note):
    hashMap = {}
    
    for word in note:
        if word in hashMap:
            hashMap[word] += 1
        else:
            hashMap[word] = 1
    
    for word in magazine:
        if word in hashMap:
            hashMap[word] -= 1
            
            if hashMap[word] == 0:
                del hashMap[word]
    
    ans = "Yes" if len(hashMap) == 0 else "No"
    print(ans)