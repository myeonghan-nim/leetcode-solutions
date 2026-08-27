class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - 97] += 1

        best = -1
        i = 0
        while i < n:
            t = ord(target[i]) - 97
            if any(cnt[c] for c in range(t + 1, 26)):
                best = i
            if cnt[t] == 0:
                break
            cnt[t] -= 1
            i += 1

        if best == -1:
            return ""

        for j in range(best, i):
            cnt[ord(target[j]) - 97] += 1

        t = ord(target[best]) - 97
        c = next(c for c in range(t + 1, 26) if cnt[c])
        cnt[c] -= 1
        tail = "".join(chr(97 + k) * cnt[k] for k in range(26))
        return target[:best] + chr(97 + c) + tail
