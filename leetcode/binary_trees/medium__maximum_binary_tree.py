# https://leetcode.com/problems/maximum-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0: return

        index, val = nums.index(max(nums)), max(nums)
        prefix, suffix = nums[:index], nums[index+1:]
        node = TreeNode(val=val)

        if len(prefix): node.left = self.constructMaximumBinaryTree(prefix)
        if len(suffix): node.right = self.constructMaximumBinaryTree(suffix)  
        
        return node