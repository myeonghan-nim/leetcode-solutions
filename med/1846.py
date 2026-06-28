class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        n = len(arr)
        counts = [0] * (n + 1)

        for num in arr:
            counts[min(num, n)] += 1

        answer = 0
        for value in range(1, n + 1):
            answer = min(value, answer + counts[value])

        return answer
