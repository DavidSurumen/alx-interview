#!/usr/bin/python3
"""
Defines makeChange function
"""


def makeChange(coins, target):
    """
    Determines the fewest number of coins needed to meet target amount
    """
    dp = [float('inf')] * (target + 1)
    dp[0] = 0
    for coin in coins:
        for i in range(coin, target + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[target] if dp[target] != float('inf') else -1
