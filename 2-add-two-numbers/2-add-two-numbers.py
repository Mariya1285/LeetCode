# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        sum_l,head = None, None
        while l1 or l2 or carry!=0:
            
            if not l1:
                x = 0
            else:
                x = l1.val
                l1 = l1.next
                
            if not l2:
                y = 0
            else:
                y = l2.val
                l2 = l2.next
                
            temp = (x+y+carry)%10
            carry = (x+y+carry)//10
            
            if sum_l:
                sum_l.next = ListNode(temp)
                sum_l = sum_l.next
            else:
                sum_l = ListNode(temp)
                head = sum_l
                
        return head