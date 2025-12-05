from pathlib import Path

input_text = Path("2025/05/input.txt").read_text()

ranges_input_text, _ = (
    input_text.split("\n\n")
)

ranges = []

for line in ranges_input_text.split("\n"):
    lower, upper = line.split("-")
    ranges.append((int(lower), int(upper)))

simple_ranges = set()
for incoming_lower, incoming_upper in ranges:
    
    lower_intersection = None
    upper_intersection = None
    
    for existing_lower, existing_upper in simple_ranges:
        if existing_lower <= incoming_lower <= existing_upper:
            lower_intersection = (existing_lower, existing_upper)
        if existing_lower <= incoming_upper <= existing_upper:
            upper_intersection = (existing_lower, existing_upper)
    
    if lower_intersection is not None and upper_intersection is not None:
        
        if lower_intersection == upper_intersection:
            continue

        existing_lower, _ = lower_intersection
        _, existing_upper = upper_intersection

        simple_ranges.remove(lower_intersection)
        simple_ranges.remove(upper_intersection)
        simple_ranges.add((existing_lower, existing_upper))

    elif lower_intersection is not None:
        existing_lower, _ = lower_intersection
        simple_ranges.remove(lower_intersection)
        simple_ranges.add((existing_lower, incoming_upper))
    elif upper_intersection is not None:
        _, existing_upper = upper_intersection
        simple_ranges.remove(upper_intersection)
        simple_ranges.add((incoming_lower, existing_upper))
    else:
        simple_ranges.add((incoming_lower, incoming_upper))

total = 0
for lower, upper in simple_ranges:
    total += upper - lower + 1

print(total)