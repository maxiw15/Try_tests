import unittest
from main import task_1, task_2, task_3


class TestDrive(unittest.TestCase):

    def test_task_1(self):
        geo_logs = [
            {'visit1': ['Москва', 'Россия']},
            {'visit2': ['Дели', 'Индия']},
            {'visit3': ['Владимир', 'Россия']},
            {'visit4': ['Лиссабон', 'Португалия']},
            {'visit5': ['Париж', 'Франция']},
            {'visit6': ['Лиссабон', 'Португалия']},
            {'visit7': ['Тула', 'Россия']},
            {'visit8': ['Тула', 'Россия']},
            {'visit9': ['Курск', 'Россия']},
            {'visit10': ['Архангельск', 'Россия']}
        ]
        run = task_1(geo_logs)
        self.assertEqual(len(run), 6)
        for i in task_1(run):
            self.assertEqual(list(i.values())[0][1], "Россия")
            self.assertTrue(list(i.values())[0][0])
        geo_logs = [
            {'visit1': ['Москва', 'Тунис']},
            {'visit2': ['Дели', 'Индия']},
            {'visit3': ['Владимир', 'Тунис']},
            {'visit4': ['Лиссабон', 'Португалия']},
            {'visit5': ['Париж', 'Франция']},
            {'visit6': ['Лиссабон', 'Португалия']},
            {'visit7': ['Тула', 'Тунис']},
            {'visit8': ['Тула', 'Тунис']},
            {'visit9': ['Курск', 'Тунис']},
            {'visit10': ['Архангельск', 'Тунис']}
        ]
        run = task_1(geo_logs)
        self.assertEqual(len(run), 0)
        for i in task_1(run):
            self.assertEqual(list(i.values())[0][1], "Россия")
            self.assertTrue(list(i.values())[0][0])
        geo_logs = [
            {'visit1': ['Москва', 'Россия']},
            {'visit2': ['Дели', 'Россия']},
            {'visit3': ['Владимир', 'Россия']},
            {'visit4': ['Лиссабон', 'Россия']},
            {'visit5': ['Париж', 'Россия']},
            {'visit6': ['Лиссабон', 'Россия']},
            {'visit7': ['Тула', 'Россия']},
            {'visit8': ['Тула', 'Россия']},
            {'visit9': ['Курск', 'Россия']},
            {'visit10': ['Архангельск', 'Россия']}
        ]
        run = task_1(geo_logs)
        self.assertEqual(len(run), 10)
        for i in task_1(run):
            self.assertEqual(list(i.values())[0][1], "Россия")
            self.assertTrue(list(i.values())[0][0])


if __name__ == '__main__':
    unittest.main()
