class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        # 교환 한 번은 '1 블록 하나를 0으로 바꿨다 되돌리기'이므로, 그 블록 양옆의 0 구간을 모두 1로 만드는 효과이다. 연속된 두 0 구간 길이 합의 최댓값을 원래 1 개수에 더한다
        # 시간 복잡도: O(n)
        active = 0
        best_gain = 0
        previous_zeros = 0
        current_zeros = 0

        for section in s:
            if section == "0":
                current_zeros += 1
                continue

            active += 1

            if current_zeros:
                if previous_zeros:
                    best_gain = max(best_gain, previous_zeros + current_zeros)
                previous_zeros = current_zeros
                current_zeros = 0

        if current_zeros and previous_zeros:
            best_gain = max(best_gain, previous_zeros + current_zeros)

        return active + best_gain
