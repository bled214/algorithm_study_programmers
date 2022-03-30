# https://programmers.co.kr/learn/courses/30/lessons/67256
from collections import defaultdict, deque

def bfs(start, target):

    q = deque()
    r, c = start
    q.append((r, c, 0))
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while q:
        r, c, d = q.popleft()
        if (r, c) == target:
            return d
        for i in range(4):
            nr = r + dx[i]
            nc = c + dy[i]
            if 0<=nr<4 and 0<=nc<3:
                q.append((nr, nc, d+1))
    return 0

def solution(numbers, hand):
    answer = ''
    
    pos_dict = defaultdict(tuple)
    cnt = 0
    for i in range(3):
        for j in range(3):
            cnt += 1
            pos_dict[str(cnt)] = (i, j)
    pos_dict['*'] = (3, 0)
    pos_dict['0'] = (3, 1)
    pos_dict['#'] = (3, 2)   
    
    left_keys = ('1', '4', '7', '*')
    right_keys = ('3', '6', '9', '#')
    
    cur_left = '*'
    cur_right = '#'
    for n in numbers:
        if str(n) in left_keys:
            cur_left = str(n)
            answer += 'L'
        elif str(n) in right_keys:
            cur_right = str(n)
            answer += 'R'
        else:
            l_distance = bfs(pos_dict[cur_left], pos_dict[str(n)])
            r_distance = bfs(pos_dict[cur_right], pos_dict[str(n)])
            if l_distance > r_distance:
                cur_right = str(n)
                answer += 'R'
            elif l_distance < r_distance:
                cur_left = str(n)
                answer += 'L'
            else:
                if hand == 'right':
                    cur_right = str(n)
                    answer += 'R'
                else:
                    cur_left = str(n)
                    answer += 'L'
    
    return answer
