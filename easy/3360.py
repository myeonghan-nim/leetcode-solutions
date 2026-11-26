class Solution:
    def canAliceWin(self, n: int) -> bool:
        alice_wins = False

        for stones in range(10, 0, -1):
            if n < stones:
                break

            n -= stones
            alice_wins = not alice_wins

        return alice_wins
