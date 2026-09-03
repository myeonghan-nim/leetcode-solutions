class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        # target과 앞에서부터 같은 글자로 최대한 맞춰 가면서, 남은 글자 중 target[i]보다 큰 글자가 있는 마지막 위치 best를 기억한다. best 자리에 그보다 큰 가장 작은 글자를 놓고 나머지는 오름차순으로 붙이면 target보다 큰 가장 작은 순열이다
        # 시간 복잡도: O(n · 26)
        n = len(s)
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - 97] += 1

        best = -1
        i = 0
        while i < n:
            t = ord(target[i]) - 97
            if any(cnt[c] for c in range(t + 1, 26)):  # 이 자리에서 target보다 커질 수 있는 마지막 위치를 기록
                best = i
            if cnt[t] == 0:  # target[i]와 같은 글자가 없으면 더 이상 접두사를 맞출 수 없다
                break
            cnt[t] -= 1
            i += 1

        if best == -1:
            return ""

        for j in range(best, i):  # best 이후에 써 버린 글자를 다시 돌려놓는다
            cnt[ord(target[j]) - 97] += 1

        t = ord(target[best]) - 97
        c = next(c for c in range(t + 1, 26) if cnt[c])
        cnt[c] -= 1
        tail = "".join(chr(97 + k) * cnt[k] for k in range(26))
        return target[:best] + chr(97 + c) + tail
