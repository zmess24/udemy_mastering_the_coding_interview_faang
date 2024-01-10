### <a href="https://leetcode.com/problems/reverse-linked-list-ii/">Reverse Linked List 2</a>

Given a linked list and numbers `m` and `n`, return it back with only positions `m` to `n` in reverse.

### Example

```
Input:
1 -> 2 -> 3 -> 4 -> 5 -> null
m = 2
n = 4

Output:
1 -> 4 -> 3 -> 2 -> 5 -> null
```

### Step 1. Constraint Questions:

-   Is the positioning 0 or 1 index? `1 index`
-   Will `m` and `n` always be within the bounds of the linkedList? `Yes, assume 1 <= m <= n <= length of linked list`
-   Can we receive m and n values for the whole linked list? `Yes, we can receieve m = 1 and n = length of linked list`

### Step 2. Test Cases:

```
Input:
1 -> 2 -> 3 -> 4 -> 5 -> null
m = 1
n = 5

Output:
5 -> 4 -> 3 -> 2 -> 1 -> null
```

```
Input:
5 -> null
m = 1
n = 5

Output:
5 -> 4 -> 3 -> 2 -> 1 -> null
```

```

Input:
null
m = 0
n = 0

Output:
0

```

### Step 3. Figure out a solution without code.

**Steps to Reverse Linked List**

1. Get current node
2. Store next value
3. Update next value to list so far
4. Store current node as list so far
5. Update current node to stored next value (2)

Keep reference to m-1, m, n, and n+1

-   **m - 1**: is section head section we want to keep
-   **m**: Begin reversal
-   **n**: End reversal
-   **n+1**:
