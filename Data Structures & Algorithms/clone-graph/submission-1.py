"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return node
        q = deque([node])
        clones = {node.val: Node(node.val)}
        while q:
            curr_node = q.popleft()
            curr_clone = clones[curr_node.val]

            for n in curr_node.neighbors:
                if n.val not in clones: # not visited
                    q.append(n)
                    clones[n.val] = Node(n.val)
                curr_clone.neighbors.append(clones[n.val])
        return clones[node.val]
        