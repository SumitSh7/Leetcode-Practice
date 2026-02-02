from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if not head:
            return False
        
        cursor = head
        lapper = head

        while lapper and lapper.next:

            cursor = cursor.next
            lapper = lapper.next.next

            if cursor == lapper:
                return True
        
        return False
        


        