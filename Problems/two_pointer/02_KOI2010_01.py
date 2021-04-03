# KOI_2010_1
#   N개의 정수를 갖는 정렬된 수열에서
#   서로 다른 두 원소를 합애서 0에 가깝게 만들기
#   A [-99][-2][-1][4][98]
#   =>포인터 두개가 양끝에서 다른방향으로 진행하는 것
#   => 정렬될수열이라서 가능한듯?
'''
풀이
    A [-99][-2][-1][4][98]
        L↑             R↑

    L := 더할 원소 중 작은 원소
    R := 더할 원소 중 큰 원소

    다음 두 경우로 나뉨
    1. L+R >0
        => 합이 0에 가까워지기 위해서 더 작아져야 한다. 즉 R을 왼쪽으로 옮긴다
    2. L+R <=0
        => 합이 0에 가까워지기 위해서 더 커져야 한다. 즉 L을 오른쪽으로 옮긴다
'''


def KOI_2010_1():
    A = [-99, -2, -1, 4, 98]
    L = 0
    R = len(A) - 1
    # SUM = -99
    resultArr = []
    RArr = []
    LArr = []
    while L != R:
        SUM = A[L] + A[R]
        print('합 : ', SUM)
        resultArr.append(SUM)
        RArr.append(R)
        LArr.append(L)
        if SUM == 0:
            return print('result:', A[L] + A[R])
        if SUM > 0:
            R -= 1
        if SUM < 0:
            L += 1

    min_val = abs(resultArr[0])
    min_idx = 0
    for i in range(len(resultArr)):
        if abs(resultArr[i]) < min_val:
            min_val = abs(resultArr[i])
            min_idx = i
    print(RArr[min_idx], '+', LArr[min_idx], '=', resultArr[min_idx])

KOI_2010_1()