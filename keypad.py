# 좀 더 효율적인 풀이가 있을 것 같은데 .. 아이디어는 이전에 참고한 적이 있던 터라 코드 구현 능력을 길렀다는 데에 의미를 두자
def get_distance(target_key, hand):
    distance = abs(target_key[0] - hand[0]) + abs(target_key[1] - hand[1])
    return distance


def solution(numbers, hand):
    result = ""
    target_key = []
    keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]

    left_hand = [3, 0]
    right_hand = [3, 2]
    for key in numbers:
        print(key, left_hand, right_hand)
        for y in range(len(keypad)):
            for x in range(len(keypad[0])):
                if keypad[y][x] == key:
                    target_key = [y, x]
                    break
        if key in (1, 4, 7, '*'):
            result += 'L'
            for left in range(len(keypad)):
                if keypad[left][0] == key:
                    left_hand = [left, 0]


        elif key in (3, 6, 9, '#'):
            result += 'R'

            for right in range(len(keypad)):
                if keypad[right][2] == key:
                    right_hand = [right, 2]

        else:

            left_distance = get_distance(target_key, left_hand)

            right_distance = get_distance(target_key, right_hand)

            if left_distance < right_distance:
                result += 'L'
                left_hand = target_key

            elif left_distance == right_distance:
                if hand == 'left':
                    result += 'L'
                    left_hand = target_key
                else:
                    result += 'R'
                    right_hand = target_key
            else:
                result += 'R'

                right_hand = target_key

    return result