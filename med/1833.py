class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        limit = min(max(costs), coins)
        count = [0] * (limit + 1)

        for cost in costs:
            if cost <= limit:
                count[cost] += 1

        answer = 0

        for cost in range(1, limit + 1):
            if coins < cost:
                break

            buy = min(count[cost], coins // cost)
            answer += buy
            coins -= buy * cost

        return answer
