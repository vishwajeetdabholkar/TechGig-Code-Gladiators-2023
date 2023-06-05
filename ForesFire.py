def solve_problem(n, x, arr):
    arr.sort()
    prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]

    left, right = 1, max(arr)
    ans = -1

    while left <= right:
        mid = left + ((right - left) // 2)
        idx = bisect.bisect_left(arr, mid)
        count = n - idx

        if count == x:
            ans = mid
            left = mid + 1
        elif count < x:
            right = mid - 1
        else:
            if (prefix_sum[-1] - prefix_sum[idx]) - mid * count <= (x - count) * mid:
                ans = mid
            left = mid + 1

    return ans


import bisect
n, x = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))
print(solve_problem(n, x, arr))