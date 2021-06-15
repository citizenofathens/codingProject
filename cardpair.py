# https://youtu.be/FX9n1PFv2K4?t=3338 clone coding. not my code

import itertools ,copy, collections


def solution(board, r, c):
    # i값과 상관없이 반복문을 실행하여 이차원 리스트를 만든다
    occur = [[] for i in range(7)]
    # 완전 탐색할 카드 페어 리스트
    brute =[]

    # 2중 for문 순회하며 board 에서 찾을 카드 페어가 있는 지를 찾는다
    for i in range(4):
        for j in range(4):
            # 빈 공간이라면 아래 코드는 실행하지 않고 넘어간다
            if board[i][j] == 0 : continue
            # 경우의 수 리스트에 해당하는 카드 (카드 번호는 6까지) 가 있다면
            # 완전 탐색리스트에 추가하고  이러면 중복 추가 되지 않나?
            if occur[board[i][j]]: brute.append(board[i][j])
            # 차례대로 순회하며 도는 것이므로 해당 카드 번호 리스트에 발견 순서대로 위치를 찍어준다
            occur[board[i][j]].append((i,j))

    n = len(brute)
    ans = 9999999
    for p in itertools.permutations(brute):
        # 주소가 아닌 값을 복사 deepcopy
        myboard = copy.deepcopy(board)

        d = [[0] * 2 for i in range(n)]
        # dist 함수로 거리를 구함 d[0][0] 은 왼쪽에서 오른쪽으로 가는 순서로 구한다고 미리 정의
        # 최초 스타트 지점 r,c 에서 occur[p[0]][0] 먼저 발견된 카드 페어 0 위치로 가는 것을 구함
        # 카드는 항상 쌍이므로 0번째 1번째가 있다
        # 스타트 지점에서 처음 발견된 카드 그 이후 발견된 카드순으로 찾는 순서의 거리 저장
        # 알고리즘 처음 설명하는 개념 참고
        d[0][0] = dist(myboard, (r,c), occur[p[0]][0])
                    +dist(myboard, occur[p[0]][0] , occur[p[0]][1])
        # d는 dp배열로 d[0][1]은 오른 쪽에서 왼쪽으로 가는 것이라고 정함

        d[0][1]