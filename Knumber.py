if __name__ == '__main__':


    # 최초 작성 코드  . 최악은 피하자
    import copy


    def solution(array, commands):

        #print문으로 확인 자제

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
        # 이런 식으로 했을 때 런타임 오류 난다 이유는 ? -> 역시 개념의 문제였고 개념이 탄탄하지 않아서였다
        # 이유는 밑에서 3이라고 지정한 것은 2차원 배열 commands 내부의 command의 길이가 각각 3이라는 것이다.
        # 프로그램 요구사항 입력 값을 제대로 확인하지 않고 그러한 개념이 탄탄하지 않았기 때문에 발생한 문제였다. 역시나
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

    # best practice
    # map(function, list ) lambda x:이후의 식은 x값에 넣을 인자. x: x ** 2  map 함수가 lambda함수를 list에 적용하라는 식이므로
    # 인자는 commands의 첫 번째 요소 부터 들어간다 commands 이차원 리스트이 하나하나의 list가 x가 되어 iterator 하는 것임
    # 그리고 인자로 들어간 x를 람다 익명 함수 내부에서 (:이 내부이다) 처리하여 return 하여 list를 만든다
    #def solution(array, commands):
    #   return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))