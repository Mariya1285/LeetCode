"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        idx = 0
        node_head, new_list_head = None, None
        random_ptrs = list()
        storage_nodes = list()
        new_nodes_storage = list()
        while head:
            if not node_head:
                node_head = Node(head.val, head.next)
                new_list_head = node_head
                random_ptrs.append(head.random)
                storage_nodes.append(head)
                print("new_list_had: ", new_list_head)
                new_nodes_storage.append(new_list_head)
                head = head.next
                idx+=1
            else:
                node_head.next = Node(head.val, head.next)
                random_ptrs.append(head.random)
                storage_nodes.append(head)
                new_nodes_storage.append(node_head.next)
                head = head.next
                node_head = node_head.next
                
                idx+=1
        #new_head =  random_ptrs[0]
        i = 0
        for random_nodes in random_ptrs:
            if random_nodes and (random_nodes in storage_nodes):
                print("index of ptr: ", storage_nodes.index(random_nodes))
                random_ptrs[i] = storage_nodes.index(random_nodes)
            else:
                random_ptrs[i] = None
            i+=1
                
        print(new_list_head)
        iterator = 0
        new_node = new_list_head
        while new_node:
            new_random_idx = random_ptrs[iterator]
            print("new random idx: ", new_random_idx)
            if new_random_idx !=None:
                new_node.random = new_nodes_storage[new_random_idx]
                new_node = new_node.next
                iterator+=1
            else:
                new_node.random = None
                new_node = new_node.next
                iterator+=1
            
            
        return new_list_head
        