def solution(s):
    # 소수점 제거 //
    max_unit = len(s) // 2

    # 기준 문자열을 담을 스택
    stack = []

    # 압축된 문자열
    compressed_list = []

    # 스택 활용 메모리 사용률 최소화

    for unit in range(1, max_unit + 1):

        compressed = ""
        # first = True
        temp_s = s

        number = 1

        while temp_s:

            if len(stack) == 0:
                based = temp_s[:unit]

                stack.append(based)

            temp_s = temp_s[unit:]
            print(temp_s)
            compare = temp_s[:unit]

            if stack[0] == compare:

                number += 1

            else:
                if number != 1:
                    result_str = str(number) + stack.pop()
                else:
                    result_str = stack.pop()
                compressed += result_str

                number = 1
            if unit > len(temp_s):
                compressed += temp_s

                temp_s = ""

                compressed_list.append(len(compressed))

                break
    print(compressed_list)
    result = min(compressed_list)

    return result

