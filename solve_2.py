# s - кол-во камней в куче
# c - кол-во сделанных ходов
# m - за сколько ходов игра должна завершиться

def f(s, c, m):
    if c == n: return c % 2 == m % 2
    if c > n: return 0
    
    moves = [f(s+1, c+1, n), f(s*2, c+1, n)]

    return any(moves) if (c+1) % 2 == m % 2 else all(moves)

for s in range(100):
    for m in range(5):
        if f(s, 0, m):
            print(s, m)
            break

