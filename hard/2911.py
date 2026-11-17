class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        INF = n + 1

        cost = [[INF] * (n + 1) for _ in range(n)]

        for d in range(1, n // 2 + 1):
            prev2 = [0] * (n + 1)
            prev1 = [0] * (n + 1)

            for length in range(2 * d, n + 1, d):
                gap = length - d

                prefix = [0] * (n - gap + 1)
                for i in range(n - gap):
                    prefix[i + 1] = prefix[i] + (s[i] != s[i + gap])

                current = [0] * (n - length + 1)

                for left in range(n - length + 1):
                    outer_cost = prefix[left + d] - prefix[left]

                    current[left] = prev2[left + d] + outer_cost

                    end = left + length
                    cost[left][end] = min(cost[left][end], current[left])

                prev2, prev1 = prev1, current

        previous = [INF] * (n + 1)
        previous[0] = 0

        for count in range(1, k + 1):
            current = [INF] * (n + 1)

            for end in range(2 * count, n + 1):
                for start in range(2 * (count - 1), end - 1):
                    current[end] = min(current[end], previous[start] + cost[start][end])

            previous = current

        return previous[n]
