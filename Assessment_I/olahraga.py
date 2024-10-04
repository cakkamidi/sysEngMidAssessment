N, M = map(int, input().split())

A = list(map(int, input().split()))

B = list(map(int, input().split()))

while True:
    candidates = [a for a in A if a <= M]
    
    if not candidates:
        break
    
    max_a = max(candidates)
    index = A.index(max_a)
    
    M += B[index]
    
    A.pop(index)
    B.pop(index)

print(M)