class Node:
    def __init__(self, key=0, val=0):
        self.key, self.val = key, val
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = dict() # key : node of key containing val
        self.left, self.right = Node(), Node()
        self.left.next = self.right
        self.right.prev = self.left
    
    def remove_node(self, node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev
    
    def insert_node(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt
        
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove_node(self.cache[key])
            self.insert_node(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove_node(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert_node(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.cache.pop(lru.key)
            self.remove_node(lru)

