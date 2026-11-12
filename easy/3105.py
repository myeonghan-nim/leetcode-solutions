class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        # 현재 원소에서 끝나는 증가·감소 구간 길이를 각각 이어 가며, 이웃 대소 관계가 깨진 쪽만 1로 되돌린다
        # 시간 복잡도: O(n)
        answer = increasing = decreasing = 1
        for prev, cur in zip(nums, nums[1:]):
            increasing = increasing + 1 if prev < cur else 1
            decreasing = decreasing + 1 if prev > cur else 1  # 같은 값이면 둘 다 1로 끊긴다
            answer = max(answer, increasing, decreasing)
        return answer
