class Solution:
    def mySqrt(self, x: int) -> int:
        # 1 ~ x//2 범위에서 제곱이 x 이하인 가장 큰 정수를 이진 탐색으로 찾는다
        # 시간 복잡도: O(log x)
        if x < 2:
            return x

        left, right = 1, x // 2
        while left <= right:
            mid = (left + right) // 2
            square = mid * mid
            if square == x:
                return mid
            elif square < x:
                left = mid + 1
            else:
                right = mid - 1

        return right  # 루프가 끝나면 right가 제곱이 x 이하인 마지막 값
