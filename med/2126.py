class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        # 작은 소행성부터 부딪히면 질량이 최대한 커진 상태로 큰 소행성을 만나므로 정렬 후 순서대로 흡수한다
        # 시간 복잡도: O(n log n)
        asteroids.sort()

        for asteroid in asteroids:
            if mass < asteroid:
                return False

            mass += asteroid

        return True
