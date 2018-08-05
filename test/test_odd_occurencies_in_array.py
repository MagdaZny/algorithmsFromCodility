from src.odd_occurenries_in_array import solution


def test_return_itself_wnen_one_element_in_array():
    assert solution([1]) == 1


def test_return_one_wnen_three_elements_in_array():
    assert solution([3, 3, 1]) == 1


def test_return_one_wnen_three_elements_in_array2():
    assert solution([9, 3, 9, 3, 1]) == 1
