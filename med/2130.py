class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # 느린/빠른 포인터로 중간 지점을 찾고, 뒤 절반을 뒤집은 뒤 앞 절반과 나란히 걸으며 쌍의 합을 비교한다
        # 시간 복잡도: O(n)
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        ans = 0
        left, right = head, prev
        while right:
            ans = max(ans, left.val + right.val)
            left = left.next
            right = right.next

        return ans
