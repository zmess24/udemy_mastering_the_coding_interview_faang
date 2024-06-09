### <a href="https://leetcode.com/problems/valid-palindrome/description/">Valid Palindrome</a>

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring case sensitivity.

### Example

```
Input:
"A man, a plan, a canal: Panama" -> "amanaplanacanalpanama"

Output:
true
```

### Step 1. Constraint Questions:

Constraints are straightforward.

### Step 2. Test Cases:

```
Input:
"aabaa" -> "aabaa"

Output:
true
```

```
Input:
"aabbaa" -> "aabbaa"

Output:
true
```

```
Input:
"abc" => "cba"

Output:
false
```

```
Input:
""" -> ""

Output:
true
```

```
Input:
""" -> ""

Output:
true
```

```
Input:
"A man, a plan, a canal: Panama" -> "amanaplanacanalpanama"

Output:
true
```

### Step 3. Figure out a solution without code.

/[^A-Za-z0-9]/g

## Approaches.

-   **Brute force**: Try every possible solution until you find the correct answer.
    -   `O(N^2), O(N)`
-   ## **Sliding Window**:
    -   `O(N), O(N)`
