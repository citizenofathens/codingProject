def solution(n, computers):


    bfs = []
    # 시작 노드 입력
    bfs.append(0)
    network_cnt = 0
    visited = [0] * n

    while 0 in visited:
        # 어떤 위치의 0이든 상관없다

        bfs.append(visited.index(0))
        while bfs:
            node = bfs.pop(0)
            # node는 인덱스
            visited[node] = 1


            for i in range(len(computers)):
                if visited[i] == 0 and computers[node][i] == 1:
                    bfs.append(i)
                    visited[i] = 1


        network_cnt += 1

    return network_cnt

# 비슷하지 않은 다른 사람 풀이
#
def solution_(n, computers):
    temp = []
    for i in range(n):
        # 네트워크 숫자
        temp.append(i)
    print(temp)
    for i in range(n):
        for j in range(n):
            if computers[i][j]:
                for k in range(n):
                    # 각각의 네트워크 개수 n 길이의  0,1, 2, 3,,,,n 숫자 각각을 네트워크라고 생각하고
                    # 완전 탐색을 하며 어떤 네트워크인지 정해주는 과정
                    # 똑같은 값으로 계속 바뀌기도 하며 '탐색'하는 과정
                    # 단순해보이는 코드에 속지 말고 그 안에 녹아있는 개념을 봐야한다
                    # 서로 연결되어있는 노드라면 k는 순환 컴퓨터인덱스이고 i는 고정 컴퓨터인덱스.
                    # 양 쪽이 1이나 0을 가지는 케이스라면
                    # 예를 들어 순환 컴퓨터배열 인덱스와 고정 컴퓨터배열 인덱스의 값이 같다면
                    # for문 처음에는 최초에 k와 i가 0 값으로 같으므로 k인덱스값 0에 0이들어간다
                    # temp[0, 순환컴퓨터배열 k값에 연결 컴퓨터 인덱스 값을 담고 k값이 회전할 때 또 그 컴퓨터 값이 될 때 네트워크를 찾는다
                    # 여기까지가 내 고민

                    # 아니 '애초에 가정 자체가' 이 for문을 돈다는 것은 computers[i][j]가 true.라는 것은 i번째 컴퓨터와 j번째가 연결 되어있다는 뜻이다. 이게 더 중요하다 . 그 이전 맥락
                    # 그렇다면 k를 순회하면서 i번째 네트워크에 속하는 k값인덱스 네트워크 값을 j번째 컴퓨터가 속한 네트워크 값으로 맞춰줘서 같은 네트워크에 있다는 것을 표시해준다.




                    # 탐색 과정을 보면 처음에 모든 값은 0 , 이미 알려진 첫 번째 노드 자기 자신이고 그 이후 j가 1일때, 2번째 컴퓨터를 탐색할 때
                    # 기준인 k번째에 컴퓨터 i번째 네트워크에 속하고(0) k번째에
                    # 아니 computers[i][j] 는 true를 뜻하는 것이고
                    #
                    # 그 때의 컴퓨터 인덱스 값 j를 가져와서 해당 네트워크
                    if temp[k] == temp[i]:
                        temp[k] = temp[j]


    return len(set(temp))

if __name__ == '__main__':

    solution_(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]])

