### <a href="https://leetcode.com/problems/container-with-most-water/">Container with Most Water</a>

You are given an arry of positive integers where each integer represents the height of a vetical line on a chart. Find two lines which together with the x-axis forms a container that would hold the greatest amount of water. Return the area of water it would hold.

### Example

Input:
[1,8,6,2,9,4] (array)

Output:
`8 * 3 = 24`

### Step 1. Constraint Questions:

-   Does the thickness of the lines affect the area? `No`
-   Do the left and right sides of the graph count as walls? `No, the sides cannot be used to form a container`
-   Does a higher line inside our container affect our area? `No, lines inside our container don't affect the area`

### Step 2. Test Cases:

```
Input:
[7,1,2,3,9] (array)

Length = 7
Width = 4 (Index 4 - Index 0)

Output:
28
```

```
Input:
[0] (array)

Output:
0
```

```
Input:
[7] (array)

Length = 7

Output:
0
```

```
Input:
[6,9,3,4,5,8] (array)
t = 5 (target)

6 * 5 = 30
8 * 4 = 32

Output:
32
```

### Step 3. Figure out a solution without code.

## Approaches.

-   **Brute force**: Try every possible solution until you find the correct answer.
    -   `O(N^2), S(1)`
-   ## **Optimized** : Shifting Pointers Technique
