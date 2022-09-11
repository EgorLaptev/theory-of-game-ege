from functools import lru_cache


def moves(n):
    a, b = n
    return (a + 1, b), (a, b + 1), (a * 2, b), (a, b * 2)


@lru_cache(None)
def f(n):
    if sum(n) >= 77:
        return 'end'
    elif any(f(x) == 'end' for x in moves(n)):
        return 'p1'
    elif all(f(x) == 'p1' for x in moves(n)):
        return 'v1'
    elif any(f(x) == 'v1' for x in moves(n)):
        return 'p2'
    elif all(f(x) == 'p2' or f(x) == 'p1' for x in moves(n)):
        return 'v2'


for i in range(1, 70):
    print(i, f((7, i)))
