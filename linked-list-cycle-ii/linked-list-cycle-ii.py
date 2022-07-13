# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        try:
            fast_pointer,slow_pointer = head.next.next, head.next
            while fast_pointer and fast_pointer.next and slow_pointer: 
                if fast_pointer == slow_pointer:
                    slow_pointer = head
                    while slow_pointer != fast_pointer:
                        slow_pointer = slow_pointer.next
                        fast_pointer = fast_pointer.next
                    return slow_pointer
                else:
                    fast_pointer = fast_pointer.next.next
                    slow_pointer = slow_pointer.next
            # return -1
        except:
            # return -1
            pass