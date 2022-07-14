# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        prev = None
        while head and temp.next:
            prev = temp
            temp = temp.next
            prev.next = prev.next.next
            temp.next = head
            head = temp
            temp = prev
        return head