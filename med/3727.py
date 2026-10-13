class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        squares = [x * x for x in nums]
        k = len(squares) // 2
        total = sum(squares)

        if k == 0:
            return total

        def select(values, rank):
            if len(values) <= 5:
                return sorted(values)[rank]

            medians = []
            for i in range(0, len(values), 5):
                group = sorted(values[i:i + 5])
                medians.append(group[len(group) // 2])

            pivot = select(medians, len(medians) // 2)

            lower = []
            higher = []
            equal_count = 0

            for value in values:
                if value < pivot:
                    lower.append(value)
                elif value > pivot:
                    higher.append(value)
                else:
                    equal_count += 1

            if rank < len(lower):
                return select(lower, rank)
            if rank < len(lower) + equal_count:
                return pivot

            return select(higher, rank - len(lower) - equal_count)

        threshold = select(squares, k - 1)

        negative_sum = 0
        count = 0
        for value in squares:
            if value < threshold:
                negative_sum += value
                count += 1

        negative_sum += (k - count) * threshold

        return total - 2 * negative_sum
