
"""
12. Длина кратчайшего пути
Решена
Лёгкая

Дан неориентированный граф. Найдите длину минимального пути между двумя вершинами.
Формат ввода

В первой строке записано целое число N N ( 1 ≤ N ≤ 100 1≤N≤100) – количество вершин в графе.

Далее записывается матрица смежности — N N строк, в каждой из которых содержится N N чисел 0 или 1, разделённых пробелом. Число 0 означает отсутствие ребра, а 1 — наличие ребра.

В последней строке задаются номера двух вершин — начальной и конечной.

Вершины нумеруются с единицы.
Формат вывода

Выведите длину кратчайшего пути — минимальное количество ребер, которые нужно пройти.

Если пути нет, нужно вывести -1.

"""


from collections import deque


def main():
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    start, finish = map(int, input().split())

    start -= 1
    finish -= 1
    visited = [False] * n
    queue = deque([(start, 0)])

    while queue:
        node, step = queue.popleft()

        if node == finish:
            print(step)
            return

        visited[node] = True

        for neighbor in range(n):
            if matrix[node][neighbor] == 1 and not visited[neighbor]:
                queue.append((neighbor, step + 1))
                visited[neighbor] = True

    print(-1)


if __name__ == '__main__':
    main()
