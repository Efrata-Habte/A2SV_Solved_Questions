# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        stack = []

        while curr:

            while stack and stack[-1] < curr.val:
                stack.pop()
            
            stack.append(curr.val)
            curr = curr.next
        
        curr = head
        i=0

        while curr:
            if curr.val != stack[i]:
                curr = curr.next
                continue
            
            if i==0:
                head = curr
                temp = head
                curr=curr.next
                i+=1
            
            elif i < len(stack) and curr.val == stack[i]:
                temp.next = curr
                temp = temp.next
                curr = curr.next
                i+=1
            
        return head

            


