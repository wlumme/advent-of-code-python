import pytest
from part_2 import solve


@pytest.mark.parametrize(
    argnames=("input_text", "expected"),
    argvalues=[
        ("1-2\n1-2\n\n", 2),
        ("1-2\n2-3\n\n", 3),
        ("1-2\n3-4\n\n", 4),
        ("1-4\n2-3\n\n", 4),
        ("3-4\n1-2\n\n", 4),
        ("3-4\n2-3\n\n", 3),
        ("3-4\n3-4\n\n", 2),
        ("2-3\n1-4\n\n", 4),
        ("3-5\n10-14\n16-20\n12-18\n\n1\n5\n8\n11\n17\n32", 14),
    ],
)
def test_solve(input_text: str, expected: int) -> None:
    assert solve(input_text) == expected
