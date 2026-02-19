def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        substring = string[i:i+k]
        seen = set()
        res = []
        for j in substring:
            if j not in seen:
                seen.add(j)
                res.append(j)
        print(''.join(res))