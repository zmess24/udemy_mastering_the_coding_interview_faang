def reverseWordsInString(string):
    if len(string) == 1 or len(string) == 0: return string
    
    # Init sliding window
    ans = []
    left = 0

    for right in range(0, len(string)):
        # If left is not space and right is space, insert the word into the front of the list
        if string[left] != " " and string[right] == " ":
            ans.insert(0, string[left:right])
            left = right
        # If left is space and right is not space, insert the word into the front of the list
        elif string[left] == " " and string[right] != " ":
            ans.insert(0, string[left:right])
            left = right
        
    ans.insert(0, string[left:right+1])
    return "".join(ans)

    
