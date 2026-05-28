class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        trie = [{}]
        best_index = [-1]

        def is_better(candidate: int, current: int) -> bool:
            if current == -1:
                return True

            candidate_len = len(wordsContainer[candidate])
            current_len = len(wordsContainer[current])
            return candidate_len < current_len or (candidate_len == current_len and candidate < current)

        def update_best(node: int, word_index: int) -> None:
            if is_better(word_index, best_index[node]):
                best_index[node] = word_index

        for word_index, word in enumerate(wordsContainer):
            node = 0
            update_best(node, word_index)

            for char in reversed(word):
                if char not in trie[node]:
                    trie[node][char] = len(trie)
                    trie.append({})
                    best_index.append(-1)

                node = trie[node][char]
                update_best(node, word_index)

        answer = []
        for word in wordsQuery:
            node = 0

            for char in reversed(word):
                next_node = trie[node].get(char)
                if next_node is None:
                    break
                node = next_node

            answer.append(best_index[node])

        return answer
