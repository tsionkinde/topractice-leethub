# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before=ListNode(0)
        after=ListNode(0)
        before_current=before
        after_current=after
        while head:
            if head.val<x:
                before_current.next=head
                before_current=before_current.next
            else:
                after_current.next=head
                after_current=after_current.next
            head=head.next
        after_current.next=None
        before_current.next=after.next
        return before.next





                
