from pathlib import Path


def print_grid(grid: dict[tuple[int, int], str]) -> None:
    max_x = 0
    max_y = 0
    for x, y in grid:
        max_x = max(max_x, x)
        max_y = max(max_y, y)

    rows = [[" " for _ in range(max_x + 1)] for __ in range(max_y + 1)]

    for (x, y), char in grid.items():
        rows[y][x] = char

    pretty = "\n".join("".join(row) for row in rows)
    print(pretty)


def solve(input_text: str) -> int:
    grid = {
        (x, y): char
        for y, row in enumerate(input_text.split("\n"))
        for x, char in enumerate(row)
    }

    adjacent_offsets = [
        (dx, dy) for dx in range(-1, 2) for dy in range(-1, 2) if dx != 0 or dy != 0
    ]

    accessible_roll_count = 0

    for (x, y), char in grid.items():
        if char != "@":
            continue

        adjacent_roll_count = 0
        for dx, dy in adjacent_offsets:
            adjacent_xy = (x + dx, y + dy)

            if adjacent_xy not in grid:
                continue

            if grid[adjacent_xy] == "@":
                adjacent_roll_count += 1
        if adjacent_roll_count < 4:
            accessible_roll_count += 1

    return accessible_roll_count


if __name__ == "__main__":
    input_text = Path("2025/04/input.txt").read_text()
    answer = solve(input_text)
    print(answer)
