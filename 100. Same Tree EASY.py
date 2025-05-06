"""
100. Same Tree
Easy
Topics
Companies

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.



Example 1:

Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:

Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:

Input: p = [1,2,1], q = [1,1,2]
Output: false



Constraints:

    The number of nodes in both trees is in the range [0, 100].
    -104 <= Node.val <= 104


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


'''class Solution(object):
    def inorderTraversal(self, root):
        result = []
        stack = []
        current = root
        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            result.append(current.val)
            current = current.right

        return result'''


class Solution(object):

    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        from collections import deque
        queue = deque((p, q))
        while len(queue) > 0:
            p, q = queue.popleft()
            if not p and not q:
                return True
            elif not p or not q:
                return False
            elif p.val != q.val:
                return False

            queue.append((p.left, q.left))
            queue.append((p.right, q.right))
        return True


class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


def build_tree_from_list(lst):
    if not lst:
        return None

    root = TreeNode(lst[0])
    queue = [root]
    i = 1

    while queue and i < len(lst):
        current_node = queue.pop(0)

        if i < len(lst) and lst[i] is not None:
            current_node.left = TreeNode(lst[i])
            queue.append(current_node.left)
        i += 1

        if i < len(lst) and lst[i] is not None:
            current_node.right = TreeNode(lst[i])
            queue.append(current_node.right)
        i += 1

    return root


