from pathlib import Path


def run(input_text: str) -> int:
    id_ranges = parse_input(input_text)
    total = 0
    for lower, upper in id_ranges:
        total += sum_invalids(lower, upper)
    return total


def parse_input(input_text: str) -> list[tuple[int, int]]:
    id_ranges = []
    for id_range in input_text.split(","):
        lower, upper = id_range.split("-")
        id_ranges.append((int(lower), int(upper)))
    return id_ranges


def sum_invalids(lower: int, upper: int) -> int:
    total = 0
    for n in range(lower, upper + 1):
        if is_invalid(n):
            print(f"{n:>10,}")
            total += n
    return total


def is_invalid(n: int) -> bool:
    s = str(n)
    length = len(s)
    return any(is_invalid_for_factor(s, factor) for factor in get_factors(length))


def get_factors(n: int) -> list[int]:
    if n == 1:
        return []
    factors = [1]
    for n_ in range(2, int(n**0.5) + 1):
        if n % n_ == 0:
            factors.append(n_)
            factors.append(n // n_)
    return factors


def is_invalid_for_factor(s: str, factor: int) -> bool:
    first = s[:factor]
    return all(s[i : i + factor] == first for i in range(factor, len(s), factor))


if __name__ == "__main__":
    input_text = Path("2025/02/input.txt").read_text()
    output = run(input_text)
    print(output)
