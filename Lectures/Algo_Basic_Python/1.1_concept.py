# https://www.inflearn.com/course/파이썬-알고리즘-기초/dashboard
'''
    알고리즘이란 ?
        어쩐 문제의 '모든 입력 사례'에 대해서 해답을 찾아주는 단계별 절차

    ex)
    > 순차탐색문제
        문제    : 어떤 수 x가 n개의 수로 구성된 리스트 S에 존재하는가?
        해답    : x가 존재하면 x의 인덱스가, 존재하지 않으면 0이 해답(반환)
        파라미터 : 정수 n(>0), 리스트 S(인덱스 범위는 1부터 n까지), 원소 x
        입력사례 : S = [0, 10, 7, 11, 5, 13, 8], n = 6, x = 5
        입력해답 : location = 4
        알고리즘 : 모든 S에 대해서 x의 인덱스를 찾아주는 단계별 절차
            - S의 첫째원소에서 시작하여 x를 찾을 때까지
            - 각 원소를 차례로 x와 비교한다.
            - 만약 x를 찾으면 x의 인덱스를 리턴하고
            - x를 찾지 못하면 0을 리턴한다.
'''
def seqsearch(n, S, x) :
    location = 1
    while(location <=n and S[location] !=x ) :
        location += 1
    if (location > n) :
        location = 0
    return location

'''
    > 리스트 원소의 합 구하기
    알고리즘 : S의 모든 원소를 차례대로 sum에 더하는 절차
        - sum을 0으로 초기화
        - 모든 S의 원소에 대해서 sum += S[i]를 실행
        - sum 값 리턴
'''
def sum(n, S) :
    result = 0
    for i in range(1, n+1):
        result = result + S[i]
        return result

'''
   > 리스트의 정렬문제 : 다양한 해법이 있음!
   알고리즘 : 모든 S에 대해서 S'를 찾아주는 단계별 철차
    - 교환정렬, 삽입정렬, 선택정렬, 합병정렬, 퀵정령 기타 등등.
    
    > 교환정렬로 구현! (가장간단)
'''
def exchange(S) :
    n = len(S)
    for i in range(n-1):
        for j in range(i+1,n):
            if(S[i]>S[j]):
                S[i], S[j] = S[j], S[i] # swap! python 개꿀

'''
 > 행렬의 곱셈문제 : 두 n X n 행렬의 곱을 구하시오(정방행렬)
    알고리즘 : 
        Cij = ∑a(ik)b(kj) : 3중 for문
'''
def matrixmult(n,A,B) :
    n = len(A)
    C = [[0]*n for _ in range(n)] #파이썬으로 이중배열 초기화하는방법!!
    for i in range(r):
        for j in range(n):
            for k in range(n):
                c[i][j] += A[i][k]*B[k][j]