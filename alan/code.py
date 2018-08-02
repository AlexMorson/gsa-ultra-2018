def solution(tests):
    def non_zero(n, edges, target):
        target = {u-1 for u in target}
        in_deg = [0 for _ in range(n)]
        open_nodes = set()
        edges_dict = {i:[] for i in range(n)}

        for u, v in edges:
            in_deg[v-1] += 1
            edges_dict[u-1].append(v-1)

        for i in range(n):
            if in_deg[i] == 0:
                open_nodes.add(i)

        while open_nodes:
            choose = open_nodes.difference(target)
            if choose:
                u = choose.pop()
                open_nodes.remove(u)

                for v in edges_dict[u]:
                    in_deg[v] -= 1
                    if in_deg[v] == 0:
                        open_nodes.add(v)
            else:
                return target == open_nodes

    total = 0
    for i, test in enumerate(tests):
        n, edges, target = test
        if non_zero(n, edges, target):
            total += 2**i

    return total

if __name__ == "__main__":
    t = (
        (2, ((1, 2),), (1,)),                                           # True
        (2, ((1, 2),), (2,)),                                           # True
        (3, ((1, 2),), (3,)),                                           # True
        (3, ((1, 2), (1, 3)), (1,)),                                    # True
        (3, ((1, 2), (2, 3)), (2, 3)),                                  # False
        (6, ((1, 3), (1, 4), (3, 6), (3, 4), (4, 5)), (5, 6, 3)),       # False
        (6, ((1, 3), (1, 4), (3, 6), (3, 4), (4, 5)), (5, 6, 3, 1)),    # False
        (6, ((1, 3), (1, 4), (3, 6), (3, 4), (4, 5)), (5, 2, 3, 1)),    # False
        (5, ((1, 3), (2, 3), (3, 4), (2, 5), (5, 4)), (1, 2, 5)),       # False
        (6, ((1, 3), (1, 4), (3, 6), (3, 4), (4, 5)), (1,)),            # True
        (6, ((1, 3), (1, 4), (3, 6), (3, 4), (4, 5)), (5, 2, 6, 3, 1)), # False
        (5, ((1, 3), (2, 3), (3, 4), (2, 5), (5, 4)), (1, 5))           # True
    )
    print(solution(t))
    # 2575
