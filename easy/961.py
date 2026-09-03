class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        # 배열 절반이 같은 값이므로 처음으로 두 번 만나는 값이 답이다
        # 시간 복잡도: O(n)
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
        return -1
