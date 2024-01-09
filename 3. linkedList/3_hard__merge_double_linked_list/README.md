### <a href="https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/">Merge Multi-level Doubly Linked Lists</a>

Given a doubly linked list, list nodes also have a child property that can point to a seperate doubly linked list. These child lists can also have one or more child doubly linked lists of their own, and so on.

Return the list as a single level flattened doubly linked list.

### Step 1. Constraint Questions:

-   Can every doublly linked list have mulitple child list nodes? `Yes, every list node can have multiple levels of children`
-   What do we do with child properities after flattening? `Just set the child property to null`

### Step 2. Test Cases:

```
Input:
1 -> 2 -> 3 -> 4 -> 5 -> 6
     7 -> 8 -> 9    12 -> 123
          10 -> 11

Output:
1 -> 2 -> 7 -> 8 -> 10 -> 11 -> 9 -> 3 -> 4 -> 5 -> 12 -> 13 -> 6
```

```
Input:
null

Output:
null
```

```
Input:
3

Output:
3
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
