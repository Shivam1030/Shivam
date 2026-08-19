def add_edge(graph, u, v):
    graph[u].append(v)
    graph[v].append(u)


def is_valid(graph):
    for i in range(len(graph)):
        for neighbor in graph[i]:
            if i not in graph[neighbor]:
                return False
    return True


vertices = 5

graph = [[] for _ in range(vertices)]

add_edge(graph, 0, 1)
add_edge(graph, 0, 2)
add_edge(graph, 1, 3)
add_edge(graph, 2, 3)
add_edge(graph, 3, 4)

print("Is valid:", is_valid(graph))

for i in range(vertices):
    print(i, "->", graph[i])