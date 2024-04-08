import unittest
import pandas as pd
from app.io.input import read_from_file_builtin, read_from_file_pandas


class TestReadFromFile(unittest.TestCase):
    def test_read_from_file_builtin_exists(self):
        # Перевірка чи функція read_from_file_builtin існує
        self.assertTrue(callable(read_from_file_builtin))

    def test_read_from_file_pandas_exists(self):
        # Перевірка чи функція read_from_file_pandas існує
        self.assertTrue(callable(read_from_file_pandas))

    def test_read_from_file_builtin_correct_data(self):
        # Перевірка правильності зчитування даних з файлу за допомогою функції read_from_file_builtin
        expected_data = "Test data from input.txt"
        with open("input.txt", "w") as file:
            file.write(expected_data)
        data = read_from_file_builtin("input.txt")
        self.assertEqual(data, expected_data)

    def test_read_from_file_pandas_correct_data(self):
        # Перевірка правильності зчитування даних з файлу за допомогою функції read_from_file_pandas
        expected_data = "Test data from input.csv"
        with open("input.csv", "w") as file:
            file.write(expected_data)
        data = read_from_file_pandas("input.csv")
        self.assertEqual(data, expected_data)

