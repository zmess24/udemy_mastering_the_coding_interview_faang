### Question

Given an array of integers, return the indicies of the two numbers that add up to a given target.

### Example

Input:
[1,3,7,9,2] (array)
11 (target)

Output:
[3, 4]

### Step 1. Constraint Questions:

-   Are all the numbers positive or can there be negatives? (Positive)
-   Can there be duplicate numbers? (No duplicates)
-   Will there always be a solution available? (No, there may not always be a solution)
-   What do we return if there is no solution? (Return Null)
-   Can there be multiple pairs that add up to the target? (Only 1 pair)

### Step 2. Test Cases:

```
Input:
[1,3,7,9,2] (array)
t = 11 (target)

Output:
[3, 4]
```

```
Input:
[1,3,7,9,2] (array)
t = 25 (target)

Output:
null
```

```
Input:
[] (array)
t = 1 (target)

Output:
null
```

```
Input:
[5] (array)
t = 5 (target)

Output:
null
```

```
Input:
[1, 6] (array)
t = 7 (target)

Output:
[0, 1]
```

### Step 3. Figure out a solution without code.

## Approaches.

-   **Brute force**: Try every possible solution until you find the correct answer.
-   **Optimized**:
