def lengthOfLIS(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    '''
    The idea is to use dp to record the lenth of increasing sequence up till position i
    [1,2,4,3]
    dp init = [1,1,1,1]
    after each scan:
    i = 0 [1,1,1,1]
    i = 1 [1,2,1,1]
    i = 2 [1,2,3,1]
    i = 3 [1,2,3,3]
    max(dp) is equal to get the max in the list (3 in this case)
    '''

    if len(nums) < 2:
        return len(nums)

    dp = [1] * len(nums)

    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = dp[j] + 1 if dp[j] + 1 > dp[i] else dp[i]

    return max(dp)