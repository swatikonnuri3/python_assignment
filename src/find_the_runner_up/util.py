def second_max(arr):
    unique = list(set(arr))
    if len(unique) < 2:
        return None
    unique.sort()
    return unique[-2]
