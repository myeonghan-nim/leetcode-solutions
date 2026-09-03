class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        # 짝수 n은 ans | (ans+1)이 항상 홀수라 불가능(-1). 홀수 n은 끝에 붙은 1의 개수가 t일 때 그 블록의 최상위 비트를 끄면 최소 ans가 된다
        # 시간 복잡도: O(n log M)
        ans = []
        for n in nums:
            if n & 1 == 0:
                ans.append(-1)
                continue

            trailing_ones = 0
            tmp = n
            while tmp & 1:
                trailing_ones += 1
                tmp >>= 1

            ans.append(n - (1 << (trailing_ones - 1)))  # 연속된 1 블록의 최상위 비트를 끈다
        return ans
