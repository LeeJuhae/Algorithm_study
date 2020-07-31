def get_logs(lines):
    logs = []
    for line in lines:
        log = []
        responded_time = line.split(' ')[1]
        processed_time = int(float(line.split(' ')[2][:-1]) * 1000)
        h, m, s = responded_time.split(':')
        ms = int((((int(h) * 60 + int(m)) * 60) + float(s)) * 1000)
        log.append(ms - processed_time + 1)
        log.append(ms)
        logs.append(log)
    return logs
    
def solution(lines):
    logs = get_logs(lines)
    logs.sort(key=lambda x:x[0])
    max_cnt = 0
    times = []
    for log in logs:
        remove_list = []
        times.append(log)
        if len(times) != 0:
            for idx, time in enumerate(times):
                if log[0] - time[1] >= 1000:
                    remove_list.append(idx)
            for idx in remove_list[::-1]:
                del times[idx]
        max_cnt = max(max_cnt, len(times))
    return max_cnt
