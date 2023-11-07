import pytest
from library import fibbonachi


class TestFibbonachi:

    # Параметризованный тест для различных значений n и ожидаемых результат
    @pytest.mark.parametrize("n, expected_result", [
        (0, []),
        (1, [0]),
        (2, [0, 1]),
        (5, [0, 1, 1, 2, 3]),
        (10, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
    ])
    def test_fibbonachi(self, n, expected_result):
        actual_result = fibbonachi(n)
        assert actual_result == expected_result

    # Тест для случая n = -1 (отрицательное значение)
    def test_fibbonachi_negative_n(self):
        with pytest.raises(ValueError):
            fibbonachi(-1)