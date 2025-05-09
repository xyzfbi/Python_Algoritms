def main():
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


if __name__ == '__main__':
    main()
