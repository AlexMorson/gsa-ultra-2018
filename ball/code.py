import collections
import math

def solution(n, c):
    swaps = {i:set() for i in range(n)}
    for u, v in c:
        swaps[u-1].add(v-1)
        swaps[v-1].add(u-1)

    seen = set()
    visit = collections.deque()
    sizes = []
    for i in range(n):
        if i not in seen:
            c = 0
            visit.append(i)
            while visit:
                box = visit.popleft()
                if box not in seen:
                    c += 1
                    seen.add(box)
                    for swappable in swaps[box]:
                        visit.append(swappable)
            sizes.append(c)

    answer = 1
    mod = 10**9 + 7
    for size in sizes:
        answer *= math.factorial(size) % mod
        answer %= mod
    return answer

if __name__ == "__main__":
    with open("downloadable_input.txt", "r") as file:
        n = file.readline().strip()
        c = file.readline().strip()

    n = int(n)
    c = [*map(int, c.split())]
    c = zip(c[::2], c[1::2])

    print(solution(n, c))

