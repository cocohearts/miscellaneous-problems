def solve_problem(list_str):
    list_stalls = []
    for r in range(len(list_str)):
        if list_str[r] == "1":
            list_stalls.append(r)
    number_stalls = len(list_str)

    #list_stalls is sorted
    if len(list_stalls) == 0:
        answer = number_stalls - 1

    else:
        current_D = float("inf")
        if len(list_stalls) > 1:
            current_D = list_stalls[1] - list_stalls[0]

        max_D = 0
        second_max_D = 0

        for r in range(len(list_stalls)-1):
            tracker_D = list_stalls[r + 1] - list_stalls[r]
            if tracker_D > max_D:
                second_max_D = max_D
                max_D = tracker_D
            elif tracker_D > second_max_D:
                second_max_D = tracker_D

            if current_D > tracker_D:
                current_D = tracker_D
        #now that we have this info:
        #casework!
        max_edge = max(list_stalls[0],number_stalls - list_stalls[-1] - 1)

        case_1 = max_D // 3
        case_2 = second_max_D // 2
        case_3 = min(max_D // 2,max_edge)
        case_4 = max_edge // 2
        case_5 = min(list_stalls[0],number_stalls - list_stalls[-1] - 1)
        answer = min(current_D,max(case_1,case_2,case_3,case_4,case_5))
    return answer

fin = open('socdist1.in','r')
N = int(fin.readline())
list_str = fin.readline()
answer = solve_problem(list_str)

with open('socdist1.out','w') as fout:
    fout.write(str(answer))