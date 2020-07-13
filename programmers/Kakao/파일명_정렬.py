def solution(files):
    answer = []
    file_info = {}
    for file in files:
        file_info[file] = []
        num_start, num_end = -1, -1
        for i in range(len(file)):
            if file[i].isdigit() and num_start == -1:
                num_start = i
            elif file[i].isdigit() == 0 and num_start != -1 and num_end == -1:
                num_end = i
                break
        if num_end == -1:
            num_end = len(file)
        file_info[file].append(file[:num_start].upper())
        file_info[file].append(int(file[num_start:num_end]))
    file_info = sorted(file_info.items(), key=lambda x: (x[1][0],x[1][1]))
    for info in file_info:
        answer.append(info[0])
    return answer
