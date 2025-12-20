from part_1 import solve


def test_solve() -> None:
    input_text = "7,1\n11,1\n11,7\n9,7\n9,5\n2,5\n2,3\n7,3"
    assert solve(input_text) == 50
