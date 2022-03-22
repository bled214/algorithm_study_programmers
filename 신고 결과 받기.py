# https://programmers.co.kr/learn/courses/30/lessons/92334
from collections import Counter, defaultdict
def solution(id_list, report, k):
    answer = []
    report_set = set()
    from_report_to_reported = defaultdict(set)
    
    for r in report:
        report_id, reported_id = r.split()
        report_set.add((report_id, reported_id))
        from_report_to_reported[report_id].add(reported_id)
    reported_cnt = Counter([reported_id for report_id, reported_id in report_set])
    suspended_id = set([key for key, value in reported_cnt.items() if value >= k])
    
    for id in id_list:
        t = 0
        for reported_id in from_report_to_reported[id]:
            if reported_id in suspended_id:
                t += 1
        answer.append(t)
    
    return answer
