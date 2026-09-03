class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        # 값 -> 노드 딕셔너리로 노드를 만들며 부모-자식을 연결하고, 자식으로 한 번도 등장하지 않은 값이 루트이다
        # 시간 복잡도: O(n)
        nodes = {}
        children = set()

        for parent, child, is_left in descriptions:
            if parent not in nodes:
                nodes[parent] = TreeNode(parent)
            if child not in nodes:
                nodes[child] = TreeNode(child)

            parent_node = nodes[parent]
            child_node = nodes[child]

            if is_left:
                parent_node.left = child_node
            else:
                parent_node.right = child_node

            children.add(child)

        for value, node in nodes.items():
            if value not in children:
                return node
