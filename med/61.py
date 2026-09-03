class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 길이를 구하고 k를 길이로 나눈 나머지만큼만 회전한다. 꼬리를 머리에 연결해 원형으로 만든 뒤 새 꼬리에서 끊는다
        # 시간 복잡도: O(n)
        if not head or not head.next or k == 0:
            return head

        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        k %= length
        if k == 0:
            return head

        tail.next = head

        steps_to_new_tail = length - k - 1
        new_tail = head
        for _ in range(steps_to_new_tail):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None

        return new_head
