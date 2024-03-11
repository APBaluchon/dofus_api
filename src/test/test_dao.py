import unittest
from unittest.mock import MagicMock, patch

from DAO.ObjectDAO import ObjectDao


class TestObjectDAO(unittest.TestCase):
    def setUp(self):
        self.mock_cursor = MagicMock()
        self.mock_cursor.limit.return_value = self.mock_cursor  # Ensure the cursor is chainable
        self.mock_collection = MagicMock()
        self.mock_collection.find.return_value = self.mock_cursor
        self.mock_db = MagicMock()
        self.mock_db.get_collection.return_value = self.mock_collection

    def test_read_by_id_ok(self):
        ressource_id = 14144
        name = "Mycoses gelées"

        self.mock_collection.find.return_value = [{"name": name}]

        dao = ObjectDao("ressources")
        dao.DB = self.mock_db
        dao.collection = self.mock_collection
        dao_name = dao.get_object_by_id(ressource_id)[0]["name"]

        self.assertEqual(dao_name, name)

    def test_read_by_id_ko(self):
        ressource_id = 1414455

        self.mock_collection.find.return_value = []

        dao = ObjectDao("ressources")
        dao.DB = self.mock_db
        dao.collection = self.mock_collection

        self.assertEqual(dao.get_object_by_id(ressource_id), [])

    def test_read_all_ok(self):
        self.mock_cursor.__iter__.return_value = [{"_id": 1}, {"_id": 2}, {"_id": 3}]

        dao = ObjectDao("ressources")
        dao.DB = self.mock_db
        dao.collection = self.mock_collection

        self.assertIsNotNone(dao.get_all_objects(limit=3))

    def test_read_all_filtering_ok(self):
        level = 200

        first_query_results = [{"name": "Object 1", "level": level}, {"name": "Object 2", "level": level}]
        second_query_results = [{"name": "Object 1", "level": level}, {"name": "Object 2", "level": level}, {"name": "Object 3", "level": level}, {"name": "Object 4", "level": level}]

        def first_results():
            yield from first_query_results

        def second_results():
            yield from second_query_results

        self.mock_cursor.__iter__.side_effect = [first_results(), second_results()]

        dao = ObjectDao("ressources")
        dao.DB = self.mock_db
        dao.collection = self.mock_collection
        read_filtered = dao.get_all_objects(level = level)
        read_unfiltered = dao.get_all_objects()

        self.assertNotEqual(read_unfiltered, read_filtered)
        self.assertIsNotNone(read_filtered)


if __name__ == "__main__":
    unittest.main()
