import pytest
from library import bubble_sort


class TestBubbleSort:

    # Параметризованный тест для различных входных данных
    @pytest.mark.parametrize("input_data, expected_result", [
        ([], []),
        ([5], [5]),
        ([4, 3, 32, 1, 6, 12], [3, 3, 4, 6, 12, 32]),
        ([1, 2, 3, 4], [1, 2, 3, 4]),
        ([4, 3, 2, 1], [1, 2, 3, 4])
    ])
    def test_bubble_sort(self, input_data, expected_result):
        actual_result = bubble_sort(input_data)
        assert actual_result == expected_result

    # Тест для попытки сортировки списка, содержащего некорректные значения
    @pytest.mark.parametrize("input_data", [(4, 3, None, 6, 12), (4, 3, "2", 6, 12)])
    def test_bubble_sort_with_invalid_input(self, input_data):
        with pytest.raises(TypeError):
            bubble_sort(list(input_data))