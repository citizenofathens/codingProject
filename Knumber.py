if __name__ == '__main__':



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