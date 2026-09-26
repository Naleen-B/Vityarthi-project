def print_item(item):
    print("\n------------------------------")
    print(f"ID          : {item.item_id}")
    print(f"Type        : {item.item_type.title()}")
    print(f"Item        : {item.name}")
    print(f"Category    : {item.category}")
    print(f"Color       : {item.color}")
    print(f"Description : {item.description}")
    print(f"Location    : {item.location}")
    print(f"Date        : {item.date}")
    print(f"Status      : {item.status}")
    print("------------------------------")


def pause():
    input("\nPress Enter to continue...")
