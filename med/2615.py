class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        # 같은 값의 인덱스 차이 합을 왼쪽에서 오른쪽, 오른쪽에서 왼쪽 두 번 훑어 구한다. 지금까지 나온 같은 값의 개수와 인덱스 합을 알면 |i - j| 합을 O(1)에 갱신할 수 있다
        # 시간 복잡도: O(n)
        n = len(nums)
        ans = [0] * n

        count = {}
        sum_so_far = {}
        for i in range(n):
            num = nums[i]
            if num in count:
                ans[i] += count[num] * i - sum_so_far[num]  # 왼쪽의 같은 값들과의 거리 합 = i × 개수 - 인덱스 합
            count[num] = count.get(num, 0) + 1
            sum_so_far[num] = sum_so_far.get(num, 0) + i

        count.clear()
        sum_so_far.clear()
        for i in range(n - 1, -1, -1):
            num = nums[i]
            if num in count:
                ans[i] += sum_so_far[num] - count[num] * i
            count[num] = count.get(num, 0) + 1
            sum_so_far[num] = sum_so_far.get(num, 0) + i

        return ans
