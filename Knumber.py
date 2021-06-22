if __name__ == '__main__':


    # 최초 작성 코드  . 최악은 피하자
    import copy


    def solution(array, commands):

        #print문으로 확인 자제ㄷ

        answer = []
        origin_array = copy.deepcopy(array)
        for i in range(len(commands[0])):
            command = commands[i]
            left_idx = commands[i][0]
            right_idx = commands[i][1]
            temp_arr = array[left_idx - 1:right_idx]
            sorted_array = sorted(temp_arr)
            print(command[2])
            print(sorted_array)
            answer.append(sorted_array[command[2] - 1])
            print(answer)
        return answer


    import copy


    # 런타임 오류가 나서 다른 사람 질문 참고
    def solution(array, commands):

        answer = []

        temp_arr = []
        # 이런 식으로 했을 때 런타임 오류 난다 이유는 ?
        # for i in range(3):
        #   left_idx = command[i][0]
        #   right_idx = command[i][1]
        #   temp_arr = array[left_idx-1:right_idx]

        for command in commands:
            # deepcopy 해서 array를 복사하지 않아도 기존의 array는 변하지 않고 temp_arr에 담기므로 copy할 필요가 없다. 어찌보면 다형성

            temp_arr = array[command[0] - 1:command[1]]
            temp_arr.sort()
            answer.append(temp_arr[command[2] - 1])

        return answer