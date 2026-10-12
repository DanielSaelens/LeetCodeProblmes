
def maxSumTwoSubarray(arr, k):
    n = len(arr)
    maxSum = 0

    for i in range(n - k + 1):
        currSum = 0

        for j in range(k):
            currSum += arr[i + j]
            
        if i == 0:
            maxSum = currSum

        else:
            maxSum = max(maxSum, currSum)
            
    return maxSum


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]
    b = [-1, -2, -3, -4, -5]
    k = 3

    print(maxSumTwoSubarray(a, k))
