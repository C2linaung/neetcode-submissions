# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            nxt = curr.next     # store next node
            curr.next = prev    # reverse pointer
            prev = curr         # move prev forward
            curr = nxt          # move curr forward

        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Cut from middle
        second = slow.next
        slow.next = None
        second = self.reverseList(second)
        first = head
        while second:
            next1 = first.next
            next2 = second.next
            first.next = second
            second.next = next1
            first = next1
            second = next2