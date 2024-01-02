### <a href="https://leetcode.com/problems/valid-palindrome-ii/">Almost a Palindrome</a>

Given a string, determine if it is almost a palindrome. A string is almost a palindrome if it becomes a palindrome by removing 1 letter. Consider only alphanumeric characters and ignore case sensitiviy.

### Example

```
Input:
"race a car"

"racecar" - 1 removal, true
"racacar" - 1 removal, true

Output:
true
```

### Step 1. Constraint Questions:

-   Do we consider a palindrome an almost palidnrome? `Yes`

### Step 2. Test Cases:

```
Input:
"abccdba"

"abccba" - 1 removal, true
"abcdba" - 1 removal, false

Output:
true
```

```
Input:
"abcdefdba"

"abdeba" - 2 removals, false
"abddba" - 2 removals, false

Output:
false
```

### Step 3. Figure out a solution without code.

/[^A-Za-z0-9]/g

## Approaches.

-   **Brute force**: Try every possible solution until you find the correct answer.
    -   `O(N^2), O(N)`
-   ## **Sliding Window**:
    -   `O(N), O(N)`
