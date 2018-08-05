def solution(A):
    zeros = 0;
    acc = 0
    for elem in A:
        if elem == 0:
            zeros += 1
        else:
            acc += zeros
        if acc > 1000000000:
            return -1
    return acc
