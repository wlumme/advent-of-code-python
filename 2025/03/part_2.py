from pathlib import Path


def get_max_joltage(bank: str, num_digits: int) -> int:
    indexed_bank = list(enumerate(bank))
    output = 0
    digit_index = 0
    for remaining_digits in range(num_digits, 0, -1):
        max_joltage = int(bank[digit_index])
        max_joltage_index = digit_index
        end_index = len(bank) - remaining_digits + 1

        for i, battery in indexed_bank[digit_index + 1 : end_index]:
            joltage = int(battery)
            if joltage > max_joltage:
                max_joltage = joltage
                max_joltage_index = i

        output = 10 * output + max_joltage
        digit_index = max_joltage_index + 1
    return output


if __name__ == "__main__":
    num_digits = 12

    input_text = Path("2025/03/input.txt").read_text()
    banks = input_text.split("\n")

    total_max_joltage = 0
    for bank in banks:
        total_max_joltage += get_max_joltage(bank, num_digits=num_digits)

    print(total_max_joltage)
