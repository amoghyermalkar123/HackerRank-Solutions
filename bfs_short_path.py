def cal(key, start, _path_matrix):
    temp = key - 1
    dis = 0
    while temp != start - 1:
        for i in range(len(_path_matrix[0])):
            if _path_matrix[i][temp] == 6:
                dis = dis + 6
                temp = i
                continue
    return dis


def do_bfs(graph, start_node, key, nodes):
    _dist, visited, queue = [], [], []
    visited.append(start_node)
    queue.append(start_node)
    path_matrix = []
    keyFound = False

    # INITIALIZING A PATH MATRIX WITH ZEROES
    for row in range(1, len(graph) + 1):
        a_row = []
        for col in range(1, len(graph) + 1):
            a_row.append(0)
        path_matrix.append(a_row)
        # EOF : path_matrix

    while queue:
        popped_node = queue.pop(0)
        for neighbor in graph[popped_node]:
            if neighbor not in visited:
                path_matrix[popped_node - 1][neighbor - 1] = 6
                visited.append(neighbor)
                queue.append(neighbor)
                if neighbor == key:
                        keyFound = True
                        break
        if keyFound:
            break
        elif not keyFound and len(queue) == 0:
            print("key unreachable")
            return -1
    distance = cal(key, start_node, path_matrix)
    return distance


def bfs(no_of_nodes, no_of_edges, edge_pair, startNode):
    graph = {}
    _all_nodes, _distances = [], []
    for v1, v2 in edge_pair:  # BUILDING ALL NODES LIST
        if v1 not in _all_nodes:
            _all_nodes.append(v1)
        elif v2 not in _all_nodes:
            _all_nodes.append(v2)
        else:
            continue

    for node in range(1, no_of_nodes + 1):
        if node not in _all_nodes:
            _all_nodes.append(node)

    _all_nodes.sort()
    if _all_nodes[0] == 0:
        _all_nodes.pop(0)
    # FINAL ALL NODES LIST READY

    def get_ngh(_node, _edge_list):
        neigh = []
        for v1, v2 in _edge_list:
            if v1 == _node and v2 not in neigh:
                neigh.append(v2)
            elif v2 == _node and v1 not in neigh:
                neigh.append(v1)
            else:
                continue
        return neigh

    for node in _all_nodes:
        graph[node] = get_ngh(node, edge_pair)

    for a_node in _all_nodes:
        if len(graph[a_node]) == 0:
            _distances.append(-1)
        elif a_node == startNode:
            continue
        else:
            dist = do_bfs(graph, startNode, a_node, _all_nodes)
            # print("dist of node {} is {}".format(a_node, dist))
            _distances.append(dist)
    return _distances


if __name__ == "__main__":
    edge_list = [[1, 2], [1, 3], [2, 1], [6, 3], [1, 4], [2, 5], [5, 6], [6, 7], [5, 6], [3, 6]]
    distance = bfs(7, 10, edge_list, 1)
    print(distance)

"""
    Some pre-prepared graphs :
    
    edge_list = [[1, 2], [1, 3], [2, 4], [2, 5], [3, 6], [3, 7], [5, 8]]
    distance = bfs(9, 7, edge_list, 1)


    edge_list = [[3, 1], [10, 1], [10, 1], [3, 1], [1, 8], [5, 2]]
    distance = bfs(10, 6, edge_list, 3)

    edge_list = [[3, 1], [3, 4], [10, 1], [10, 4], [7, 8], [4, 7], [10, 7]]
    distance = bfs(10, 7, edge_list, 2)



"""
