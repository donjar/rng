import random

def pattern_check(patterns, amount=100):
    k = 0
    m = 0
    while True:
        if m % 10000 == 1:
            print(k / m)
        r = ''.join(random.choice('01') for _ in range(amount))
        if any(p in r for p in patterns):
            k += 1
        m += 1

    return k / trials
