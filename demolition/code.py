import collections

def solution(n, xs, rs):
    remaining = dict(enumerate(xs))
    to_explode = collections.deque()
    sorted_rs = sorted(range(n), reverse=True, key=lambda i:rs[i])

    c = 0

    for i in sorted_rs:
        if i in remaining:
            print(f"Detonating bomb {i} ({xs[i]}, {rs[i]})")
            to_explode.append(i)
            del remaining[i]
            c += 1

        while to_explode:
            i = to_explode.pop()
            
            for j, x in [*remaining.items()]:
                if xs[i]-rs[i] <= x <= xs[i]+rs[i]:
                    print(f"Which detonated bomb {j} ({xs[j]}, {rs[j]})")
                    to_explode.append(j)
                    del remaining[j]

    return c*10000

if __name__ == "__main__":
    with open("downloadable_input.txt", "r") as file:
        n, x, r = file.read().strip().split("\n")
    n = int(n)
    x = [*map(int, x.split())]
    r = [*map(int, r.split())]

    print(solution(n, x, r))
