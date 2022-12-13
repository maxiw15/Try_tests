import unittest
from main import task_1, task_2, task_3, YandexDisk
from TOKEN_secret import token


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

    def test_task_2(self):
        ids = {'user1': [213, 213, 213, 15, 213],
               'user2': [54, 54, 119, 119, 119],
               'user3': [213, 98, 98, 35]}
        res = task_2(ids)
        self.assertEqual(res, [98, 35, 15, 213, 54, 119])
        ids = {'user1': [],
               'user2': [],
               'user3': []}
        res = task_2(ids)
        self.assertEqual(res, [])

    def test_task_3(self):
        stats = {'facebook': 120, 'yandex': 160, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
        res = task_3(stats)
        self.assertEqual(res, ['yandex'])
        stats = {'facebook': 160, 'yandex': 160, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
        res = task_3(stats)
        self.assertEqual(res, ['facebook', 'yandex'])

    def test_yandex_folder_create(self):
        test_yandex = YandexDisk(token)
        res = test_yandex.create_folder(name_folder="test")
        # self.assertEqual(res, 201)
        res = test_yandex.exist_folder()
        self.assertIn("test", res)



if __name__ == '__main__':
    unittest.main()
