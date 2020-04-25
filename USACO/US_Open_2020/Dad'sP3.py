class InfectionSimulator:
    def __init__(self, size, n, k, video_record):
        self.size = size
        self.n = n
        self.k = k
        self.video_record = video_record
    
    def run_simulation(self):
        cow_infected = [0] * self.size
        cow_counter = [0] * self.size
        cow_infected[self.n] = 1
        for record in self.video_record:
            x = record[1] - 1
            y = record[2] - 1 
                if cow_infected[x] == 1:
                cow_counter[x] += 1
            if cow_infected[y] == 1:
                cow_counter[y] += 1
            if cow_infected[x] == 1 and cow_infected[y] == 0:
                if cow_counter[x] <= self.k:
                    cow_infected[y] = 1            
            if cow_infected[y] == 1 and cow_infected[x] == 0 :
                if cow_counter[y] <= self.k:
                    cow_infected[x] = 1
#        print('n=', self.n, 'k=', self.k, cow_infected)
        return cow_infected

def main():
    fin = open('tracing.in','r')
    first_line = fin.readline().split(" ")
    N = int(first_line[0])
    T = int(first_line[1])
    infected = str(fin.readline())[:-1]
    time_list = []
    for r in range(T):
        new_line = fin.readline().split(" ")
        time_list.append((int(new_line[0]),int(new_line[1]),int(new_line[2])))
    list.sort(time_list, key=lambda record: record[0])
    for i in range(N):
        for k in range(N):
            simulator = InfectionSimulator(N, i, k, time_list)
            simulator_result = simulator.run_simulation()
            if simulator_result == result:
                print('Found one possiblity:', 'pacient zero is ', i+1, 'k >= ', k)
                break

    with open('tracing.out','w') as fout:
        print(solve_problem(N,time_list,infected))
        fout.write(solve_problem(N,time_list,infected))


if __name__== "__main__":
    main()