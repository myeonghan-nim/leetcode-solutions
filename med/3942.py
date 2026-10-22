class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # 두 연산은 원형 배열의 회전·뒤집기만 만들므로 오름차순 순환이거나 내림차순 순환일 때만 정렬 가능하다. 첫 원소 k로 두 전략(회전만 / 뒤집기 포함) 중 짧은 쪽을 닫힌식으로 고른다
        # 시간 복잡도: O(n)
        n, k = len(nums), nums[0]
        if all(nums[i] == (k + i) % n for i in range(n)):
            return min((n - k) % n, k + 2)  # 왼쪽으로 n-k번 회전 vs 뒤집고 k번 회전 뒤 다시 뒤집기
        if all(nums[i] == (k - i) % n for i in range(n)):
            return min(k + 2, n - k)  # k+1번 회전해 완전 내림차순을 만들고 뒤집기 vs 먼저 뒤집고 n-k-1번 회전
        return -1
