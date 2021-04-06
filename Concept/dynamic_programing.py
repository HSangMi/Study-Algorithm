'''
다이나믹 프로그래밍 : 알고리즘 x, 접근방식 O
    - 점화식
    - 큰 문제를 작은문제를 사용해 해결하는 방법
    - 과거에 구한 해를 활욯하는 방법
    - 메모이제이션
    => 재귀적으로 생각하기 + 불필요한 계산 줄이기

재귀적이란?
    := 귀납적 ( 작은 문제는 해결되어 있다는 믿음을 가지고 큰 문제를 해결하는 방법 )

    1 + 3 + 5 + ... + (2n-1) = n^2

    1) n=1 일떄 참이고
    2) n=k 가 참이라고 가정했을때
    3) n=k+1 일때도 참이라면, 해당 명제는 참

    ex) 피보나치수열
    f0 = 1,
    f1 = 1,
    f(n) = f(n-1) + f(n-2)
    => 이것을 그냥 구현하게 되면 불필요한 계산이 너무 많음!!
    => 이것을 해결하기위한 기법이
    => 1. '메모이제이션' => 이미 했던 계산은 다시하지 않는다.
    => 2. 밑에서부터 계산하기

'''


# 피보나치
def fibo(n):
    if n == 0: return 1
    if n == 1: return 1
    return fibo(n - 1) + fibo(n - 2);


# 피보나치 + 메모이제이션
memo = [0] * 10000


def fibo1(n):
    if n == 0: return 1
    if n == 1: return 1
    if memo[n] != 0: return memo[n]
    memo[n] = fibo1(n - 1) + fibo1(n - 2);
    return memo[n];


# 피보나치 + 밑에서부터 계산하기

fi = [0] * 1000


def fibo2(n):
    fi[0] = 1
    fi[1] = 1
    for i in range(2, 1000):
        fi[i] = fi[i - 1] + fi[i - 2]

# https://www.youtube.com/watch?v=bzfm8SO4j9I&list=PLN3yisVKGPfhmFpkSEwsWZOZDJ3UUojEA&index=2&ab_channel=IOIKOREA