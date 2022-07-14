# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        odd, even = head, head.next
        connecting_point = even
        while odd.next and even.next:
            try:
                odd.next = odd.next.next
                odd = odd.next
            except:
                pass
            try:
                even.next = even.next.next
                even = even.next
            except:
                pass

        odd.next = connecting_point
        return head
        