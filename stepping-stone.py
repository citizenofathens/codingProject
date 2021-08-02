

# 이 문제로 논리가 스텝 바이 스텝으로 이어지는 것을 배웠다 논리 과정이 이어지는 것 알기
def solution(distance, rocks, n):

    """

    :param distance: 목표 지점까지의 거리
    :param rocks: 바위가 놓인 위치
    :param n: 바위를 제거하는 개수
    :return: n 값을 만족하는 지점 간 거리의 최솟값 중 최댓값
    """
    rocks = sorted(rocks)
    left = 0
    right = distance




    while left<=right: # left == mid == right 가 종료 조건이므로 그 이후는 수행하지 않는다



        # 답을 mid 라고 가정하고 탐색한다

        mid = (left + right) // 2
        # 각 단계의 최솟값
        min_distance = float('inf')
        current = 0
        remove_cnt = 0

        # min값과 지점 간의 거리를 비교하는 로직

        # 한번에 답을 찾을 수는 없으므로 정답이라고 가정한 거리를 기점으로 바위를 제거하면서 바위를 지울 지 거리를 늘려볼 지 탐색하고 정답까지의 거리를 좁혀나간다
        for rock in rocks:
            # 현재 지점 부터 바위까지의 거리
            diff = rock - current
            # 바위를 제거하는 거리의 최댓값 mid 보다 작은 거리인 바위를 지운다고 가정한다
            if diff < mid:
                remove_cnt +=1
            else:
                current = rock
                min_distance = min(min_distance,diff) # 해당 바위로 넘어 가므로 이전의 diff 를 저장
        # 너무 많이 지웠다면 길이를 줄인다
        if remove_cnt > n:
            # right를 mid -1로 옮긴다 그 이상의 거리는 모두 바위를 n값보다 많이 지우게 되므로 제외시킨다
            right = mid -1
        else:
            # left를 mid +1로 옮긴다 그 이하의 거리는 바위를 제거하는 개수 n을 충족 시킬 수 없거나 최솟값 중 최댓값 아닐 수 있으므로 제외된다
            # 바위 개수는 충족했고 개수를 맞추면서 최댓값을 충족 시킬 수 있는 지 찾는다
            answer =min_distance
            left = mid + 1

        #구간이 옮겨졌다

    return answer