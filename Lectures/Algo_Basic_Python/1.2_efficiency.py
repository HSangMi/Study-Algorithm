'''
1.2 알고리즘의 효율성

    알고리즘의 성능 : '시간'과 '공간'의 사용량의 효율성

        ex) 순차탐색 vs 이분탐색
        : 입력 리스트의 조건에 따른 탐색 알고리즘의 선택
          - 정렬되지 않은 리스트에서 키 찾기 : 순차탐색 (n)
          - 정렬된 리스트에서 키 찾기 : 이분검색 log(n+1)
'''

'''
    > 이분검색
        - 주어진 리스트 S(정렬된)와 키 x에 대해서,
        - 먼저 x를 리스트 중앙에 위치한 원소와 비교
        1) 만약 같으면, 찾았음
        2) x보다 작으면, 왼쪽에 있을것임
            - 왼쪽리스트에서 다시 재귀호출
        3) x보다 크면, 오른쪽에 있을거임
            - 오른쪽 리스트에서 다시 재귀 호출
        3) 더이상 찾을 리스트가 없으면 알고리즘 종료
'''
def binsearch(n, S, x):
    low = 1         #start
    high = n        #end
    location = 0    #정답!
    while (low <= high and location == 0):
        mid = (low+high) // 2
        if (x == S[mid]):
            location = mid
        elif (x<S[mid]):
            high = mid -1
        else
            low = mid + 1
    return location

'''
    > 피보나치 수열의 n번째 항 구하기 : 재귀!
        알고리즘: 재귀적 정의를 그대로 구현!
            f0 = 0, f1 = 1
            f(n) = f(n-1) + f(n-2)
'''
def fib(n):
    if (n<=1):
        return n
    else:
        return fib(n-1)+fib(n-2)

for i in range(11):
    print(fib(i), end=1)

# 재귀적 정의 이용 > 작성하기도 쉽고, 이해하기도 쉬움!
# 그러나 비효율적!!
# 비효율성을 개선하려면 ! 중복계산을 피해야함!
# 이미계산한 값은 리스트에 저장하고, 필요할때 꺼내쓰기!
def fib2(n):
    f = [0]*(n+1)
    if (n > 0):
        f[1] = 1
        for i in range(2, n+1):
            f[i] = f[i-1]+f[i-2]
    return f[n]
for i in range(11) :
    print(fib2(i), end=" ")