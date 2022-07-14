# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head
        itr, prev = head, head
        while itr:
            
            if itr.val == val:
                if itr == head:
                    head = itr.next
                    itr = head
                else:
                    prev.next = prev.next.next
                    itr = prev.next
            else:
                prev = itr
                itr = itr.next
        return head
                