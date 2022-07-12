# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        try:
            fast_pointer,slow_pointer = head.next.next, head
            while fast_pointer.next and slow_pointer.next:
                
                if fast_pointer == slow_pointer:
                    return True
                else:
                    fast_pointer = fast_pointer.next.next
                    slow_pointer = slow_pointer.next
            return False
        except:
            return False