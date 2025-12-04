from textwrap import dedent

import pytest
from part_1 import solve


@pytest.mark.parametrize(
    argnames=("input_text", "expected"),
    argvalues=[
        (".", 0),
        ("@", 1),
        ("..\n@@", 2),
        ("..@\n@@@\n@@@", 4),
        ("..@@\n@@@.\n@@@@\n@.@@", 5),
        (
            """\
            ..@@.@@@@.
            @@@.@.@.@@
            @@@@@.@.@@
            @.@@@@..@.
            @@.@@@@.@@
            .@@@@@@@.@
            .@.@.@.@@@
            @.@@@.@@@@
            .@@@@@@@@.
            @.@.@@@.@.
            """,
            13,
        ),
    ],
)
def test_solve(input_text: str, expected: int) -> None:
    input_text = dedent(input_text)
    assert solve(input_text) == expected
