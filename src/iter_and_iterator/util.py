from itertools import combinations

def probability_with_a(n, l, k):
    if len(l) != n:
        raise ValueError(f"Expected {n} elements, but got {len(l)}")
    counta = 0
    for combo in combinations(l, k):
        if "a" in combo:
            counta += 1
    total = 0
    for combo in combinations(l, k):
        total += 1
    return counta / total