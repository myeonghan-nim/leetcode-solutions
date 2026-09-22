class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        tree = [None] * (4 * n)

        def merge(left, right):
            left_product, left_count = left
            right_product, right_count = right

            count = left_count.copy()

            for remainder in range(k):
                new_remainder = left_product * remainder % k
                count[new_remainder] += right_count[remainder]

            product = left_product * right_product % k
            return product, count

        def make_leaf(value):
            remainder = value % k
            count = [0] * k
            count[remainder] = 1
            return remainder, count

        def build(node, lo, hi):
            if lo == hi:
                tree[node] = make_leaf(nums[lo])
                return

            mid = (lo + hi) // 2
            build(node * 2, lo, mid)
            build(node * 2 + 1, mid + 1, hi)

            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])

        def update(node, lo, hi, index, value):
            if lo == hi:
                tree[node] = make_leaf(value)
                return

            mid = (lo + hi) // 2
            if index <= mid:
                update(node * 2, lo, mid, index, value)
            else:
                update(node * 2 + 1, mid + 1, hi, index, value)

            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])

        def query_suffix(node, lo, hi, start):
            if start <= lo:
                return tree[node]

            mid = (lo + hi) // 2
            if start > mid:
                return query_suffix(node * 2 + 1, mid + 1, hi, start)

            left_part = query_suffix(node * 2, lo, mid, start)
            right_part = tree[node * 2 + 1]

            return merge(left_part, right_part)

        build(1, 0, n - 1)

        result = []

        for index, value, start, x in queries:
            update(1, 0, n - 1, index, value)

            _, count = query_suffix(1, 0, n - 1, start)
            result.append(count[x])

        return result
