from pathlib import Path

input_text = Path("2025/05/input.txt").read_text()

fresh_ingredient_id_ranges_input_text, available_ingredient_ids_input_text = (
    input_text.split("\n\n")
)

fresh_ingredient_id_ranges = []

for line in fresh_ingredient_id_ranges_input_text.split("\n"):
    lower, upper = line.split("-")
    fresh_ingredient_id_ranges.append((int(lower), int(upper)))

available_ingredient_ids = [
    int(ingredient_id)
    for ingredient_id in available_ingredient_ids_input_text.split("\n")
]

available_fresh_ingredient_id_count = 0
for ingredient_id in available_ingredient_ids:
    for lower, upper in fresh_ingredient_id_ranges:
        if lower <= ingredient_id <= upper:
            available_fresh_ingredient_id_count += 1
            break

print(available_fresh_ingredient_id_count)
