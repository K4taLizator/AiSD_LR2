class Node:
    def __init__(self, key = None):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
        self.height = 1     # Высота элемента в дереве
        self.color = 'red'  # Новый узел всегда красный
        self.parent = None  # Указатель на родительский узел
    
    def grandparent(self):
        if self.parent is None:
            return None
        return self.parent.parent

    # function to get the sibling of node
    def sibling(self):
        if self.parent is None:
            return None
        if self == self.parent.left:
            return self.parent.right
        return self.parent.left

    # function to get the uncle of node
    def uncle(self):
        if self.parent is None:
            return None
        return self.parent.sibling()