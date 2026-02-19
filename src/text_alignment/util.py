def align_text(thickness, c):
    lines = []

    # Top Cone
    for i in range(thickness):
        lines.append((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1))

    # Top Pillars
    for _ in range(thickness + 1):
        lines.append(
            (c * thickness).center(thickness * 2) +
            (c * thickness).center(thickness * 6)
        )

    # Middle Belt (IMPORTANT FIX)
    for _ in range((thickness + 1) // 2):
        lines.append(c * (thickness * 6))

    # Bottom Pillars
    for _ in range(thickness + 1):
        lines.append(
            (c * thickness).center(thickness * 2) +
            (c * thickness).center(thickness * 6)
        )

    # Bottom Cone
    for i in range(thickness):
        lines.append(
            ((c * (thickness - i - 1)).rjust(thickness) + c +
             (c * (thickness - i - 1)).ljust(thickness)).rjust(thickness * 6)
        )

    return lines
