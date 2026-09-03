class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 정렬된 리스트에서 중복은 항상 인접하므로, 다음 노드 값이 같으면 다음 노드를 건너뛰어 연결한다
        # 시간 복잡도: O(n)
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head
