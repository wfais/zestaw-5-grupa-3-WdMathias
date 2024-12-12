from itertools import product



def maximize_expression(K, M, lists):
    # twoj kod tutaj
    maximum = 0
    for i in product(*lists):
        s = sum(x**2 for x in i) % M
        if s > maximum:
            maximum = s
    return maximum
 



if __name__ == "__main__":
    K, M = map(int, input().rstrip().split())

    lists = [list(map(int, input().rstrip().split()[1:])) for _ in range(K)]

    result = maximize_expression(K, M, lists)
    print(result)
