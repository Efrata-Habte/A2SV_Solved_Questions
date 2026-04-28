# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        # Use BFS traversal
        target = root.val
        q = deque()
        q.append(root)

        while q:
            front = q.popleft()
            if front.val != target:
                return False

            if front.left:
                q.append(front.left)
            if front.right:
                q.append(front.right)
        
        return True

        