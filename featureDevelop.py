


if __name__ == '__main__':

    def solution(progresses, speeds):

        answer = []
        que = []
        while progresses:

            day = 1
            count = 1
            process = progresses.pop(0)
            speed = speeds.pop(0)
            rate = 0

            if not progresses:
                answer.append(count)
                break
            # 처음 작업량이 100인 경우? 를 생각해서 먼저 rate를 계산하니 통과할 수 있었다 . 역시 좋음을 추구하자
            rate = process + (speed * day)
            while rate < 100:
                day += 1
                rate = process + (speed * day)

            while progresses:
                # 나중에 이렇게 순회하면서 시간 구하고 이럴 거면 애초에 처음에 계산하는 게 나을 듯 -> 애초에 이럴 거면 생각은 했어도 전처리를 먼저 다해놓는 코드로 짜기
                # 정상적 케이스 말고 예외케이스를 생각하기 모두 통과하려면 -> 이 문제에서 얻은 아주 큰 교훈

                next_p = progresses[0]
                next_s = speeds[0]

                time = next_p + (next_s * day)

                if time >= 100:
                    progresses.pop(0)
                    speeds.pop(0)
                    count += 1
                else:
                    break

            answer.append(count)

        return answer