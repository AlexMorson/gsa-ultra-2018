def solution(s):
    N = len(s)
    def starting_at(n):
        def different(c):
            return c["R"] != c["Y"] and c["R"] != c["B"] and c["Y"] != c["B"]

        cols = {"R":0, "Y":0, "B":0}
        while cols["R"] == 0 or cols["Y"] == 0 or cols["B"] == 0: 
            cols[s[n]] += 1
            n += 1
            if n >= N:
                return 0

        count = 0
        if different(cols): count += 1
        while n < N:
            cols[s[n]] += 1
            if different(cols): count += 1
            n += 1

        return count

    return sum(starting_at(i) for i in range(N)) + 10000 # <- Forgot the 10000 in the comp D':

if __name__ == "__main__":
    with open("downloadable_input.txt", "r") as file:
        s = file.read().strip()

    print(solution(s))
