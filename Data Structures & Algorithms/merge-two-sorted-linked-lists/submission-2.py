# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # #naive 
        # arr = []
        # head1 = list1
        # while head1:
        #     arr.append(head1.val)
        #     head1 = head1.next
        
        # while list2:
        #     arr.append(list2.val)
        #     list2 = list2.next 

        # arr.sort()

        # merged = []
        # dummy = ListNode(-1)
        # curr = dummy 

        # for i in arr:
        #     node = ListNode(i)
        #     curr.next = node 
        #     curr = node 
        
        # return dummy.next
        # #time - O(n+m *logn+m) + O(n+m), space - O(n+m)

        #using recursion 
        if list1 is None:
            return list2 
        if not list2:
            return list1

        
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next,list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1,list2.next)
            return list2
        
        