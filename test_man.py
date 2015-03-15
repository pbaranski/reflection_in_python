from unittest import TestCase
from ref import Man


class TestMan(TestCase):
    def test_send_none(self):
        data = None
        man = Man(data)
        self.assertEqual(man.name(), None)
        self.assertEqual(man.surname, None)

    def test_send_name(self):
        name = 'pszemek'
        data = {'name':name}
        man = Man(data)
        self.assertEqual(man.name(), name)
        self.assertEqual(man.surname, None)

    def test_send_surname(self):
        surname = 'owczarski'
        data = {'surname':surname}
        man = Man(data)
        self.assertEqual(man.name(), None)
        self.assertEqual(man.surname, surname)

    def test_send_surname_and_name_dict(self):
        name = 'pszemek'
        surname = 'owczarski'
        data = {'name':name,'surname':surname}
        man = Man(data)
        self.assertEqual(man.name(), name)
        self.assertEqual(man.surname, surname)

    def test_send_surname_and_name_list(self):
        name = 'pszemek'
        surname = 'owczarski'
        data = [None, name, surname]
        man = Man(data)
        self.assertEqual(man.name(), name)
        self.assertEqual(man.surname, surname)
        self.assertEqual(man._age, None)

    def test_send_surname_and_name_as_arguments(self):
        name = 'pszemek'
        surname = 'owczarski'
        man = Man(None, name, surname)
        self.assertEqual(man.name(), name)
        self.assertEqual(man.surname, surname)

    def test_send_surname_and_name_two_dicts(self):
        name = 'pszemek'
        surname = 'owczarski'
        data1 = {'name':name}
        data2 = {'surname':surname}
        man = Man(data1, data2)
        self.assertEqual(man.name(), name)
        self.assertEqual(man.surname, surname)