import unittest

from DAO.ObjectDAO import ObjectDao


class TestObjectDAO(unittest.TestCase):
    def test_read_by_id_ok(self):
        ressource_id = 14144
        name = "Mycoses gelées"

        dao = ObjectDao("ressources")

        self.assertEqual(dao.get_object_by_id(ressource_id)[0]["name"], name)

    def test_read_by_id_ko(self):
        ressource_id = 1414455

        dao = ObjectDao("ressources")

        self.assertEqual(dao.get_object_by_id(ressource_id), [])

    def test_read_all_ok(self):

        dao = ObjectDao("ressources")

        self.assertIsNotNone(dao.get_all_objects(limit=3))


if __name__ == "__main__":
    unittest.main()
