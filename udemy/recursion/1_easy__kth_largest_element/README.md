### <a href="https://leetcode.com/problems/valid-parentheses/solutions/1406241/python-solution-with-and-without-using-stack/">Valid Parentheses</a>

Given an unsorted array, return the kth largest element. It is the kth largest element in sorted order, not the kth distinct element.

### Example

```
Input:
k = 2
a = [5,3,1,6,4,2]

Output:
5
```

### Step 1. Constraint Questions:

-   Can we get an array where `k` is larger than the array length? `No, assume the answer is always available`

### Step 2. Test Cases:

```
Input:
k = 2
a = [5,3,1,6,4,2]

Output:
5
```

```
Input:
k = 4
a = [2,3,1,2,4,2]

Output:
2
```

```
Input:
k = 1
a = [3]

Output:
3
```
