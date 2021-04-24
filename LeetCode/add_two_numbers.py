# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        carry = 0

        sum = (l1.val + l2.val + carry)
        carry = 0
        value = sum % 10
        temp_node = ListNode(val=value)
        # print(temp_node.val)
        if sum > 9:
            carry = 1
        l1 = l1.next
        l2 = l2.next
        l3 = temp_node
        head = l3

        while (l1 is not None) or (l2 is not None):
            if l1 is not None and l2 is not None:
                sum = (l1.val + l2.val + carry)
                carry = 0
                value = sum % 10
                temp_node = ListNode(val=value)
                # print(temp_node.val)
                if sum > 9:
                    carry = 1
                l1 = l1.next
                l2 = l2.next
                l3.next = temp_node
                l3 = l3.next
            if l1 is not None and l2 is None:
                sum = (l1.val + carry)
                carry = 0
                value = sum % 10
                temp_node = ListNode(val=value)
                # print(temp_node.val)
                if sum > 9:
                    carry = 1
                l1 = l1.next
                l3.next = temp_node
                l3 = l3.next
            if l1 is None and l2 is not None:
                sum = (l2.val + carry)
                carry = 0
                value = sum % 10
                temp_node = ListNode(val=value)
                # print(temp_node.val)
                if sum > 9:
                    carry = 1
                l2 = l2.next
                l3.next = temp_node
                l3 = l3.next
        if carry == 1:
            temp_node = ListNode(val=1)
            l3.next = temp_node
            l3 = l3.next
        # while head is not None:
        #     print(head.val)
        #     head = head.next
        return head
