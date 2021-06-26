


if __name__ == '__main__':

    # 2try

    from collections import deque


    def solution(priorities, location):

        answer = 0
        deq = deque(priorities)

        while deq:
            doc = deq.popleft()

            max_val = max(deq)
            if not deq:
                answer += 1
                return answer

            if max_val > doc:
                deq.append(doc)
                if idx == location:
                    location = len(deq)
                location -= 1
            else:
                answer += 1
                if location == idx:
                    return answer

                location -= 1

            idx += 1

        return answer

    # 3try
    from collections import deque


    def solution(priorities, location):

        answer = 0
        deq = deque(priorities)
        idx = 0

        # 빼내고 하면서 인덱스가 유지가 안 된다

        while deq:

            doc = deq.popleft()

            if not deq:
                answer += 1
                return answer

            max_val = max(deq)
            # 최댓값이 아닐 경우

            if max_val > doc:
                # 이 순서가 잘못 됐다 더하고 길이재면 인덱스 상으로 다름 . 기초 문제
                # location update

                #  원하는 아이템 찾았을 때 길이로 location update , idx 초기화
                if idx == location:
                    location = len(deq)
                    idx = 0

                elif idx != location
                    iocation -= 1

                deq.append(doc)
                # 꼬이면 다시 생각하기 어려우니 머리속으로 다시 생각

            # 최댓값이면 빼내고 카운트 + 1

            else:
                answer += 1

                if idx != 0:
                    idx -= 1
                if location == idx:
                    return answer

        return answer


    # 전체 코드도 단계별로 작성하는 습관 , 생각을 해나가기 맞든 틀리든 생각하는 수준을 높이면 된다
    # step 으로 생각하기
    from collections import deque


    # step1.
    # case는 append 하거나 출력하거나 둘 중 하나.
    # step2.
    # 내가 원하는 문서였는데 append 하는 경우와 출력하는 경우로 나뉜다
    # step3.
    # append하는 경우
    # 원하는 문서인 경우
    # idx를 초기화하고 location을 해당 시점의 deq 길이로 바꾼다
    # 원하는 문서가 아닌 경우
    # 길이가 줄어들었으므로 location -= 1 을 해주고 idx는 그대로 진행한다
    # step4 출력하는 경우
    # 원하는 문서인 경우
    #
    # 원하는 문서가 아닌 경우
    # idx 를 하나 줄여준다 전체적으로는 그대로 가도록
    # 애초에 idx와 location을 굳이 만나게 할 필요가 있나? -> idx가 무슨 의미가 있지? 어차피 더하고 빼지면서 location의 차례가 오기만 하면 된다

    # 4try
    def solution(priorities, location):
        deq = deque(priorities)
        max_val = max(deq)
        answer = 0
        idx = 0
        while deq:
            doc = deq.popleft()
            if max_val > doc:
                # 뒤로 가는 경우이므로 초기화
                if idx == location:
                    location = len(deq)
                    idx = 0
                else:
                    location -= 1
                deq.append(doc)
                # 뒤에 append 되므로 locaton은 줄여진다

            else:  # 출력하는 경우
                answer += 1
                if idx == location:
                    return answer
                idx = 0


    # 5try
    # 애초에 idx와 location을 굳이 만나게 할 필요가 있나? -> idx가 무슨 의미가 있지? 어차피 더하고 빼지면서 location의 차례가 오기만 하면 된다 yagni 한 코드

    from collections import deque


    def solution(priorities, location):
        deq = deque(priorities)
        answer = 0

        while deq:
            doc = deq.popleft()
            # append 하는 경우
            if not deq:
                answer += 1
                return answer
            max_val = max(deq)

            if location == 0:
                if max_val > doc:
                    # 뒤로 가는 경우이므로 초기화
                    location = len(deq)
                    deq.append(doc)
                    # 뒤에 append 되므로 locaton은 줄여진다
                else:  # 출력하는 경우
                    answer += 1
                    return answer
            else:  # 대상이 아니라면 append 하거나 출력하므로 location이 0이 아니므로 0씩 줄여준다

                if max_val > doc:
                    location -= 1
                    deq.append(doc)
                else:
                    location -= 1
                    answer += 1

# https://liveyourit.tistory.com/182 다른 사람의 풀이 참고함