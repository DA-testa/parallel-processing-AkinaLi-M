# python3
import heapq

def parallel_processing(n, m, data):
    output = []
    processing = [(0, i) for i in range(n)] # seko līdzi, kuri pavedieni apstrādā darbu

    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs

    for i in range(m):
        thread_time, threat_index = heapq.heappop(processing)
        output.append((thread_index, thread_time))
        heapq.heappush(processing, (thread_time + data[i], thread_index))

    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n, m = map(int, input().split())

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = list(map(int, input().split()))

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    for pair in result:
        print(pair[0], pair[1])



if __name__ == "__main__":
    main()
