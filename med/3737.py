class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        # target을 +1, 나머지를 -1로 보고 누적합 cur을 구하면 합이 양수인 구간이 답이다. 누적합 값별 개수를 유지하고 '현재보다 작은 누적합의 개수(less)'를 cur이 오르내릴 때마다 O(1)로 갱신한다
        # 시간 복잡도: O(n)
        ans = 0
        cur = 0
        less = 0
        freq = {0: 1}

        for x in nums:
            if x == target:
                less += freq.get(cur, 0)  # cur이 1 오르면 이전 cur 값도 새 cur보다 작아진다
                cur += 1
            else:
                less -= freq.get(cur - 1, 0)  # cur이 1 내리면 cur-1 값은 더 이상 작지 않다
                cur -= 1

            ans += less
            freq[cur] = freq.get(cur, 0) + 1

        return ans
