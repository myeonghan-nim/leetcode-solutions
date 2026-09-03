class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 두 리스트를 앞(일의 자리)부터 자리올림과 함께 더하고, 마지막까지 올림이 남으면 노드를 하나 더 붙인다
        # 시간 복잡도: O(max(m, n))
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
