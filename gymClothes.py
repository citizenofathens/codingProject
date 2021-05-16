import copy


def solution(n, lost, reserve):
    cnt = 0

    lost_copy = copy.deepcopy(lost)  # 새 값을 복사

    while lost_copy:
        pop = lost_copy.pop(0)
        if pop in reserve:
            lost.remove(pop)
            reserve.remove(pop)

    if len(lost) != 0:
        if reserve != 0:

            for i in lost:
                if i - 1 in reserve:
                    reserve.remove(i - 1)
                    cnt += 1
                elif i + 1 in reserve:
                    reserve.remove(i + 1)
                    cnt += 1

            for i in range(cnt):
                lost.pop(0)
        else:
            pass

    answer = n - len(lost)

    return answer
