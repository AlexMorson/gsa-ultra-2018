def score(s):
    chars = {}
    for c in s:
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1

    total = 0
    has_odd = False
    for c, n in chars.items():
        if n % 2 == 1:
            has_odd = True
            total += n-1
        else:
            total += n
    if has_odd:
        total += 1

    return total

# For testing the hypothesis that the optimal way to split into 4 parts can be
# found by looking at the optimal way of splitting into 2 parts (false, btw!)
def brute_force_2(s):
    best_score = 1e100
    best_splits = None

    for i in range(1, len(s)):
        cur_score = score(s[:i]) + score(s[i:])
        if cur_score < best_score:
            best_score = cur_score
            best_splits = [(s[:i], s[i:])]
        elif cur_score == best_score:
            best_splits.append((s[:i], s[i:]))

    print(best_splits)
    return best_score

def brute_force_4(s):
    best_score = 1e100
    best_splits = None

    c = 0
    for i in range(1, len(s)-2):
        for j in range(i+1, len(s)-1):
            for k in range(j+1, len(s)):
                c += 1
                print("\r",c, end="")
                cur_score = score(s[:i]) + score(s[i:j]) + score(s[j:k]) + score(s[k:])
                if cur_score < best_score:
                    best_score = cur_score
                    best_splits = [(s[:i], s[i:j], s[j:k], s[k:])]
                elif cur_score == best_score:
                    best_splits.append((s[:i], s[i:j], s[j:k], s[k:]))

    print(best_splits)
    return best_score

def solution(s):
    n = len(s)

    scores = [] # scores[i][j] = score(s[i:i+j+1])
    for start in range(len(s)):
        chars = {}
        num_odd = 0
        cur_score = 0
        line = []
        for c in s[start:]:
            num = chars.get(c, 0)
            if num % 2 == 0:
                num_odd += 1
                if num_odd == 1:
                    cur_score += 1
            else:
                num_odd -= 1
                cur_score += 2
                if num_odd == 0:
                    cur_score -= 1
            chars[c] = num+1

            line.append(cur_score)
        scores.append(line)

    optimal_endings = [] # Optimal (min) score for one split of s[i:]
    for start in range(len(s)-1):
        optimal_endings.append(min(scores[start][split-start-1] + scores[split][n-split-1] for split in range(start+1, len(s))))

    best_score = 1e100
    for i in range(1, n-2):
        for j in range(i+1, n-1):
            cur_score = scores[0][i-1] + scores[i][j-i-1] + optimal_endings[j]
            if cur_score < best_score:
                best_score = cur_score
    
    return best_score

if __name__ == "__main__":
    with open("downloadable_input.txt", "r") as file:
        s = file.readline().strip()

    print(solution(s))
