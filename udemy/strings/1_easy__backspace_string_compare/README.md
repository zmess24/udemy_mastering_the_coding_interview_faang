### <a href="https://leetcode.com/problems/backspace-string-compare/">Backspace String Compare</a>

Given two strings S and T, return if they are equal when both are typed out. Any '#' that appears in the string counts as a backspace.

### Example

```
Input:
"cb#d "

Output:
"cd"
```

```
Input:
"cb#d"

Output:
"cd"
```

```
Input:
"ab#z"

Output:
"az"
```

```
Input:
"ab##"

Output:
""
```

```
Input:
"a###b"

Output:
"b"
```

### Step 1. Constraint Questions:

-   Are two empty strings equal to other? `Yes`
-   Does case sensitivity matter? `Yes it does, 'a' does not equal 'A'.`

### Step 2. Test Cases:

```
Input:

S: "ab#z" => "az"
T: "az#z" => "az"

Output:

True
```

```
Input:

S: "abc#d" => "abd"
T: "acc#c" => "acc"

Output:

False
```

```
Input:

S: "x#y#z#" => ""
T: "a#" => ""

Output:

True
```

```
Input:

S: "a###b" => "b"
T: "b" => "b"

Output:

True
```

```
Input:

S: "Ab#z" => "Az"
T: "ab#z" => "az"

Output:

False
```

### Step 3. Figure out a solution without code.

```
Input:

S: "ab#z" => "az"
T: "az#z" => "az"

Output:

False
```

Logic:

```
newS = []
newT = []

for (let i = 0; i < S.length: i++) {
    if (currentChar === "#") {
        newS.pop()
    } else {
        newS.push(currentChar)
    }
}

for (let i = 0; i < T.length: i++) {
    if (currentChar === "#") {
        newT.pop()
    } else {
        newT.push(currentChar)
    }
}

newS = newS.join('')
newT = newT.join('')

return newS === newT ? true : false

```

## Approaches.

-   **Brute force**: Try every possible solution until you find the correct answer.
    -   `O(N^2), S(1)`
-   ## **Optimized** : Shifting Pointers Technique
