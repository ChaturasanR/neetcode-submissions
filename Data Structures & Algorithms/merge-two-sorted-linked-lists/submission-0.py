# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1:
            return list2
        
        if not list2:
            return list1
        
        curr, temp1, temp2 = None, list1, list2
        if list1.val <= list2.val:
            head = list1
            temp1 = list1.next
        else:
            head = list2
            temp2 = list2.next

        curr = head
        while temp1 != None and temp2 != None:
            if temp1.val <= temp2.val:
                curr.next = temp1
                temp1 = temp1.next
            else:
                curr.next = temp2
                temp2 = temp2.next

            curr = curr.next

        if temp1 != None:
            curr.next = temp1
        
        if temp2 != None:
            curr.next = temp2
        
        return head