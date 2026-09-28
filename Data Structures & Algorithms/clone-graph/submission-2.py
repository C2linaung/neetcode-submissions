"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        clone = {node.val: Node(node.val)}
        q = deque([node])
        while q:
            curr_node = q.popleft()
            curr_clone = clone[curr_node.val]
            for nei in curr_node.neighbors:
                if nei.val not in clone:
                    q.append(nei)
                    clone[nei.val] = Node(nei.val)
                curr_clone.neighbors.append(clone[nei.val])
        return clone[node.val]