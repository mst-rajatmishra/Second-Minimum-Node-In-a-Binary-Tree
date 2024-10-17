# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        unique_values = set()
        
        # Helper function for DFS traversal
        def dfs(node):
            if not node:
                return
            unique_values.add(node.val)
            dfs(node.left)
            dfs(node.right)
        
        # Start DFS from the root
        dfs(root)
        
        # Convert set to sorted list
        unique_values = sorted(unique_values)
        
        # Check for second minimum value
        if len(unique_values) > 1:
            return unique_values[1]
        return -1

# Example usage
# Constructing the binary tree [2,2,5,null,null,5,7]
root = TreeNode(2)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)

solution = Solution()
print(solution.findSecondMinimumValue(root))  # Output: 5

# Constructing the binary tree [2,2,2]
root2 = TreeNode(2)
root2.left = TreeNode(2)
root2.right = TreeNode(2)

print(solution.findSecondMinimumValue(root2))  # Output: -1

