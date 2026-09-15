# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #pre-order i = root , 2i+1 = left, 2i+2 = right 
        inorder_map = {}
        for i,val in enumerate(inorder):
            inorder_map[val] = i 
        pre_order_index = 0 
        def dfs(left,right):
            nonlocal pre_order_index
            if left > right:
                return None 
            
            root_value = preorder[pre_order_index]
            pre_order_index+=1

            root = TreeNode(root_value)

            mid = inorder_map[root_value]

            root.left = dfs(left,mid-1)
            root.right = dfs(mid+1,right)

            return root 
        return dfs(0,len(preorder)-1)
