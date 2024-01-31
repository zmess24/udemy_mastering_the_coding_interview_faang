### (https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/solutions/309013/find-starting-and-ending-in-two-binary-search/)[Start and End of a Sorted Array]

Given an array of integers sorted in ascending order, return the starting and ending index of a given target value in an array i.e [x,y]

Your solution should run in O(logN) time.

### Example

```
Input:
k = 5
a = [1, 3, 3, 5, 5, 5, 8, 9]

Output:
[3, 5]
```

### Step 1. Constraint Questions:

-   What do we return if the target is not found in the array? `Return -1`

### Step 2. Test Cases:

```
Input:
k = 5
a = [1, 3, 3, 5, 5, 5, 8, 9]

Output:
[3, 5]
```

```
Input:
k = 4
a = [1, 2, 3, 4, 5, 6]

Output:
[3,3]
```

```
Input:
k = 9
a = [1, 2, 3, 4, 5, 6]

Output:
[-1, -1]
```

```
Input:
k = 3
a = []

Output:
[-1, -1]
```

### When to use Binary Search

Say you wanted to determine the minimum square footage of office space needed to fit all a company's employees easily. Then, you can conduct a binary search for that suggested size rather than sequentially checking through all the possible dimensions. Typically, you would estimate maximum and minimum sizes when conducting the binary search, then check a middle value, so you can halve the interval repeatedly until you get your answer. This process saves a lot of time, especially when considering the vast number of possible iterations of office space square foot available!
