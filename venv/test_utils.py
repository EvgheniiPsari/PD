import unittest
import datetime  # Добавьте этот импорт
from utils import get_current_date, square

class TestUtilsFunctions(unittest.TestCase):

    def test_get_current_date(self):
        # Проверка, что возвращаемая дата является экземпляром datetime.date
        self.assertIsInstance(get_current_date(), datetime.date)

    def test_square_positive_number(self):
        # Проверка квадрата положительного числа
        self.assertEqual(square(4), 16)

    def test_square_negative_number(self):
        # Проверка квадрата отрицательного числа
        self.assertEqual(square(-3), 9)

    def test_square_zero(self):
        # Проверка квадрата нуля
        self.assertEqual(square(0), 0)

if __name__ == '__main__':
    unittest.main()
