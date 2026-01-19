# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        cursor = ListNode()
        cursor = head

        while cursor and cursor.next:
            if cursor.val == cursor.next.val:
                cursor.next = cursor.next.next
            else:
                cursor = cursor.next

        return head



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

        l1 = create_linked_list([1,1,2,2,2,3,4,5,5,6,6,6,7])
        
        result_node = sol.deleteDuplicates(l1)
        
        # Convert result back to list to see the output:
        print(linked_list_to_python_list(result_node))