class Node(object):
    def __init__(self, has_end=False):
        self.is_terminal = has_end
        self.children = dict()

class Trie(object):
    def __init__(self):
        self.head = Node()

    def insert(self, string):
        cur_node = self.head
        for char in string:
            if cur_node.children.get(char) is None:
                cur_node.children[char] = Node()
            cur_node = cur_node.children[char]
        cur_node.is_terminal = True

    def search(self, string):
        cur_node = self.head
        for char in string:
            if cur_node.children.get(char) is None:
                return False
            cur_node = cur_node.children[char]
        return cur_node.is_terminal
