# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        count = 0
        arr = []

        curr_node = head
        while curr_node is not None:
            count += 1
            arr.append(curr_node.val)
            curr_node = curr_node.next
        
        return arr == arr[::-1]
            
