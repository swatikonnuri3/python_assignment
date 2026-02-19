def merge_the_tools(string, k):
    result = []

    for i in range(0, len(string), k):
        substring = string[i:i + k]
        seen = set()
        res = []

        for ch in substring:
            if ch not in seen:
                seen.add(ch)
                res.append(ch)

        result.append(''.join(res))

    return result
