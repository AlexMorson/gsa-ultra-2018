import collections
import itertools

def solution(n, m):
    def find_landmarks():
        keys = {"R":[], "G":[], "B":[]}
        for y in range(n):
            for x in range(n):
                t = m[y][x]
                if t == "S":
                    start = (x, y)
                elif t == "C":
                    cheese = (x, y)
                elif t not in {"W", "."}:
                    keys[t].append((x, y))
        return start, cheese, keys

    def get_distances(origin):
        visited = {origin}
        explore = collections.deque([(origin, 0)])
        distances = {}
        while explore:
            (x, y), dist = explore.popleft()

            t = m[y][x]
            if t != ".":
                distances[(x, y)] = dist

            for new_x, new_y in ((x-1, y), (x, y-1), (x+1, y), (x, y+1)):
                if (new_x, new_y) in visited:
                    continue

                if 0 <= new_x < n and 0 <= new_y < n and m[new_y][new_x] != "W":
                    explore.append(((new_x, new_y), dist+1))
                    visited.add((new_x, new_y))

        return distances

    # Get the locations of the important tiles
    start, cheese, keys = find_landmarks()

    # Find the distance to important tiles from the start and end
    distances = {}
    distances[start] = get_distances(start)
    distances[cheese] = get_distances(cheese)

    # Remove keys that are not reachable
    keys = {colour:[tile for tile in locations if tile in distances[start]] for colour, locations in keys.items()}

    # Find closest key of each colour
    best_tiles = []
    for colour, locations in keys.items():
        best_dist = 1e100
        best_tile = None
        for tile in locations:
            dist = distances[start][tile] + distances[cheese][tile]
            if dist < best_dist:
                best_dist = dist
                best_tile = tile
        best_tiles.append(best_tile)

    # BFS from each of the keys
    for tile in best_tiles:
        distances[tile] = get_distances(tile)

    # Make a 'good' route from these tiles
    best_length = 1e100
    for t1, t2, t3 in itertools.permutations(best_tiles):
        length = distances[start][t1] + distances[t1][t2] + distances[t2][t3] + distances[t3][cheese]
        if length < best_length:
            best_length = length

    # Ignore keys further than this distance
    keys = {colour:[tile for tile in locations if distances[start][tile] + distances[cheese][tile] <= best_length] for colour, locations in keys.items()}

    # Calculate distances for all remaining keys
    for key in itertools.chain.from_iterable(keys.values()):
        if key not in distances:
            distances[key] = get_distances(key)

    # Brute force the rest
    best_length = 1e100
    for red_key in keys["R"]:
        for green_key in keys["G"]:
            for blue_key in keys["B"]:
                for k1, k2, k3 in itertools.permutations([red_key, green_key, blue_key]):
                    length = distances[start][k1] + distances[k1][k2] + distances[k2][k3] + distances[k3][cheese]
                    if length < best_length:
                        best_length = length

    return best_length

if __name__ == "__main__":
    with open("downloadable_input.txt", "r") as file:
        n = file.readline().strip()
        m = file.read().strip()

    n = int(n)
    m = m.split("\n")

    x = solution(n, m)
