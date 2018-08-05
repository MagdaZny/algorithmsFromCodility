def solution(A):
    sum = 0
    for elem in A:
        sum = sum ^ elem
    return sum
