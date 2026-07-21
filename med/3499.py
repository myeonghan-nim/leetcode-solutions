class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
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
