# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        temp = head
        flag = True
        while temp:
            stack.append(temp.val)
            temp = temp.next
        while head:
            ele = stack.pop()
            if head.val == ele:
                head = head.next
            else:
                print("False here: ",ele)
                print(head.val)
                flag = False
                break
              
        return flag