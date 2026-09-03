class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 숫자를 문자열로 바꾸지 않고, 자릿수를 거꾸로 조립한 수가 원래 수와 같은지 확인한다. 음수는 부호 때문에 회문이 아니다
        # 시간 복잡도: O(log x)
        if x < 0:
            return False
        original = x
        reversed_num = 0
        while x > 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x //= 10
        return original == reversed_num
