class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
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
