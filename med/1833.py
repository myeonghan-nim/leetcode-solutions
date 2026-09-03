class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        # 가격 상한이 작아 정렬 대신 계수 정렬. 싼 것부터 살 수 있는 만큼 산다
        # 시간 복잡도: O(n + C) — C는 가격 상한
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
