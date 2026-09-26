import tempfile
import unittest
from pathlib import Path

from models import Item
from matching import calculate_match
from storage import JsonStorage
from task_manager import LostFoundManager


class TestCampusFind(unittest.TestCase):
    def test_same_category_and_color_increase_score(self):
        lost = Item.create(
            "lost", "Boat earbuds", "electronics", "black",
            "wireless earbuds", "library", "2026-09-20", "student"
        )
        found = Item.create(
            "found", "Bluetooth earbuds", "electronics", "black",
            "wireless earphones", "library", "2026-09-20", "student"
        )
        score, reasons = calculate_match(lost, found)
        self.assertGreaterEqual(score, 80)
        self.assertIn("same category", reasons)

    def test_search(self):
        with tempfile.TemporaryDirectory() as directory:
            storage = JsonStorage(str(Path(directory) / "items.json"))
            manager = LostFoundManager(storage)
            manager.create_item(
                item_type="lost", name="Blue Bottle",
                category="bottle", color="blue",
                description="steel bottle", location="canteen",
                date="2026-09-20", contact="x"
            )
            self.assertEqual(len(manager.search("blue")), 1)

    def test_invalid_match_id(self):
        with tempfile.TemporaryDirectory() as directory:
            storage = JsonStorage(str(Path(directory) / "items.json"))
            manager = LostFoundManager(storage)
            with self.assertRaises(ValueError):
                manager.find_matches("INVALID")


if __name__ == "__main__":
    unittest.main()
