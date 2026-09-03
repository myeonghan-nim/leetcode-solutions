class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 더미 노드 뒤에 두 리스트의 앞쪽 노드 중 작은 쪽을 차례로 이어 붙이고, 한쪽이 끝나면 나머지를 통째로 붙인다
        # 시간 복잡도: O(m + n)
        dummy = ListNode()
        current = dummy

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        current.next = list1 or list2  # 남은 쪽(둘 다 None이면 None)을 그대로 붙인다

        return dummy.next
