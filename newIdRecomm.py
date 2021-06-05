import re


def solution(new_id):
    answer = ''
    # step1
    new_id = new_id.lower()

    # step2
    new_id = re.sub('[^a-z0-9-_.]', '', new_id)

    # step3 마침표가 마침표를 뜻하는게 아니라 이스케이프문자를 활용해야 한다 그냥 . 으로 하면 모든 문자를 반복
    new_id = re.sub(r"(\.)\1+", r"\1", new_id)

    # step4
    if len(new_id) == 1:
        if new_id == '.':
            new_id = ''
    elif len(new_id) != 1:

        if new_id[0] == '.':
            new_id = new_id[1:]

            if len(new_id) == 1 and new_id == '.':
                new_id = ''
        if new_id and new_id[-1] == '.':
            new_id = new_id[:-1]

    # step5
    if new_id == '':
        new_id = 'a'

        # step6
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    # step7
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id += new_id[-1]

    answer = new_id
    return answer