def annotate(garden):

    if not garden:
        return []
    
    result = []

    rows = len(garden)
    cols = len(garden[0])

    for row in garden:
        if len(row) != cols:
            raise ValueError("The board is invalid with current input.")
        for char in row:
            if char not in (" ", "*"):
                raise ValueError("The board is invalid with current input.")

    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),          (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]

    for r in range(rows):
        new_row = ""

        for c in range(cols):
            if garden[r][c] == "*":
                new_row += "*"
            else:
                count = 0

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if 0 <= nr < rows and 0 <= nc < cols:
                        if garden[nr][nc] == "*":
                            count += 1

                if count == 0:
                    new_row += " "
                else:
                    new_row += str(count)

        result.append(new_row)

    return result

