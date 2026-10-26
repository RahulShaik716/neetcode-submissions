# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #naive 
        arr = []
        head1 = list1
        while head1:
            arr.append(head1.val)
            head1 = head1.next
        
        while list2:
            arr.append(list2.val)
            list2 = list2.next 

        arr.sort()

        merged = []
        dummy = ListNode(-1)
        curr = dummy 

        for i in arr:
            node = ListNode(i)
            curr.next = node 
            curr = node 
        
        return dummy.next
        