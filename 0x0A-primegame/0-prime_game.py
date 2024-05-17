#!/usr/bin/python3
"""
Game of prime numbers. Contains one function -isWinner
"""


def isWinner(x, nums):
    """
    Returns the winner of the game, where two players take turns
    finding a prime number.
    """
    ben = 0
    maria = 0
    if x < 1:
        return None

    for n in nums:
        if nums.index(n) == x:
            break
        prime = [True for i in range(n+1)]
        p = 2
        while (p*p <= n):
            if prime[p]:
                for i in range(p*p, n+1, p):
                    prime[i] = False
            p += 1
        primes = []
        for p in range(2, n+1):
            if prime[p]:
                primes.append(p)
        if len(primes) % 2 == 0:
            ben += 1
        else:
            maria += 1

    if ben > maria:
        return "Ben"
    elif maria > ben:
        return "Maria"
    else:
        return None
