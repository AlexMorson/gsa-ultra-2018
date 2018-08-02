def solution(a):
    squares = {str(x*x) for x in range(32)}
    def almost_square(n):
        n = str(n)
        for i in range(len(n)):
            if n[:i] + n[i+1:] in squares:
                return True
        return False
    
    c = 0
    for n in range(10, a+1):
        if almost_square(n):
            c += 1
    return c

if __name__ == "__main__":
    print(solution(1234))
