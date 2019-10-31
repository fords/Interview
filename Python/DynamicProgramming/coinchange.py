'''
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.
'''

# Approach  write the test cases on the table, build it and use dynamic programming.

def coinChange(coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """
     #     0 1 2 3 4 5 6
     # 0
     # 1   0 1 2 3 4 5 6
     # 2   0 1 1 2 2 3 3
     # 5   0 1 1 2 2 1 1

    dp = [[0 for _ in range(amount+1)]  for _ in range(len(coins)+1)]
    for i in range(len(coins)+1):
        dp[i][0] = 0
    for j in range(1,(amount+1)):
        dp[0][j] = amount + 1
    # print dp
    for i in range(1,len(coins)+1):
        for j in range(1, amount + 1):
            if j - coins[i-1] >= 0:
                dp[i][j] = min(dp[i][j-coins[i-1]]+ 1,dp[i-1][j] )
            else:
                dp[i][j] = dp[i-1][j]
    return dp[-1][-1] if dp[-1][-1] != amount + 1 else -1
