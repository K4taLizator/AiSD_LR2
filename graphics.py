from graphviz import Digraph
import numpy as np
import matplotlib.pyplot as plt
def visualize(root, name):
        dot = Digraph()
        _visualize(dot, root)
        dot.render(name, format = 'png', cleanup = True)

def _visualize(dot, node):
        if node is not None:
            dot.node(str(node.key), str(node.key), color=node.color)
            if node.left is not None and node.left.key is not None:
                dot.edge(str(node.key), str(node.left.key))
                _visualize(dot, node.left)
            if node.right is not None and node.right.key is not None:
                dot.edge(str(node.key), str(node.right.key))
                _visualize(dot, node.right)

def inorder_traversal(node):
    if node is not None and node.key != None:
        inorder_traversal(node.left)
        print(node.key, end=' ')
        inorder_traversal(node.right)

def preorder_traversal(node):
    if node is not None and node.key != None:
        print(node.key, end=' ')
        preorder_traversal(node.left)
        preorder_traversal(node.right)

def postorder_traversal(node):
    if node is not None and node.key != None:
        postorder_traversal(node.left)
        postorder_traversal(node.right)
        print(node.key, end=' ')

def wide_traversal(root):

    if not root:
        return []

    queue = [root]  # Начинаем с корня дерева
    result = []

    while queue:
        current_node = queue.pop(0)  # Извлекаем первый элемент из очереди
        if current_node.key != None:
            print(current_node.key, end = ' ')  # Сохраняем значение текущего узла
        # Добавляем левого и правого ребенка в очередь, если они существуют
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)

def find_height(node):
    if node == None:
         return 0
    else:
        return max(find_height(node.left), find_height(node.right)) + 1
    
def plots(x, y, name):
    fig = plt.figure()
    plt.title(f'Высота {name} дерева')
    plt.xlabel('Число элементов')
    plt.ylabel('Высота')
    plt.scatter(x, y, marker ="o", color  = "red")
    t = np.arange(1000, 20000, 100)
    plt.plot(t, np.log2(t), "b--")
    plt.plot(x, y)
    plt.grid()
    plt.show()