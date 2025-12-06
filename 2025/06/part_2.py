from pathlib import Path

operators = {"+": lambda x, y: x + y, "*": lambda x, y: x * y}


def solve(input_text: str) -> int:
    rows = input_text.split("\n")
    cols = zip(*rows, strict=True)

    operator = None
    subtotal = None
    total = 0

    for col in cols:
        if all(char == " " for char in col):
            total += subtotal
            subtotal = None
            operator = None
            continue

        value = int("".join([char for char in col[:-1] if char != " "]))

        last_char = col[-1]
        if last_char != " ":
            operator = operators[last_char]

        subtotal = value if subtotal is None else operator(subtotal, value)

    total += subtotal
    return total


if __name__ == "__main__":
    input_text = Path("2025/06/input.txt").read_text().strip("\n")
    total = solve(input_text)
    print(total)
