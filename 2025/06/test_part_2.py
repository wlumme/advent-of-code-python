import pytest
from part_2 import solve


@pytest.mark.parametrize(
    argnames=("input_text", "expected"),
    argvalues=[
        ("123\n 45\n  6\n*  ", 8544),
        ("328\n64 \n98 \n+  ", 625),
        (" 51\n387\n215\n*  ", 3_253_600),
        ("64 \n23 \n314\n+  ", 1058),
        (
            "123 328  51 64 \n 45 64  387 23 \n  6 98  215 314\n*   +   *   +  ",
            3_263_827,
        ),
    ],
)
def test_solve(input_text: str, expected: int) -> None:
    assert solve(input_text) == expected
