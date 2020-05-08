from functools import lru_cache

# -> Bad Fibonacci <-
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55

# Notum lowercase í nafnið á func í Python
# def fib(n):
#     if n == 1:
#         return 0
#     elif n == 1:
#         return 1
#     elif n == 2:
#         return 1
#     elif n > 2:
#         # Þetta er endurkvæmt fall því það kallar í sjálft sig.
#         # Skoðum betur seinna hvað er raunverulega að gerast í minni tölvunnar.
#         return fib(n - 1) + fib(n - 2)
#
# # range (inclusive, exclusive)
# for n in range(1, 51):
#     print(n, ":", fib(n))
# # Rennum yfir hvernig þetta er að kalla aftur og aftur í það sama...

# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# -> Basic memoization <-
# Munum hverju við höfum komist að.

# Þetta er dictionary til að geyma síðustu köll í fallið fib
fib_cache = {}

# def fib_with_memoization(n):
#     if n in fib_cache:
#         return fib_cache[n]
#     if n == 1:
#         return 0
#     elif n == 1:
#         return 1
#     elif n == 2:
#         return 1
#     elif n > 2:
#         ret = fib_with_memoization(n - 1) + fib_with_memoization(n - 2)
#
#         fib_cache[n] = ret
#         return ret
#
# for n in range(1, 10001):
#     print(n, ":", fib_with_memoization(n))

# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# Memoization using Least Recently Used Cache
#
#
# @lru_cache(maxsize=1000)
# def fib_with_lru_cache(n):
#     if type(n) != int:
#         raise TypeError("n á að vera tala asninn þinn!")
#     if n < 0:
#         raise ValueError("n á að vera jákvæð tala asninn þinn1!")
#     if n == 1:
#         return 0
#     elif n == 1:
#         return 1
#     elif n == 2:
#         return 1
#     elif n > 2:
#         # Þetta er endurkvæmt fall því það kallar í sjálft sig.
#         # Skoðum betur seinna hvað er raunverulega að gerast í minni tölvunnar.
#         return fib_with_lru_cache(n - 1) + fib_with_lru_cache(n - 2)
#
# # range (inclusive, exclusive)
# for n in range(2, 1001):
#     fib_with_lru_cache(n)
#     print(n, ":", fib_with_lru_cache(n))
#     # print(round(fib_with_lru_cache(n + 1) / fib_with_lru_cache(n), 6))
#
# # x = 1499 #  [Previous line repeated 496 more times]
# # x = 1.41
# # x = -1
# # x = "tveir"
#
# # print(x, ":", fib_with_lru_cache(x))

# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# Hexagonal numbers

# def hex_numbers(n):
#     return 2*n**2 - n
# for n in range(1, 11):
#     print(hex_numbers(n))

# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# Catalan numbers
#
# @lru_cache(maxsize=1000)
# def catalan(n):
#     if n <= 1:
#         return 1
#
#     ret = 0
#     for i in range(n):
#         ret += catalan(i) * catalan(n - i - 1)
#
#     return ret
#
#
# for i in range(1001):
#     print(i, ":", catalan(i))

# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# Max slices with n cuts
# n = 5
# p = (n**2+n+2)/2
#
# print(int(p))
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# Look and say
def look_and_say(n):
    if n == 1:
        return "1"
    if n == 2:
        return "11"

    s = "11"
    for i in range(3, n + 1):
        s += '$'
        l = len(s)
        cnt = 1
        tmp = ""

        for j in range(1, l):
            if s[j] != s[j - 1]:
                tmp += str(cnt + 0)
                tmp += s[j - 1]
                cnt = 1
            else:
                cnt += 1

        s = tmp
    return s


N = 4
print(look_and_say(N))