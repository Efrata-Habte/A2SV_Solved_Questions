# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        right = head
        left = head
        cont = []

        while right:
            cont.append(right.val)
            right = right.next

        n = len(cont)
        idx = n - 1
        while left:
            left.val = cont[idx]
            left = left.next
            idx -= 1

        return head
