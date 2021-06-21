if __name__ == '__main__':

    import copy


    def solution(array, commands):

        answer = []
        origin_array = copy.deepcopy(array)
        for i in range(len(commands[0])):
            command = commands[i]
            left_idx = commands[i][0]
            right_idx = commands[i][1]
            temp_arr = array[left_idx:right_idx]
            sorted_array = sorted(temp_arr)
            print(command)
            answer.append(sorted_array[command[1]])
        return answer