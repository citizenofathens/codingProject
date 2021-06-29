if __name__ == '__main__':

    # 소수 찾기 방법 step  https://myjamong.tistory.com/139
    import math
    from itertools import permutations


    def is_prime(number):
        if number == 1 or number == 0:
            return False
        else:
            for i in range(2, int(math.sqrt(int(number)) + 1)):
                if number % i == 0:
                    return False

        return True


    def solution(numbers):
        # 1try

        #     # 2 3 5 7
        #     # 1, 4, 6, 8
        #     # 짝수인 걸 치운다
        #     # 에라토스 테네스의 체 ?
        #     #
        #     i = 0

        #     # 길이가 1인 소수

        #     #for i in numbers:
        #     #    if i == 2 or i == 3 or i == 5 or i ==7:
        #     #        prime_number += 1

        #     per_list = permutations(numbers)
        #     answer = 0

        #     for number in per_list:
        #         if len(number) == 1 and if number[-1] in ('2357') :
        #             answer +=1
        #         else len(number) !=1 and number[-1] in ('12357'):
        #             answer +=1

        #     return answer

        # 2try and 풀이 참조

        answer = []

        for i in range(1, len(numbers) + 1):
            arr = list(permutations(numbers, i))
            for j in range(len(arr)):
                number = int(''.join(arr[j]))
                if is_prime(number):
                    answer.append(number)
        answer = list(set(answer))
        return len(answer)