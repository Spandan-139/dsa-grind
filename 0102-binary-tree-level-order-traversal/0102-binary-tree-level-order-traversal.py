from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        result = []
        queue = deque()
        queue.append(root)  # start with root
        
        while queue:
            level = []                    # stores current level's values
            size = len(queue)             # how many nodes are in this level
            
            for i in range(size):
                node = queue.popleft()    # take from front
                level.append(node.val)    # add value to current level
                
                if node.left:
                    queue.append(node.left)   # add left child for next level
                if node.right:
                    queue.append(node.right)      # add right child for next level
            
            result.append(level)          # add this level to result
        
        return result