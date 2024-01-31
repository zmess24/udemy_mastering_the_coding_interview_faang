def solution(pattern, source):
    matches = 0
    left = 0
    right = len(pattern) - 1
    
    while right < len(source):
        sub = source[left:right+1]
        passed = True
        for i in range(len(sub)):
            char = sub[i]
            p = pattern[i]
            
            if p == "0" and char in 'aeiouy':
                continue
            elif p == '1' and char not in 'aeiouy':
                continue
            else:
                passed = False
                break
            
        if passed:
            matches += 1
            
        left += 1
        right += 1
        
    return matches
    
    
    
