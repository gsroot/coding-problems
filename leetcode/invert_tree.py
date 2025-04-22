# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        current = root
        visited = {root}
        roots = []
        while current:
            current.left, current.right = current.right, current.left
            if current.left and current.left not in visited:
                roots.append(current)
                current = current.left
                visited.add(current)
            elif current.right and current.left not in visited:
                roots.append(current)
                current = current.right
                visited.add(current)
            else:
                current = roots.pop(-1)
                if current == root:
                    break
        return root
