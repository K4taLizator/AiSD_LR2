from Node import Node
class BinaryTree:
    def __init__(self):
        self.root = None  # Корень дерева

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursively(self.root, key)

    def _insert_recursively(self, current_node, key):
        if key < current_node.key:
            if current_node.left is None:
                current_node.left = Node(key)
            else:
                self._insert_recursively(current_node.left, key)
        elif key > current_node.key:
            if current_node.right is None:
                current_node.right = Node(key)
            else:
                self._insert_recursively(current_node.right, key)

    def min_value_node(node):
        """Функция для нахождения узла с минимальным значением в поддереве."""
        current = node
        while current.left is not None:
            current = current.left
        return current

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        """Функция удаления узла с заданным ключом из бинарного дерева поиска."""
        # Шаг 1: Найти узел, который нужно удалить
        if node is None:
            return node

        # Узел с ключом меньше, чем корень
        if key < node.key:
            node.left = self._delete(node.left, key)
        # Узел с ключом больше, чем корень
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            # Узел с ключом найден
            # Узел с одним дочерним элементом или без дочерних элементов
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Узел с двумя дочерними элементами: получаем inorder преемника (наименьший узел в правом поддереве)
            temp = self.min_value_node(node.right)
            node.key = temp.key  # Копируем значение inorder преемника в узел для удаления
            node.right = self._delete(node.right, temp.key)  # Удаляем inorder преемника

        return node