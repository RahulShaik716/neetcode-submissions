"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToNew = {}

        curr = head 
        while curr:
            node = Node(curr.val)
            oldToNew[curr] = node 
            curr = curr.next 
        
        
        curr = head 

        while curr:
            node = oldToNew[curr]

            node.next = oldToNew.get(curr.next)
            node.random = oldToNew.get(curr.random)

            curr = curr.next 
        
        return oldToNew.get(head)
            
        