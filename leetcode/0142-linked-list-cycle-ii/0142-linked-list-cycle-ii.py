# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        cycle = False

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                cycle = True
                break
        
        if cycle:
            slow = head

        while slow != fast and cycle:
            slow = slow.next
            fast = fast.next

        return slow if cycle else None 
        
