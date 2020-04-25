def XOR(bool1,bool2):
    return (bool1 and not bool2) or (bool2 and not bool1)

def find_R(list_health_tuples):
    R = float("inf")
    for r in range(len(list_health_tuples)-1):
        if XOR(list_health_tuples[r][1],list_health_tuples[r+1][1]):
            if R > list_health_tuples[r+1][0]-list_health_tuples[r][0]:
                R = list_health_tuples[r+1][0]-list_health_tuples[r][0]
    return R

def my_sort(list_tuples):
    list_health_tuples = []
    tracker_dict = {}
    tracker_list = []
    for tup in list_tuples:
        tracker_dict[tup[0]] = tup[1]
        tracker_list.append(tup[0])
    tracker_list.sort()
    for loc in tracker_list:
        list_health_tuples.append((loc,tracker_dict[loc]))
    return list_health_tuples

#list_health_tuples
def solve_problem(list_tuples):
    #first we gotta sort by first number
    list_health_tuples = my_sort(list_tuples)
    R = find_R(list_health_tuples)
    start_counter = 0
    for r in range(len(list_health_tuples)-1):
        if list_health_tuples[r][1] == 1:
            if list_health_tuples[r+1][0] - list_health_tuples[r][0] >= R:
                start_counter += 1
    if list_health_tuples[-1][1] == 1:
        start_counter += 1
    print(R)
    print(list_health_tuples)
    return start_counter

list_tuples = []
fin = open('socdist2.in','r')
N = int(fin.readline())
for r in range(N):
    new_cow = fin.readline()
    new_cow = new_cow.split(" ")
    list_tuples.append((int(new_cow[0]),int(new_cow[1])))
answer = solve_problem(list_tuples)
with open("socdist2.out","w") as fout:
    fout.write(str(answer))