# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution(object):
#     def middleNode(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode

#         """
#         count = 1
#         recount = 1
#         next_head = head
#         while head.next is not None:
#             head = head.next
#             count += 1

#         start_point = count // 2 + 1
#         re = None

#         while next_head is not None:
#             if recount == start_point:
#                 re = next_head
#                 break
#             elif recount < start_point:
#                 recount += 1

#             next_head = next_head.next
#         return re


# ===================
# EFFICIENT SOLLUTION
class Solution:
    def middleNode(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print(head)
        return slow

