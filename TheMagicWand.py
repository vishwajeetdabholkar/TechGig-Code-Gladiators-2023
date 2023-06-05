from bisect import bisect_left

# reading inputs
N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
queries = list(map(int, input().split()))

# creating prefix sum array
prefix_sum = [0]*(N+1)
for i in range(1, N+1):
    prefix_sum[i] = prefix_sum[i-1] + arr[i-1]

# calculating total operation cost for each query
for q in queries:
    idx = bisect_left(arr, q)
    total_cost = (q*idx - prefix_sum[idx]) + (prefix_sum[N] - prefix_sum[idx] - q*(N-idx))
    print(total_cost, end=" ")
