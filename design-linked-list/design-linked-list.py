class LinkedNode():
    def __init__(self,val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.length = 0
    def get(self, index: int) -> int:
        print("length: ", self.length)
        if index>=self.length:
            return -1
        else:
            first_node = self.head
            if index==0:
                return self.head.val
            else:
                while index>1:
                    first_node = first_node.next
                    index-=1
                return first_node.next.val

    def addAtHead(self, val: int) -> None:
        self.length+=1
        if not self.head:
            self.head = LinkedNode(val)
        else:
            new_node = LinkedNode(val)
            new_node.next = self.head
            self.head = new_node

    def addAtTail(self, val: int) -> None:
        self.length+=1
        if not self.head:
            self.head = LinkedNode(val)
        else:
            first_node = self.head
            while first_node.next:
                first_node = first_node.next
            first_node.next = LinkedNode(val)
        
    def addAtIndex(self, index: int, val: int) -> None:        
        if index>self.length:
            pass
        else:
            self.length+=1
            if not self.head:
                self.head = LinkedNode(val)
            else:
                first_node = self.head
                if index==0:
                    self.addAtHead(val)
                else:                    
                    while index>1:
                        first_node = first_node.next
                        index-=1
                    new_node = LinkedNode(val)
                    new_node.next = first_node.next
                    first_node.next = new_node
        

    def deleteAtIndex(self, index: int) -> None:
        
        if index>=self.length:
            pass
        else:
            self.length-=1
            first_node = self.head
            if index==0:
                self.head = self.head.next
            else:
                while index>1:
                    first_node = first_node.next
                    index-=1
                first_node.next = first_node.next.next

#print(MyLinkedList())
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)