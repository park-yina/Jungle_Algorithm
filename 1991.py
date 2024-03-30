n = int(input())
arr = []
for _ in range(n):
    arr.append(input().split())

class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

    def preOrder(self, node):
        print(node.data, end='')
        if node.left != '.':
            self.preOrder(tree[node.left])
        if node.right != '.':
            self.preOrder(tree[node.right])

    def inOrder(self, node):
        if node.left != '.':
            self.inOrder(tree[node.left])
        print(node.data,end='')
        if node.right != '.':
            self.inOrder(tree[node.right])

    def postOrder(self, node):
        if node.left != '.':
            self.postOrder(tree[node.left])
        if node.right != '.':
            self.postOrder(tree[node.right])
        print(node.data,end='')

tree = {}
for item, left, right in arr:
    tree[item] = Node(item, left, right)

tree_root = tree['A']  # Assuming 'A' is the root of the tree
tree_root.preOrder(tree_root)
print()
tree_root.inOrder(tree_root)
print()
tree_root.postOrder(tree_root)