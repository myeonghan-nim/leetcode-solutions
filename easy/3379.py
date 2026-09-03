class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        # 각 원소만큼 이동한 위치를 파이썬 나머지 연산으로 감싸면 음수 이동도 자동으로 순환한다
        # 시간 복잡도: O(n)
        n = len(nums)
        return [nums[(i + nums[i]) % n] for i in range(n)]
