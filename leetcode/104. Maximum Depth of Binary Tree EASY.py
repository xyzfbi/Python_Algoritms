"""
104. Maximum Depth of Binary Tree
Easy
Topics
Companies

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.



Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:

Input: root = [1,null,2]
Output: 2



Constraints:

    The number of nodes in the tree is in the range [0, 104].
    -100 <= Node.val <= 100
"""
"""
Ожидаемый результат: [1,3,2]
Алгоритм (используем стек):

    Инициализируем пустой стек и пустой результат

    Начинаем с корня (current = root)

    Пока current не None или стек не пуст:

        Идём влево до конца, добавляя все узлы в стек

        Достаём узел из стека (это будет самый левый)

        Добавляем его значение в результат

        Переходим к правому поддереву

Пошаговое выполнение:

Исходное дерево:
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0

        max_depth = 0
        stack = [(root, 1)]
        while stack:
            node, depth = stack.pop()
            max_depth = max(max_depth, depth)
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))

        return max_depth
