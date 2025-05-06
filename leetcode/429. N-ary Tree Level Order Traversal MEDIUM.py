"""
Подход

Для решения задачи используется алгоритм обхода дерева в ширину (BFS). Основные шаги:

    Проверка на пустое дерево: Если корень дерева отсутствует, возвращается пустой список.

    Инициализация очереди: Создается очередь, в которую помещается корневой узел.

    Обработка каждого уровня: Пока очередь не пуста, обрабатываются все узлы текущего уровня. Для каждого узла его значение добавляется в текущий уровень, а его дочерние узлы помещаются в очередь для обработки на следующем уровне.

    Сбор значений уровней: После обработки всех узлов текущего уровня, собранные значения добавляются в результирующий список.
"""


"""
429. N-ary Tree Level Order Traversal
Solved
Medium
Topics
Companies

Given an n-ary tree, return the level order traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

 

Example 1:

Input: root = [1,null,3,2,4,null,5,6]
Output: [[1],[3,2,4],[5,6]]

Example 2:

Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]

 

Constraints:

    The height of the n-ary tree is less than or equal to 1000
    The total number of nodes is between [0, 104]

"""


# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


from collections import deque


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []

        queue = deque([root])  # двусторонняя очередь для обхода дерева
        result = []  # езультат
        while queue:  # пока есть узлы
            level_s = len(queue)  # получаем длину сейчасшнего левела
            curr_level = []  # инициализация массива для хранения левела
            for _ in range(level_s):  # для каждого узла уровня
                node = queue.popleft()  # извлекаем из очереди первый элемент
                curr_level.append(node.val)  # добавляем его значение
                queue.extend(node.children or [])  # и каждого ребенка  этого узла мы добавляем в очередб на будущее
                '''for child in node.children: 
                    curr_level.append(child.val) '''
            result.append(curr_level)  # добавляем по итогу массив этого левела

        return result


s = Solution()
graph = node = Node(3, children=[
    Node(5),
    Node(6)
])
print(s.levelOrder(graph))
