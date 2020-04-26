house_rob_value = [1,2,3,1]


def rob(nums):
    if not nums:
        return 0

    if len(nums) == 1:
        return nums[1]

    dp = [0] * (len(nums))
    dp[0] = nums[0]
    dp[1] = max(dp[0], nums[1])  # this chooses between first or second

    for i in range(2, len(nums)):
        dp[i] = max(dp[i-2] + nums[i], dp[i-1])  # first is for alternate, second to move pointer forward

    return dp[-1]


print(rob(house_rob_value))
