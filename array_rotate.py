A = [3, 8, 9, 7, 6]
B = []
i = 1
def solution(A, K):
    global i
    if(i <= K):
        for item in A:
            C = A.pop()
            B.append(C)
            print(B)
            i = i + 1
    B.reverse()        
    B.extend(A)
    print(B)
solution(A, 3)          

