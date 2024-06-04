def groupAnagrams(words):
    wordMap = {}
    
    for word in words:
        formatted_word = "".join(sorted(word))
        
        if formatted_word in wordMap:
            wordMap[formatted_word].append(word)
        else:
            wordMap[formatted_word] = [word]

    return list(wordMap.values())
        