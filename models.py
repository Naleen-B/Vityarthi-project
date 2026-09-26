from dataclasses import dataclass, asdict
from uuid import uuid4


@dataclass
class Item:
    item_id: str
    item_type: str
    name: str
    category: str
    color: str
    description: str
    location: str
    date: str
    contact: str
    status: str = "open"

    @classmethod
    def create(cls, item_type, name, category, color, description,
               location, date, contact):
        return cls(
            item_id=str(uuid4())[:8].upper(),
            item_type=item_type,
            name=name,
            category=category,
            color=color,
            description=description,
            location=location,
            date=date,
            contact=contact,
        )

    def to_dict(self):
        return asdict(self)

    @classmethod
    def from_dict(cls, data):
        return cls(**data)
