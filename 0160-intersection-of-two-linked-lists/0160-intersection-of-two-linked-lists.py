# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        x,y=headA,headB
        while x!=y:
            if x:
                x=x.next
            else:
                x=headB
            if y:
                y=y.next
            else:
                y=headA
        return x                    
                    

        