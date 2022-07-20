# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2:
            if not list1:
                return list2
            elif not list2:
                return list1
            else:
                return ListNode()
        else:
            # new_head = ListNode()
            # head = new_head
            head = None
            first_node = None
            while list1 and list2:
                ### do merge
                if list1.val < list2.val:
                    if not head:
                        head = ListNode(list1.val)
                        first_node = head
                    else:
                        head.next = ListNode(list1.val)
                        head = head.next
                    list1 = list1.next
                elif list2.val<list1.val:
                    if not head:
                        head = ListNode(list2.val)
                        first_node = head
                    else:
                        head.next = ListNode(list2.val)
                        head = head.next
                    list2 = list2.next
                else:
                    if not head:
                        head = ListNode(list1.val)
                        first_node = head
                        head.next = ListNode(list2.val)
                        head = head.next
                    else:
                        head.next = ListNode(list1.val)
                        head = head.next
                        head.next = ListNode(list2.val)
                        head = head.next
                    list1 = list1.next
                    list2 = list2.next
            if not list1:
                head.next = list2
            else:
                head.next = list1
            
            return first_node