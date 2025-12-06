from functools import reduce
from pathlib import Path

input_text = Path("2025/06/input.txt").read_text().strip()

rows = [line.split() for line in input_text.split("\n")]
cols = zip(*rows, strict=True)

operators = {"+": lambda x, y: x + y, "*": lambda x, y: x * y}

total = 0
for col in cols:
    values = [int(n) for n in col[:-1]]
    operator = operators[col[-1]]
    subtotal = reduce(operator, values)
    total += subtotal

print(total)
