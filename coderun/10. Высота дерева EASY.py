"""
10. Высота дерева
Не решалась
Лёгкая

Реализуйте бинарное дерево поиска для целых чисел.

Программа должна последовательно обрабатывать вводимые числа. Если очередное число есть в дереве, ничего делать не нужно. Если числа в дереве нет, нужно добавить его в соответствующее место дерева.

Балансировку дерева производить не нужно.

Найдите высоту получившегося дерева.
Формат ввода

На вход программа получает последовательность натуральных чисел. Последовательность завершается числом 0, которое означает конец ввода. Добавлять его в дерево не надо.
Формат вывода

Выведите высоту получившегося дерева.
"""
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
def insert(root, key):
    if root is None:
        return TreeNode(key)
    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    
    return root
def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))
def main():
    root = None
    nums = map(int, input().split())
    for num in nums:
        if num == 0:
            break
        
        root = insert(root, num)
    
    print(height(root))


if __name__ == '__main__':
    main()
