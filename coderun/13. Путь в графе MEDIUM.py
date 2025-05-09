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
    queue = deque([start])
    visited[start] = True
    route = [-1] * n
    if start == finish:
        print(0)
        return
    while queue:
        node = queue.popleft()

        if node == finish:
            break

        for neighbor in range(n):
            if matrix[node][neighbor] == 1 and not visited[neighbor]:
                queue.append(neighbor)
                route[neighbor] = node
                visited[neighbor] = True

    if route[finish] == -1:
        print(-1)
        return
    else:
        path = []
        current = finish
        while current != -1:
            path.append(current + 1)
            current = route[current]

        path.reverse()
        if len(path) - 1 == 0:
            print(0)
            return

        else:
            print(len(path) - 1)
            print(*path)
            
if __name__ == '__main__':
    main()
