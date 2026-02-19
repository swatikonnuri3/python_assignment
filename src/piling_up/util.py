def pile_up(cubes):
    left = 0
    right = len(cubes) - 1
    pile_top = max(cubes)
    while left <= right:
        if cubes[left] >= cubes[right]:
            chosen = cubes[left]
            left += 1
        else:
            chosen = cubes[right]
            right -= 1
        if chosen > pile_top:
            return "No"
        pile_top = chosen
    return "Yes"