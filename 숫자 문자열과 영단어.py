# https://programmers.co.kr/learn/courses/30/lessons/81301
def solution(s):
    answer = ''
    
    num_dict = {'zero':'0', 'one':'1', 'two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
    tmp = ''
    for i, ch in enumerate(s):        
        if 48 <= ord(ch) <= 57:
            tmp = ''
            answer += ch
            continue
        tmp += ch
        if tmp in num_dict:
            answer += num_dict[tmp]
            tmp = ''   
        
    
    return int(answer)
