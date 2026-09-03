class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        # 정렬 후 첫 원소는 1, 이후는 직전보다 최대 1 크게 만들 수 있다. n보다 큰 값은 n으로 잘라 계수 정렬하고, 값 v를 볼 때마다 answer는 v를 넘지 못한다
        # 시간 복잡도: O(n)
        n = len(arr)
        counts = [0] * (n + 1)

        for num in arr:
            counts[min(num, n)] += 1

        answer = 0
        for value in range(1, n + 1):
            answer = min(value, answer + counts[value])

        return answer
