### <a href="https://leetcode.com/problems/valid-parentheses/solutions/1406241/python-solution-with-and-without-using-stack/">Minimum Brackets to Remove</a>

Given a string only containing round brackets `(` and `)` and lowercase characters, remove the least amount of brackets so the string is valid.

A string is considered valid if it is empty or if there are brackets, they all close.

### Example

```
Input:
"a(bc(d)"

Output:
1
```

### Step 1. Constraint Questions:

-   What do we return from our algorithm? `Return a valid string with the fewest brackets removed`.

-   Will there be spaces in the string? `No, the string only contains lowercase characters (and brackets)`

-   Is a string containing only lowercase characters valid? `Yes, you don't need any brackets for a string to valid.`

### Step 2. Test Cases:

```
Input:
"a(bc(d)"

Output:
"abc(d)
```

```
Input:
"))(("

Output:
""
```

```
Input:
"(ab(c)d"

Output:
"ab(c)d" OR "(abc)d"
```

### Step 3. Figure out a solution without code.

## Approaches.

-   **Recursion**: Try every possible solution until you find the correct answer.
