# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        current = head
        seq = []

        while current:
            seq.append(current.val)
            current = current.next
        
        return self.checkPalindrome(seq)
    
    def checkPalindrome(self, seq):
        left, right = 0, len(seq) - 1

        while left < right:
            if (seq[left] != seq[right]):
                return False
        
            left += 1
            right -= 1
        
        return True