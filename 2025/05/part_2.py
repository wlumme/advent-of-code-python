from pathlib import Path


def solve(input_text: str) -> int:
    ranges_input_text, _ = input_text.split("\n\n")

    ranges = []

    for line in ranges_input_text.split("\n"):
        lower, upper = line.split("-")
        ranges.append((int(lower), int(upper)))

    ranges.sort()
    prev_lower, prev_upper = ranges[0]
    total = 0

    for lower, upper in ranges[1:]:
        if lower <= prev_upper:
            prev_upper = max(upper, prev_upper)
        else:
            total += prev_upper - prev_lower + 1
            prev_lower = lower
            prev_upper = upper

    total += prev_upper - prev_lower + 1
    return total


if __name__ == "__main__":
    input_text = Path("2025/05/input.txt").read_text()
    total = solve(input_text)
    print(total)
