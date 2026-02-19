def second_max(n):
    try:
        arr = list(map(int, input("Enter Elements: ").split()))
        if len(arr) != n:
            raise ValueError(f"Expected {n} elements, but got {len(arr)}")

        sec_max = sorted(set(arr))
        if len(sec_max) < 2:
            raise ValueError("Not enough unique elements to find second maximum")

        return sec_max[-2]

    except ValueError as ve:
        print("ValueError:", ve)
        return None
    except Exception as e:
        print("Unexpected error:", e)
        return None