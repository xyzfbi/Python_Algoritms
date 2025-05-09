"""
    from collections import defaultdict
    n, m = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]

    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    visited = set()
    stack = [1]
    component = []
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            component.append(node)
            stack.extend(set(graph[node]) - visited)

    component.sort()
    print(len(component))
    print(*component)
"""
"""
8. Компоненты связности
Не решалась
Средняя

Дан неориентированный невзвешенный граф, состоящий из N N вершин и M M ребер. Необходимо посчитать количество его компонент связности и вывести их.

Напомним:

Компонента связности в неориентированном графе - это подмножество вершин, таких что все вершины достижимы друг из друга.
Формат ввода

Во входном файле записано два числа N и M (0 < < N ≤ ≤ 100000, 0 ≤ ≤ M ≤ ≤ 100000). В следующих M строках записаны по два числа i и j (1 ≤ ≤ i, j ≤ ≤ N), которые означают, что вершины i и j соединены ребром.
Формат вывода

В первой строчке выходного файла выведите количество компонент связности. Далее выведите сами компоненты связности в следующем формате: в первой строке количество вершин в компоненте, во второй - сами вершины в произвольном порядке.
"""


def main():
    from collections import defaultdict
    n, m = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]

    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    visited = set()
    components = []

    def dfs(start):
        stack = [start]
        component = []
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                component.append(node)
                stack.extend(set(graph[node]) - visited)

        return sorted(component)

    for nd in range(1, n + 1):
        if nd not in visited:
            components.append(dfs(nd))
    
    print(len(components))
    for comp in components:
        print(len(comp))
        print(*comp)


if __name__ == '__main__':
    main()
