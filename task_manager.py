from matching import calculate_match
from models import Item
from storage import JsonStorage


class LostFoundManager:
    def __init__(self, storage=None):
        self.storage = storage or JsonStorage()
        self.items = self.storage.load()

    def _save(self):
        self.storage.save(self.items)

    def create_item(self, **data):
        if data["item_type"] not in {"lost", "found"}:
            raise ValueError("Item type must be lost or found.")
        item = Item.create(**data)
        self.items.append(item)
        self._save()
        return item

    def search(self, query="", item_type="all"):
        query = query.lower().strip()
        results = []

        for item in self.items:
            if item_type != "all" and item.item_type != item_type:
                continue

            searchable = " ".join([
                item.name, item.category, item.color,
                item.description, item.location
            ]).lower()

            if not query or query in searchable:
                results.append(item)

        return results

    def find_matches(self, lost_id, minimum_score=35):
        lost = next(
            (x for x in self.items
             if x.item_id == lost_id and x.item_type == "lost"),
            None
        )
        if not lost:
            raise ValueError("Lost item ID not found.")

        matches = []
        for found in self.items:
            if found.item_type != "found" or found.status != "open":
                continue

            score, reasons = calculate_match(lost, found)
            if score >= minimum_score:
                matches.append({
                    "item": found,
                    "score": score,
                    "reasons": reasons,
                })

        return sorted(matches, key=lambda x: x["score"], reverse=True)

    def statistics(self):
        lost = sum(x.item_type == "lost" for x in self.items)
        found = sum(x.item_type == "found" for x in self.items)

        possible_pairs = lost * found
        matched_pairs = 0

        for item in self.items:
            if item.item_type == "lost":
                if self.find_matches(item.item_id):
                    matched_pairs += 1

        return {
            "total": len(self.items),
            "lost": lost,
            "found": found,
            "possible_pairs": possible_pairs,
            "matched_pairs": matched_pairs,
        }
