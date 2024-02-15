def semordnilap(words):
    ans = []
    hashMap = {}

    for word in words:
        if word not in hashMap:
            reversed = word[::-1]
            hashMap[reversed] = word
        else:
            ans.append([hashMap[word], word])
    
    return ans