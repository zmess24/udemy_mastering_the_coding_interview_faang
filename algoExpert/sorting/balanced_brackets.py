def balancedBrackets(string):
    # Create stack to hold brackets
    stack = []
    # Brackets
    brackets = "([{}])"
    # Create bracket mapping
    map = { "}": "{", ")": "(", "]": "[" }
    # Iterate over string
    for char in string:
        if char not in brackets: continue
        # Check if current char is a closing bracket
        if char in map:
            # If it is, see if it matches last entry in the stack.
            if len(stack) > 0 and map[char] == stack[-1]:
                stack.pop()
            else:
                return False
            # If it does, remove last from stack and continue
        # Append to stack
        else:
            stack.append(char)

    # If stack is empty return True, else return False
    return True if len(stack) == 0 else False
