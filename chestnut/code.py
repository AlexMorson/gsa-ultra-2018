def solution(t_n, t_a, t_b, t_x, t_y):
    def alice_wins(n, a, b, x, y):
        # With 1, 2 or 3 chestnuts left, we win
        a_wins = [True, True, True]
        b_wins = [True, True, True]

        for offset in range(1, n-2):
            # If we can't make a move then we've lost
            new_a = False
            for i in (0, 1, 2):
                if (i+offset) % a == 0 or (i+offset) % b == 0:
                    continue
                if not b_wins[i]:
                    new_a = True
                    break

            new_b = False
            for i in (0, 1, 2):
                if (i+offset) % x == 0 or (i+offset) % y == 0:
                    continue
                if not a_wins[i]:
                    new_b = True
                    break

            a_wins = a_wins[1:] + [new_a]
            b_wins = b_wins[1:] + [new_b]

        return a_wins[2]

    total = 0
    for n, a, b, x, y in zip(t_n, t_a, t_b, t_x, t_y):
        if alice_wins(n, a, b, x, y):
            total += 1

    return total + 123

if __name__ == "__main__":
    t_n = (23, 12, 37, 79, 20)
    t_a = (4, 2, 4, 6, 3)
    t_b = (5, 3, 5, 6, 16)
    t_x = (3, 6, 4, 6, 7)
    t_y = (6, 15, 5, 6, 8)

    print(solution(t_n, t_a, t_b, t_x, t_y))
