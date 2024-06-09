## (https://leetcode.com/problems/binary-tree-right-side-view/)[Binary Tree Right Side View]

Given a binary tree, imagine you're standing to thr gith of the tree. Return an array of the values of the nodes you can see ordered from top to bottom.

## Depth First Search

**Insights** 

1. Prioritize Right
2. Keep track of level of nodes

**Preorder**:

1. Node
2. Left
3. Right

**Inorder**:

1. Left
2. Node
3. Right

**Postorder**:

1. Left
2. Right
3. Node