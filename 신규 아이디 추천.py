# https://programmers.co.kr/learn/courses/30/lessons/72410
def solution(new_id):
    # step 1
    new_id = new_id.lower()
    # print(new_id)
    # step 2
    tmp = ''
    for ch in new_id:
        if 48<=ord(ch)<=57 or 65<=ord(ch)<=90 or 97<=ord(ch)<=122:
            tmp += ch
        elif ch == '-' or ch =='_' or ch =='.':
            tmp += ch
    new_id = tmp
    # print(tmp)
    # step 3
    while '..' in new_id:
        new_id = new_id.replace('..', '.')
    # step 4
    if len(new_id) > 0:
        if new_id[0] == '.': new_id = new_id[1:]
    if len(new_id) > 0:
        if new_id[-1] == '.': new_id = new_id[:-1]
    # step 5
    if len(new_id) == 0: new_id = 'a'
    # step 6
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.': new_id = new_id[:-1]
    # step 7
    if 0 < len(new_id) <= 2:
        tmp = new_id[-1]
        while len(new_id) != 3:
            new_id += tmp
    
    return new_id
