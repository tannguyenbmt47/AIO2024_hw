def levenshtein_distance(source, target):

    # step 1
    M = len(source) + 1
    N = len(target) + 1
    D = [[0] * N for _ in range(M)]

    # step 2
    for i in range(M):
        D[i][0] = i
    for j in range(N):
        D[0][j] = j

    # step 3
    for i in range(1, M):
        for j in range(1, N):
            cost = 0 if source[i-1] == target[j-1] else 1
            D[i][j] = min(
                D[i-1][j] + 1,
                D[i][j-1] + 1,
                D[i-1][j-1] + cost
            )

    # step 4
    return D[M-1][N-1]


if __name__ == "__main__":
    source = "hola"
    target = "hello"

    print("Khoảng cách Levenshtein giữa '{}' và '{}' là: {}".format(
        source, target, levenshtein_distance(source, target)))
