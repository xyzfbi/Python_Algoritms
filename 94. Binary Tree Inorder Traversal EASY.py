"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.



Example 1:

Input: root = [1,null,2,3]

Output: [1,3,2]

Explanation:

Example 2:

Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

Output: [4,2,6,5,7,1,3,9,8]

Explanation:

Example 3:

Input: root = []

Output: []

Example 4:

Input: root = [1]

Output: [1]



Constraints:

    The number of nodes in the tree is in the range [0, 100].
    -100 <= Node.val <= 100


Follow up: Recursive solution is trivial, could you do it iteratively?
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
    def inorderTraversal(self, root):
        def inorder(node, result):
            if node:
                inorder(node.left, result)

                result.append(node.val)
                inorder(node.right, result)

        result = []
        inorder(root, result)
        return result

    '''def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []
        stack = []
        current = root
        while current or stack:
            while current:  # идем до конца левого
                stack.append(current)  # добавляем в стек
                current = current.left

            current = stack.pop()  # куррент будет последним родителем в стеке то есть последним родителем нижнего дерева
            result.append(current.val)  # добавляем его в результат
            current = current.right  # идем в правое дерево

        return result'''


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


s = Solution()
arr = [1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9]
print(s.inorderTraversal(build_tree_from_list(arr)))
