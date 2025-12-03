from pathlib import Path


def get_max_joltage(bank: str) -> int:
    max_leading_digit = int(bank[0])
    leading_digit_index = 0
    for i, battery in enumerate(bank[:-1]):
        joltage = int(battery)
        if joltage > max_leading_digit:
            max_leading_digit = joltage
            leading_digit_index = i

    max_trailing_digit = int(max(bank[leading_digit_index + 1 :]))

    return 10 * max_leading_digit + max_trailing_digit


if __name__ == "__main__":
    input_text = Path("2025/03/input.txt").read_text()
    banks = input_text.split("\n")
    total_max_joltage = 0
    for bank in banks:
        total_max_joltage += get_max_joltage(bank)

    print(total_max_joltage)
