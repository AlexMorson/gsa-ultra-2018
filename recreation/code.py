# Too slow :/
def solution(a, b):
    if a == "": return 0

    b = "".join(c for c in b if c in a)
    
    i = 0
    j = 0
    c = 1
    while i < len(a):
        if j >= len(b):
            j = 0
            c += 1
            
        if a[i] == b[j]:
            i += 1
        j += 1
    
    return c

def solution(a, b):
    if a == "": return 0

    a_chars = {c for c in a}

    b = "".join(c for c in b if c in a_chars)

    new_b = {}
    for i, c in enumerate(b):
        if c in new_b:
            new_b[c].append(i)
        else:
            new_b[c] = [i]

    copies = 1
    i = -1
    for c in a:
        for j in new_b[c]:
            if j > i:
                i = j
                break
        else:
            copies += 1
            i = new_b[c][0]

    return copies
    
if __name__ == "__main__":
    a = "ab"*10000
    b = "a" + "c"*10000 + "b"

    with open("downloadable_input.txt", "r") as file:
        a, b = file.readline().split()
