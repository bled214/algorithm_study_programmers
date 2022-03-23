# https://programmers.co.kr/learn/courses/30/lessons/77484
def solution(lottos, win_nums):
    
    win_nums = set(win_nums)
    rank = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    
    unrecognizable_cnt = 0 
    recognizable_num_set = set()
    
    for l in lottos:
        if l == 0:
            unrecognizable_cnt += 1
        else:
            recognizable_num_set.add(l)
    lowest_score = len([i for i in recognizable_num_set if i in win_nums])
    highest_score = lowest_score + unrecognizable_cnt
    
    return [rank[highest_score], rank[lowest_score]]
