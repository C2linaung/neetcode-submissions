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
            clone_node = clone[curr_node.val]
            for n in curr_node.neighbors:
                if n.val not in clone:
                    q.append(n)
                    clone[n.val] = Node(n.val)
                clone_node.neighbors.append(clone[n.val])
        return clone[node.val]
