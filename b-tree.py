class BTreeNode:
    def __init__(self):
        self.values = [] 
        self.children = [] 

class BTree:
    def __init__(self):
        self.root = BTreeNode() # 루트 노드

    def insert(self, value): # 값 삽입
        if not self.root.children:
            # 자식이 없다는 것은 얘가 그냥 리프가 되면 됨
            self.root.values.append(value)
            self.root.values.sort()
            if len(self.root.values) > 4:
                left = BTreeNode()
                right = BTreeNode()
                # 왼쪽과 오른쪽 노드에 값 할당
                left.values = self.root.values[:2]
                right.values = self.root.values[2:]
                left.children = []
                right.children = []
                # 중간 값 제거
                self.root.values = self.root.values[2:]
                # 새로운 노드를 현재 노드의 자식으로 할당
                self.root.children = [left, right]
        else:
            # 분할이 일어나지 않는다면 오름차순으로 삽입 진행하면 됨
            self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, node, value):
        if not node.children:
            # 리프 노드에 도달하면 값을 삽입하고 정렬
            node.values.append(value)
            node.values.sort()
            if len(node.values) > 4:
                left = BTreeNode()
                right = BTreeNode()
                # 왼쪽과 오른쪽 노드에 값 할당
                left.values = node.values[:2]
                right.values = node.values[2:]
                left.children = []
                right.children = []
                # 중간 값 제거
                node.values = node.values[2:]
                # 새로운 노드를 현재 노드의 자식으로 할당
                node.children = [left, right]
        else:
            # 자식 노드가 있는 경우 재귀적으로 삽입 진행
            i = 0
            while i < len(node.values):
                if value < node.values[i]:
                    break
                i += 1
            self._insert_recursive(node.children[i], value)
    
    def get(self, value):
        return self._get_recursive(self.root, value)
    
    def _get_recursive(self, node, value):
        if not node.children:
            return value in node.values
        else:
            i = 0
            while i < len(node.values):
                if value == node.values[i]:
                    return True
                if value < node.values[i]:
                    return self._get_recursive(node.children[i], value)
                i += 1
            return self._get_recursive(node.children[i], value)
    def delete_key(self, value):
        self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        if value in node.values:
            node.values.remove(value)
        else:
            i = 0
            while i < len(node.values):
                if value < node.values[i]:
                    break
                i += 1
        self._delete_recursive(node.children[i], value)
