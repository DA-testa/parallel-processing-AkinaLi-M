# python3

def parallel_processing(n, m, data):
    output = []
    processing = [0] * n # seko līdzi, kuri pavedieni apstrādā darbu

    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs

    for i in range(m):
        min_thread_time = float('inf')
        min_thread_index = None
        for j in range(n):
            if processing[j] + data[i] < min_thread_time:
                min_thread_time = processing[j] + data[i]
                min_thread_index = j
        output.append((min_thread_index, processing[min_thread_index]))
        processing[min_thread_index] += data[i]

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
