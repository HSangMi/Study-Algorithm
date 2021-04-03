# 핵심노트
# https://www.youtube.com/watch?v=rI8NRQsAS_s&list=PLRx0vPvlEmdAZ6xXAUyBbLQa2-Ideakb-&ab_channel=%EB%8F%99%EB%B9%88%EB%82%98
'''
배열의 특정 '연속된' 구간을 처리하는 경우
 * 문제에서 연속된 데이터 구간을 처리하기를 원한다면?
 * 다양한 접근 방법을 떠올려 보는 것이 중요합니다!
 * 자주 사용 되는 기법 : 투 포인터, 구간 합
'''
'''
문제 1) 특정 합을 가지는 부분 연속 수열 찾기
[문제 설명]
* N개의 자연수로 구성된 수열이 있습니다.
* 합이 M인 부분 연속 수열의 개수를 구해보세요.
* 시간제한 : O(N)
[문제 해결 방법]
* 투 포인터 방법 : 리스트에 순차적으로 접근해야 할 때 두개의 점을 이용해 위치를 기록하면서 구하는 기법

[알고리즘 설명]
1. 시작점(S)와 끝점(E)이 첫 번째 원소의 인덱스(0)를 가리키도록 한다.
2. 현재 부분 합이 M과 같다면, 카운트 한다.
3. 현재 부분 합이 M보다 작거나 같다면, end를 1증가시킨다.
4. 현재 부분합이 M보다 크다면, start를 1증가시킨다.
5. 모든 경우를 확인 할때까지 2번부터 4번의 과정을 반복한다.

 S                          S
 ↓                          ↓
[1][2][3][4][5]         [1][2][3][4][5]
 ↑                             ↑
 E                             E
'''


# 데이터 개수 N과 부분 연속 수열의 합 M을 입력받기
def two_pointers():
    n, m = 5, 5
    data = [1, 2, 3, 2, 5]

    result = 0
    summary = 0
    end = 0
    # start 를 차례대로 증가시키며 반복
    for start in range(n):
        print('start커서!! :', start)
        print('summary!! :', summary)
        # end를 가능한 만큼 이동시키기
        while summary < m and end < n:
            print('  while문 : end커서:', end)
            summary += data[end]
            print('     현재 summary : ', summary)
            end += 1

        # 부분 합이 m일 때 카운트 증가
        if summary == m:
            print('  if 문 : summary == m?? :', start, '부터', end - 1)
            result += 1
        # 다음 start 로 넘어가기 전에
        summary -= data[start]
        # print('다음계산할 summary : ', summary)
        print('----------------------------------')

    print(result)
    print('end Program..')


'''
>> 구간 합 빠르게 계산하기 <<
[문제 설명]
- 아래와 같이 N개의 정수로 구성된 수열이 있습니다.
- M개의 쿼리(Query) 정보가 주어집니다.
    - 각 쿼리는 L과 R로 구성됩니다.
    - [L, R] 구간에 해당하는 데이터들의 합을 모두 구하는 문제입니다.
- 시간제한: O(N+M)

[문제 해결 방법]
- 접두사 합(Prefix Sum)
    : 구간의 합을 빠르게, 여러번 구하고자 할때, 테이블을 만들어서 각 구간의 합을 빠르게 구하는 방법

[Prefix Sum을 활용한 알고리즘 설명]
1. Prefix Sum을 계산하여 배열 P에 저장한다.
2. 매 M개의 쿼리 정보를 확인 할 때, 구간 합은 P[R] - P[L-1]이다

        [ 10][ 20][ 30][ 40][ 50]
                ↓ Prefix Sum 계산
 P [  0][ 10][ 30][ 60][100][150]

    ex) 1) L = 1, R = 3  → P[3] - P[1-1] = 60
        2) L = 2, R = 5  → P[5] - P[2-1] = 140
                ...
        2) L = 3, R = 4  → P[4] - P[3-1] = 70
'''


def prefix_sum01():
    # 데이터의 개수 N과 데이터 입력받기
    n = 5
    data = [10, 20, 30, 40, 50]

    # Prefix Sum 배열 계산
    summary = 0
    prefix_sum = [0]
    for i in data:
        summary += i
        prefix_sum.append(summary)
    # 구간 합 계산
    left = 3
    right = 4
    print(prefix_sum[right] - prefix_sum[left - 1])


prefix_sum01()


def practice():
    n, m = 5, 5
    data = [1, 2, 3, 2, 5]
    #        0  1  3  6  8  13
    result = 0
    summary = 0
    end = 0

    prefix_sum = [0]
    for i in data:
        summary += i
        prefix_sum.append(summary)

    # start 를 차례대로 증가시키며 반복
    for start in range(n):
        # end를 가능한 만큼 이동시키기
        for end in range(start + 1, n + 1):
            print('start:', start, ', end:', end)
            if prefix_sum[end] - prefix_sum[start] == m:
                print('  if 조건일치 : ', start, end)
                result += 1
        print('-----------------------')
    print(result)
    print('end Program..')


practice()
