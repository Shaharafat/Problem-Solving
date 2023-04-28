# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        digit_count = 0
        num_one = 0
        num_two = 0
        final_num = 0
        while l1 or l2:
            if l1 is not None:
                num_one += l1.val * (10**digit_count)
                l1 = l1.next
            if l2 is not None:
                num_two += l2.val * (10**digit_count)
                l2 = l2.next
            digit_count += 1

        final_num = num_one + num_two
        result_length = len(str(final_num)) + 1
        sum_linked_list = None

        digit_count = 0
        for i in range(1, result_length):
            digit = final_num % (10**i) // 10**digit_count

            if i == 1:
                sum_linked_list = ListNode(digit)
                node = sum_linked_list
            else:
                new_node = ListNode(digit)
                node.next = new_node
                node = new_node

            digit_count += 1
        # print(sum_linked_list)
        return sum_linked_list


s = Solution()
s.addTwoNumbers(
    ListNode(2, ListNode(4, ListNode(3, None))),
    ListNode(5, ListNode(6, ListNode(4, None))),
)

# s.addTwoNumbers(
#     ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, None)))))),
#     ListNode(5, ListNode(6, ListNode(4, None))),
# )
tests = [
    (
        ([2,4,3],[5,6,4]),
        ([7,0,8]),
    )
]