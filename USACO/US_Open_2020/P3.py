def bash_check(k,pat_zero,N,time_stamp_list):
    sickness_list = [0]*(pat_zero-1) + [1] + [0]*(N-pat_zero)
    tracker_list = [0]*N
    for interaction in time_stamp_list:
        for cow in interaction:
            if sickness_list[cow-1] == 1:
                tracker_list[cow-1] += 1
        if (sickness_list[interaction[0]-1]) and (tracker_list[interaction[0]-1] <= k):
            sickness_list[interaction[1]-1] = 1
        if (sickness_list[interaction[1]-1]) and (tracker_list[interaction[1]-1] <= k):
            sickness_list[interaction[0]-1] = 1
    final_infections = ""
    for cow in sickness_list:
        final_infections += str(cow)
    return final_infections

def my_sort(time_list):
    tracker_dict = {}
    tracker_list = []
    time_stamp_list = []
    for interaction in time_list:
        tracker_dict[interaction[0]] = interaction[1:]
    for time in time_list:
        tracker_list.append(time)
    tracker_list.sort()
    for time in tracker_dict:
        time_stamp_list.append(tracker_dict[time])
    return time_stamp_list

def solve_problem(N,time_list,infected):
    time_stamp_list = my_sort(time_list)
    max_K = 0
    pat_zeroes = 0
    least_K = float("inf")
    for pat_zero in range(N):
        passed = False
        for k in range(N+1):
            if bash_check(k,pat_zero,N,time_stamp_list) == infected:
                passed = True
                if k>max_K:
                    max_K = k
                if k < least_K:
                    least_K = k
                if k == N:
                    max_K = float("inf")
        if passed:
            pat_zeroes += 1
    final_string = str(pat_zeroes) + " " + str(least_K) + " "
    if max_K == float("inf"):
        final_string += "Infinity"
    else:
        final_string += str(max_K)
    return final_string


fin = open('tracing.in','r')
first_line = fin.readline().split(" ")
N = int(first_line[0])
T = int(first_line[1])
infected = str(fin.readline())[:-1]
time_list = []
for r in range(T):
    new_line = fin.readline().split(" ")
    time_list.append((int(new_line[0]),int(new_line[1]),int(new_line[2])))
    print(time_list)
with open('tracing.out','w') as fout:
    fout.write(solve_problem(N,time_list,infected))