def calculate_happiness(arr, set_a, set_b):
    happiness = 0
    for num in arr:
        if num in set_a:
            happiness += 1
        elif num in set_b:
            happiness -= 1
    return happiness