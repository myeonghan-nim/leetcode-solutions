class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1, n2 = l1, l2
        carry = 0

        head = ListNode()
        node = head
        while n1 or n2 or carry:
            v1, v2 = n1.val if n1 else 0, n2.val if n2 else 0
            carry, val = divmod(v1 + v2 + carry, 10)

            node.next = ListNode(val)
            node = node.next

            if n1:
                n1 = n1.next
            if n2:
                n2 = n2.next

        return head.next
