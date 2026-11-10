class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        # i번 계단의 최소 비용은 직전 세 계단 값만으로 정해지므로 변수 세 개를 굴리며 갱신한다.
        # 시간 복잡도: O(n)
        inf = float('inf')
        back3, back2, back1 = inf, inf, 0  # 각각 3칸 전, 2칸 전, 1칸 전 계단까지의 최소 비용
        for cost in costs:
            back3, back2, back1 = back2, back1, cost + min(back1 + 1, back2 + 4, back3 + 9)
        return back1
