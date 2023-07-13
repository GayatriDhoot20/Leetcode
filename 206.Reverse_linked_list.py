# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        if head.next is None:
            return head
        current = temp = ListNode(head.val)
        head=head.next
        while (head!=None):
            temp = ListNode(head.val)
            head=head.next
            temp.next=current
            current=temp
        return current