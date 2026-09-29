# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        queue = deque([root])
        res = []
        while queue:  
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    res.append(str(node.val))
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    res.append('N')
               
        print(res)
        return ",".join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        if vals[0]=="N":
            return None
        n = len(vals)
        i = 1
        root = TreeNode(int(vals[0]))
        queue = deque([root])
        while queue:
            node = queue.popleft() 
            if i<len(vals) and vals[i]!="N":
                node.left = TreeNode(int(vals[i]))
                queue.append(node.left)
            i+=1
            if i<len(vals) and vals[i]!="N":
                node.right = TreeNode(int(vals[i]))
                queue.append(node.right)
            i+=1
        return root


