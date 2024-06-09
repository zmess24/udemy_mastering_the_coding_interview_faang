### <a href="https://leetcode.com/problems/longest-substring-without-repeating-characters/">Longest Substring Without Repeating Characters</a>

Given a string, find the length of the longest substring without repeating characters

### Example

```
Input:
"abccabb" -> "abc", "cab"

Output:
"3"
```

### Step 1. Constraint Questions:

-   Can substrings overlap? `Yes`

### Step 2. Test Cases:

```
Input:
"abccabb" -> "abc", "cab"

Output:
3
```

```
Input:
"cccccc" -> "c"

Output:
1
```

```
Input:
""

Output:
0
```

```
Input:
"abcbda" -> "cbda"

Output:
4
```

### Step 3. Figure out a solution without code.

## Approaches.

-   **Brute force**: Try every possible solution until you find the correct answer.
    -   `O(N^2), O(N)`
-   ## **Sliding Window**:
    -   `O(N), O(N)`
