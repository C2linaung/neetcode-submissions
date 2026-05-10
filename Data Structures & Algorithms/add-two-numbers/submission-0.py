# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        hasCarry = False
        t1 = l1
        t2 = l2
        final = ListNode()
        curr = final
        while t1 or t2:
            curr.next = ListNode()
            curr = curr.next
            v1 = t1.val if t1 else 0
            v2 = t2.val if t2 else 0
            val = v1 + v2 + (1 if hasCarry else 0)
            hasCarry = val > 9
            curr.val = val % 10
            t1 = t1.next if t1 else None
            t2 = t2.next if t2 else None
        
        if hasCarry:
            curr.next = ListNode(1)
        return final.next
                


