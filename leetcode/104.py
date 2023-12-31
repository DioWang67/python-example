# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

if __name__ =='__main__':
	s = Solution()
	null=""
	root=[3,9,20,null,null,15,7]
	print(s.maxDepth(root))