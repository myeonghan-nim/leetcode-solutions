class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # 일의 자리부터 자리올림을 더해 가며, 마지막까지 올림이 남으면 맨 앞에 1을 붙인다
        # 시간 복잡도: O(n)
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            digit = digits[i] + carry
            digits[i] = digit % 10
            carry = digit // 10
        if carry:
            digits = [1] + digits
        return digits
