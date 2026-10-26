class Node:
    def __init__(self,key,val):
        self.key , self.val = key,val 
        self.prev = self.next = None
class LRUCache:
    #LRU is with linkedlist , access a key , we move it to the end of the list, remove the first element if the cache is full , add a new key at the end 
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left,self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right,self.left

    #implement two helpers one for insertion , one for removal 
    def remove(self, node):
        prev, nxt = node.prev, node.next 
        prev.next, nxt.prev = nxt,prev 
     
     #insert always happens at the end 
    def insert(self,node):
        prev,nxt = self.right.prev, self.right
        prev.next = nxt.prev = node 
        node.prev,node.next = prev, nxt

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
  

    def put(self, key: int, value: int) -> None:
        #insert if key is already in remove and insert update key node 
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])

        #if length of hashmap exceeds capacity then remove the left node 
        if len(self.cache) > self.capacity:
            lru = self.left.next 
            self.remove(lru)
            del self.cache[lru.key]
 
