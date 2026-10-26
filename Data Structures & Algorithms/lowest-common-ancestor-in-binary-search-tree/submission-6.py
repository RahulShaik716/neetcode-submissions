# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # all node values are unique , 
        # two nodes , output : return lca ,  node which has both p and q are descendants of that node. 

        # # if it's a bst then root > leftsubtree and root < rightsubtree
        # if not root or not p or not q:
        #     return
       
        # if max(p.val,q.val) < root.val:
        #     return self.lowestCommonAncestor(root.left,p,q)
        # elif min(p.val,q.val) > root.val:
        #     return self.lowestCommonAncestor(root.right,p,q)
        # else:
        #     return root
        

        #time O(h) , space O(h)


        curr = root 

        while True:
            if max(p.val,q.val) < curr.val:
                curr = curr.left
            elif min(p.val,q.val) > curr.val:
                curr = curr.right
            else:
                return curr