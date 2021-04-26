import heapq



if __name__ == "__main__":

    # 그래프에 노드를 넣고 첫 노드 부터 탐색

    # 왜 ?

    # 최소 힙큐를 선택하는 이유는 한 노드에서 시작 한 다음 그 다음의 노드를 선택해서 또 탐색할 때의 그 전에 최단거리로 갱신해왔기 때문에

    # 이미 최단거리라면 빠르게 계산을 뛰어넘기 위해서이다.

    # 그리고 탐색하는 것 .

    # 알고리즘의 경우 외워'지는' 것은 좋지만 무작정 외우는 것은 좋지 않다

    n =  6
    s =  4
    a = 6
    b = 2

    fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]

    graph = [[] for i in range(n+1)]

    for fare in fares:
        c, d , cost = fare

        graph[c].append((d,cost))
        graph[d].append((c,cost))

    def dikstra(n, graph, start):

        distances = [float('inf') for i in range(n+1)]

        distances[start] = 0

        q = []


        current_node , current_distance = graph[start]


        heapq.heappush(q,(distances[start],))




    # 최단거리 힙큐를 사용해서 최단 거리에 있는 노드부터 탐색할 수 있으니까