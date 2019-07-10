from functools import lru_cache
from typing import Generator


def fib1(n: int) -> int:
    if n < 2:
        return n
    return fib1(n-1) + fib1(n-2)


memo = {0: 0, 1: 1}


def fib2(n: int) -> int:
    if n not in memo:
        memo[n] = fib2(n-1) + fib2(n-2)
    return memo[n]


@lru_cache(maxsize=None)
def fib3(n:int) -> int:
    if n<2:
        return n
    return fib3(n-1) + fib3(n-2)


def fib4(n: int) -> Generator[int, None, None]:
    yield 0
    if n > 0: yield 1
    last = 0
    next = 1
    for _ in range(1, n):
        last, next = next, last + next
        yield next



if __name__ == '__main__':
    # print(fib3(50))
    # print(fib3(5))
     for i in fib4(51):
         print(i)
