# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        rl1 = l1[::-1]
        rl2 = l2[::-1]
        count = rl1 + rl2
        return count
        

sol = Solution()
resoult = sol.addTwoNumbers([2, 4, 3], [5, 6, 4])
print(resoult)