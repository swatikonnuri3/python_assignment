def print_formatted(number):
    lines = []
    for i in range(1, number + 1):
        lines.append(
            f"{i} {oct(i)[2:]} {hex(i)[2:].upper()} {bin(i)[2:]}"
        )
    return "\n".join(lines)
