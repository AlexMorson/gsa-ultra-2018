import itertools

# Slow and memory inefficient one
def solution(n, m, r, c, k):
    def get_spaces(l):
        spaces = []
        current = l[0]
        for x in l[1:]:
            if x-current > 1:
                spaces.append(x-current-1)
            current = x
        return spaces
    
    # Spaces between walls
    heights = sorted(get_spaces(r))
    widths = sorted(get_spaces(c))

    areas = sorted([w*h for w in widths for h in heights])

    return areas[k-1]

def solution(n, m, r, c, k):
    def get_spaces(l):
        spaces = []
        current = l[0]
        for x in l[1:]:
            if x-current > 1:
                spaces.append(x-current-1)
            current = x
        return spaces
    
    # Spaces between walls
    heights = sorted(get_spaces(r))
    widths = sorted(get_spaces(c))

    # Run length encoded [(x, n)]
    heights = [(k, len(list(g))) for k, g in itertools.groupby(heights)]
    widths = [(k, len(list(g))) for k, g in itertools.groupby(widths)]
    
    areas = {}
    for h, hc in heights:
        for w, wc in widths:
            if w*h not in areas:
                areas[w*h] = wc*hc
            else:
                areas[w*h] += wc*hc

    area_list = sorted(areas.items(), key=lambda x:x[0])

    i = 0
    while k > 0:
        k -= area_list[i][1]
        i += 1
    
    return area_list[i-1][0]

if __name__ == "__main__":
    with open("downloadable_input.txt", "r") as file:
        n, r, c, k = file.read().strip().split("\n")
    n, m = [*map(int, n.split())]
    r = [*map(int, r.split())]
    c = [*map(int, c.split())]
    k = int(k)

    print(solution(n, m, r, c, k))
    #37248
