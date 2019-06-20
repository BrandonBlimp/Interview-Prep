# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example:

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        returnl = ListNode(0)
        pointerl = returnl
        carry = 0
        while l1 is not None or l2 is not None or carry > 0:
            nextVal1 = 0
            nextVal2 = 0
            if l1 is not None:
                nextVal1 = l1.val
            if l2 is not None:
                nextVal2 = l2.val
            
            if (nextVal1 + nextVal2 + carry) >= 10:
                pointerl.next = ListNode((nextVal1 + nextVal2 + carry)%10)
                carry = 1
            else:
                pointerl.next = ListNode(nextVal1 + nextVal2 + carry)
                carry = 0
            
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
            pointerl = pointerl.next
            
        return returnl.next