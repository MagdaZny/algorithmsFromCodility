from src.passing_cars import solution


def test_return_zero_when_only_one_element():
    assert solution([1]) == 0


def test_return_zero_when_only_one_element2():
    assert solution([1]) == 0


def test_return_zero_when_two_elements1():
    assert solution([1,0]) == 0


def test_return_zero_when_two_elements2():
    assert solution([0,1]) == 1


def test_return_zero_when_two_elements3():
    assert solution([0,1,0,1,1]) == 5


