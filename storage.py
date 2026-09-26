import json
from pathlib import Path
from models import Item


class JsonStorage:
    def __init__(self, filename="data/items.json"):
        self.path = Path(filename)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        if not self.path.exists():
            self.save([])

    def load(self):
        try:
            with self.path.open("r", encoding="utf-8") as file:
                data = json.load(file)
            return [Item.from_dict(row) for row in data]
        except (json.JSONDecodeError, OSError):
            return []

    def save(self, items):
        with self.path.open("w", encoding="utf-8") as file:
            json.dump([item.to_dict() for item in items], file, indent=2)
