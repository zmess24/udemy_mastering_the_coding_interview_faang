### <a href="https://leetcode.com/problems/valid-parentheses/solutions/1406241/python-solution-with-and-without-using-stack/">Valid Parentheses</a>

Given a string containing only parentheses, determine if it is valid. The string is valid if all parentheses close.

### Example

```
Input:
"{([])}"

Output:
true
```

### Step 1. Constraint Questions:

-   Does an empty string count as valid? `Yes`

### Step 2. Test Cases:

```
Input:
"{([])]"

Output:
false
```

```
Input:
"{([)]}"

Output:
false
```

```
Input:
"[{{}}]"

Output:
true
```

```
Input:
"{[]()}"

Output:
true
```

### Step 3. Figure out a solution without code.

## Approaches.

-   **Recursion**: Try every possible solution until you find the correct answer.
