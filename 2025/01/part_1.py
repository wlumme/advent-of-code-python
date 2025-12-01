from pathlib import Path


def parse_line(line: str) -> int:
    direction_key = {"L": -1, "R": 1}
    direction = direction_key[line[0]]
    magnitude = int(line[1:])
    return direction * magnitude


input_text = Path("2025/01/input.txt").read_text()
rotations = [parse_line(line) for line in input_text.split("\n")]

position = 50
zero_count = 0

for rotation in rotations:
    position = (position + rotation) % 100
    if position == 0:
        zero_count += 1

print(zero_count)
