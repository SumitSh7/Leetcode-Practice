# Definition for singly-linked list.
from typing import Optional, List

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        list3 = ListNode()
        current = list3

       
        while list1 and list2:
            
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next
        
        if list1:
           current.next = list1
        else:
           current.next = list2
        
        current.next = list1 if list1 else list2

        return list3.next
        




# --- HELPER FUNCTIONS FOR LOCAL TESTING ---

def create_linked_list(arr: list) -> Optional[ListNode]:
    """Converts a Python list [1,2,3] to a ListNode chain."""
    dummy = ListNode()
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def linked_list_to_python_list(node: Optional[ListNode]) -> list:
    """Converts a ListNode chain back to a Python list for easy printing."""
    res = []
    while node:
        res.append(node.val)
        node = node.next
    return res

if __name__ == "__main__":
    sol = Solution()
    
    # Convert lists to ListNodes before passing them to the function
    l1 = create_linked_list([10,20,30,50])
    l2 = create_linked_list([12,16,23,25,27,31,35,40])
    
    result_node = sol.mergeTwoLists(l1, l2)
    
    # Convert result back to list to see the output: [1, 1, 2, 3, 4, 4]
    print(linked_list_to_python_list(result_node))