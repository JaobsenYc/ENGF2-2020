import random

def estimate_pi(n):
    r = 1.0
    a, b = (0.0, 0.0)
    m = 0
    for i in range(0, n+1):
        x1 = random.uniform(a-r, a+r)
        y1 = random.uniform(b-r, b+r)
        if x1**2 + y1**2 <= 1.0:
            m =m+1
    return (m / float(n)) * 4

def estimate_pi(n):
    r = 1.0
    a, b = (0.0, 0.0)
    m = 0
    for i in range(0, n+1):
        x1 = random.uniform(a-r, a+r)
        y1 = random.uniform(b-r, b+r)
        if x1**2 + y1**2 <= 1.0:
            m =m+1
    return (m / float(n)) * 4

print(estimate_pi(1000000))