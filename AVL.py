from Node import Node

class AVLTree:
    def __init__(self, key = None):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        # 1. Выполнить стандартную вставку узла в BST
        if not node:
            return Node(key)
        elif key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)

        # 2. Обновить высоту предка узла
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

        # 3. Получить баланс узла
        balance = self.get_balance(node)

        # 4. Если узел стал несбалансированным, то выполнить соответствующие операции
        # Левый Левый случай
        if balance > 1 and key < node.left.key:
            return self.right_rotate(node)

        # Правый Правый случай
        if balance < -1 and key > node.right.key:
            return self.left_rotate(node)

        # Левый Правый случай
        if balance > 1 and key > node.left.key:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        # Правый Левый случай
        if balance < -1 and key < node.right.key:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node
    
    def min_value_node(self, node):
        if node is None or node.left is None:
            return node
        return self.min_value_node(node.left)

    def delete(self, key):
        self.root = self._delete(self.root, key)
    
    def _delete(self, node, key):
        # Стандартное удаление узла
        if not node:
            return node

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            # Узел с единственным дочерним элементом или без дочерних элементов
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Узел с двумя дочерними элементами: получаем inorder преемника (наименьший узел в правом поддереве)
            temp = self.min_value_node(node.right)
            node.key = temp.key
            node.right = self._delete(node.right, temp.key)

        # Если дерево стало пустым
        if node is None:
            return node

        # Обновляем высоту узла
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

        # Балансируем дерево
        balance = self.get_balance(node)

        # Левый левый случай
        if balance > 1 and self.get_balance(node.left) >= 0:
            return self.right_rotate(node)

        # Левый правый случай
        if balance > 1 and self.get_balance(node.left) < 0:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        # Правый правый случай
        if balance < -1 and self.get_balance(node.right) <= 0:
            return self.left_rotate(node)

        # Правый левый случай
        if balance < -1 and self.get_balance(node.right) > 0:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node


   
    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        # Выполнить поворот
        y.left = z
        z.right = T2

        # Обновить высоты
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        # Возвратить новый корень
        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        # Выполнить поворот
        y.right = z
        z.left = T3

        # Обновить высоты
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        # Возвратить новый корень
        return y

    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)
