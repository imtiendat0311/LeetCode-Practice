# Runtime: 918 ms, faster than 88.43% of Python3 online submissions for LRU Cache.
# Memory Usage: 76.6 MB, less than 22.95% of Python3 online submissions for LRU Cache.

class Node:
    def __init__(self,key: int,val:int):
        self.key=key
        self.val=val
        self.right=None
        self.left=None
        
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left=Node(0,0)
        self.right=Node(0,0)
        self.left.right = self.right
        self.right.left = self.left
    def insert(self,node):
        prev = self.right.left 
        self.right.left = node
        node.right = self.right
        node.left = prev
        prev.right = node
    def remove(self,node):
        if node.left and node.right is not None:
            node.left.right = node.right
            node.right.left = node.left
        if node.left is None:
            node.right.left = None
        if node.right is None:
            node.left.right = None
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key]=Node(key,value)
        self.insert(self.cache[key])
        if len(self.cache)>self.capacity:
            lru = self.left.right
            self.remove(lru)
            del self.cache[lru.key]
            
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)