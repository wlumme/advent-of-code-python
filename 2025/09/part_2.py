from pathlib import Path

XY = tuple[int, int]


def solve(input_text: str) -> int:
    print("Solving...")
    red_xys = get_red_xys(input_text=input_text)
    green_xys = get_green_xys(red_xys=red_xys)
    oob_xys = get_oob_xys(red_xys=red_xys, green_xys=green_xys)
    return get_max_area(red_xys=red_xys, oob_xys=oob_xys)


def get_red_xys(input_text: str) -> list[XY]:
    print("Getting red XYs...")
    red_xys = []

    for line in input_text.split("\n"):
        x, y = (int(n) for n in line.split(","))
        red_xys.append((x, y))

    return red_xys


def get_green_xys(red_xys: list[XY]) -> set[XY]:
    print("Getting green XYs...")

    x1, y1 = red_xys[-1]
    green_xys = set()

    for x2, y2 in red_xys:
        new_green_xys = get_green_line(x1=x1, y1=y1, x2=x2, y2=y2)
        green_xys.update(new_green_xys)
        x1, y1 = x2, y2

    return green_xys


def get_green_line(x1: int, y1: int, x2: int, y2: int) -> list[XY]:
    if x1 == x2:
        y_min = min(y1, y2)
        y_max = max(y1, y2)
        return [(x1, y) for y in range(y_min + 1, y_max)]
    x_min = min(x1, x2)
    x_max = max(x1, x2)
    return [(x, y1) for x in range(x_min + 1, x_max)]


def get_oob_xys(red_xys: list[XY], green_xys: set[XY]) -> set[XY]:
    print("Getting OOB XYs...")

    x_min = min(x for x, _ in red_xys) - 1
    x_max = max(x for x, _ in red_xys) + 1
    y_min = min(y for _, y in red_xys) - 1
    y_max = max(y for _, y in red_xys) + 1

    flooded_xys = {(x_min, y_min)}
    xys_to_search = [(x_min, y_min)]
    searched_xys = set()

    while xys_to_search:
        print(f"{len(xys_to_search):>10,}")
        x, y = xys_to_search.pop()

        for xa, ya in (x - 1, y - 1), (x - 1, y + 1), (x + 1, y - 1), (x + 1, y + 1):
            if (
                x_min <= x <= x_max
                and y_min <= y <= y_max
                and (xa, ya) not in searched_xys
                and (xa, ya) not in green_xys
                and (xa, ya) not in red_xys
            ):
                flooded_xys.add((xa, ya))
                xys_to_search.append((xa, ya))

            searched_xys.add((xa, ya))

    return flooded_xys


def get_max_area(red_xys: list[XY], oob_xys: set[XY]) -> int:
    print("Getting max area...")

    max_area = 1
    xys = []

    for x1, y1 in red_xys:
        for x2, y2 in xys:
            if is_rectangle_in_bounds(x1=x1, y1=y1, x2=x2, y2=y2, oob_xys=oob_xys):
                area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
                # print(x1, y1, x2, y2, area)
                max_area = max(max_area, area)

        xys.append((x1, y1))

    return max_area


def is_rectangle_in_bounds(
    x1: int, y1: int, x2: int, y2: int, oob_xys: set[XY]
) -> bool:
    x_min = min(x1, x2)
    x_max = max(x1, x2) + 1
    y_min = min(y1, y2)
    y_max = max(y1, y2) + 1

    for x in range(x_min, x_max):
        for y in range(y_min, y_max):
            if (x, y) in oob_xys:
                print(x1, y1, x2, y2, x, y)
                return False

    return True


if __name__ == "__main__":
    input_text = Path("2025/09/input.txt").read_text()
    answer = solve(input_text)
    print(answer)
