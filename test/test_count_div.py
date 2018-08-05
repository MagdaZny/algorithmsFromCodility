from src.count_div import solution


def test_return_zero_when_a_b_equals_zero():
    assert solution(0, 0, 1) == 1


def test_return_zero_when_a_b_equals_zero1():
    assert solution(1, 1, 2) == 0


def test_return_zero_when_a_b_equals_zero11():
    assert solution(1, 1, 11) == 0


def test_return_zero_when_a_b_equals_zero2():
    assert solution(3, 3, 3) == 1


def test_return_zero_when_a_b_equals_zero3():
    assert solution(1, 5, 2) == 2


def test_return_zero_when_a_b_equals_zero4():
    assert solution(3, 20, 5) == 4


def test_return_zero_when_a_b_equals_zero5():
    assert solution(3, 21, 20) == 1


def test_return_zero_when_a_b_equals_zero6():
    assert solution(2, 10, 2) == 5


def test_return_zero_when_a_b_equals_zero7():
    assert solution(2, 10, 10) == 1


def test_return_zero_when_a_b_equals_zero8():
    assert solution(20, 30, 10) == 2


def test_return_zero_when_a_b_equals_zero9():
    assert solution(6, 11, 2) == 3


