def solution(A, B, K):
    start = A + (K - A) % K
    end = B - (B - K) % K
    return int((end - start) / K + 1)
