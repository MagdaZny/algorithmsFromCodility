def solution(A):
    half_of_a_sum = sum(A)/2
    differencies = [0] * (len(A)-1)
    acc_sum = 0
    for index in range(0, len(A)-1):
        acc_sum = acc_sum + A[index]
        differencies[index] = abs(half_of_a_sum - acc_sum)
    return int(min(differencies)*2)
