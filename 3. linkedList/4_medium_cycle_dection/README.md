### <a href="https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/">Merge Multi-level Doubly Linked Lists</a>

Given a doubly linked list, list nodes also have a child property that can point to a seperate doubly linked list. These child lists can also have one or more child doubly linked lists of their own, and so on.

Return the list as a single level flattened doubly linked list.

Node Properities:

```js
function Node (val, prev, next, child) {
    this.val = val;
    this.prev = prev
    this.next = next
    this.child = child
}

```

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

1. Get current node and store in `current_node` variable.
2. Check if current node has a child property.
    1. If it does, navigate to child node.
    2. If 
4. If it doesn't, check for next property and navigate to next node.
5. 
5. Update current node to stored next value (2)

Keep reference to m-1, m, n, and n+1

-   **m - 1**: is section head section we want to keep
-   **m**: Begin reversal
-   **n**: End reversal
-   **n+1**:
