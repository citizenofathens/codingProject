import heapq



if __name__ == "__main__":


    # n이 셀 수 있는 범위이면 완전 탐색 대상인지 생각

    # q 에 dist 와 start 지점 큐를 최초 삽입

    # 항상 최소거리부터 탐색하기 위하여 파이썬 heapq 사용 최소힙이 default인 큐이다

    # 그래프에 노드를 넣고 첫 노드 부터 탐색

    # 왜 ?

    # 최소 힙큐를 선택하는 이유는 한 노드에서 시작 한 다음 그 다음의 노드를 선택해서 또 탐색할 때의 그 전에 최단거리로 갱신해왔기 때문에

    # 이미 최단거리라면 빠르게 계산을 뛰어넘기 위해서이다.

    # 그리고 탐색하는 것 .

    # 알고리즘의 경우 외워'지는' 것은 좋지만 무작정 외우는 것은 좋지 않다


    def dikstra(n, graph, start):


        distances = [float('inf') for i in range(1,n+1)]

        distances[start] = 0

        q = []



        heapq.heappush(q,(0,start))

        while heapq:

           dist, node =  heapq.heappop(q)

           if distances[node] < dist:
               continue


           for i in graph[node]:
               # 현재 큐에서 뽑은 노드의 그래프 노드 탐색전(?)

               # 그래프 노드의 거리와 해당 노드
               stopover_dist = i[0]
               stopover_node = i[1]

               # 현재 저장된 거리 배열에 저장된 그래프 노드 까지의 거리가 현재 노드까지 온 후에 현재 노드의 그래프로 이어진 거리보다 작다면 업데이트 할 필요가 없다
               if distances[stopover_node] < distances[node] + stopover_dist:
                    pass
               if distances[stopover_node] > distances[node] + stopover_dist:
                   distances[stopover_node]  = distances[node] + stopover_dist

                   #해당 그래프 노드는 발견된 노드이므로 이후에 현재 노드가 완료된 이후 시작점이 되어 똑같이 탐색하기 위해 최단거리를 먼저 뽑기 위해 최소힙큐에 저장
                   heapq.heappush(q,(stopover_dist,stopover_node))


        return  distances



    def solution(n, s, a,  b , fares):



        graph = [[] for i in range(n + 1)]


        for fare in fares:
            c, d, cost = fare
            # fares 배열에 두 지점 간 예상 택시요금은 1개만 주어집니다. 즉, [c, d, f]가 있다면 [d, c, f]는 주어지지 않습니다 -> 내가 만든다
            graph[c].append((d, cost))
            graph[d].append((c, cost))


        distances_init = dikstra(n, graph, s)

        dist_a = distances_init[a]
        dist_b = distances_init[b]

        for node in range(1,n+1):

            distances = dikstra(n,graph,node)

            if  dist_a + dist_b < distances_init[node]+ distances[a] + distances[b]: # node == s  인 경우 pass 하도록 고려하지 않았다. 알고리즘 내에서도 가능한 모든 가능성 고려해야 함 효율성
                return dist_a + dist_b
            else:
                return distances_init[node]+ distances[a] + distances[b]









    # 최단거리 힙큐를 사용해서 최단 거리에 있는 노드부터 탐색할 수 있으니까