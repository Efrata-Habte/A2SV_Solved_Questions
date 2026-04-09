# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        curr = head

        while curr:
            stack.append(curr.val)
            curr = curr.next

        stack.sort() 

        cur = head
        i = 0
        while cur:
            cur.val = stack[i]
            cur = cur.next
            i+=1

        return head