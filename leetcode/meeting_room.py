def meeting_room(times):
    times = sorted(times)
    start = times[0][0]
    end = times[-1][1] + 1
    ing = []
    max_cnt = 0
    for i in range(start, end):
        while times and times[0][0] == i:
            ing.append(times.pop(0))
        ing = [t for t in ing if t[1] != i]
        max_cnt = max(max_cnt, len(ing))
    return max_cnt



input = [[5, 10], [15, 20], [0, 30], [8, 11], [2, 7], [3, 9], [10, 12], [13, 14], [16, 17], [18, 19]]
print(meeting_room(input))