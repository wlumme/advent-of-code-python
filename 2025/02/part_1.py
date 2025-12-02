from pathlib import Path

input_text = Path("2025/02/input.txt").read_text()

id_ranges = []
for id_range in input_text.split(","):
    lower, upper = id_range.split("-")
    id_ranges.append((int(lower), int(upper)))


def is_invalid(n: int) -> bool:
    s = str(n)
    meet_me_halfway = len(s) // 2  # Right at the borderline...
    return s[:meet_me_halfway] == s[meet_me_halfway:]


total = 0
for lower, upper in id_ranges:
    for n in range(lower, upper + 1):
        if is_invalid(n):
            total += n

print(total)
