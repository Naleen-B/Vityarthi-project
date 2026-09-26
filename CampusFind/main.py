from task_manager import LostFoundManager
from validators import get_non_empty, get_choice
from utils import print_item, pause


def register_lost(manager):
    print("\n--- Report Lost Item ---")
    item = manager.create_item(
        item_type="lost",
        name=get_non_empty("Item name: "),
        category=get_non_empty("Category: "),
        color=get_non_empty("Color: "),
        description=get_non_empty("Description: "),
        location=get_non_empty("Last seen location: "),
        date=get_non_empty("Date (YYYY-MM-DD): "),
        contact=get_non_empty("Contact info: "),
    )
    print(f"\nLost item registered with ID: {item.item_id}")


def register_found(manager):
    print("\n--- Report Found Item ---")
    item = manager.create_item(
        item_type="found",
        name=get_non_empty("Item name: "),
        category=get_non_empty("Category: "),
        color=get_non_empty("Color: "),
        description=get_non_empty("Description: "),
        location=get_non_empty("Found location: "),
        date=get_non_empty("Date (YYYY-MM-DD): "),
        contact=get_non_empty("Contact info: "),
    )
    print(f"\nFound item registered with ID: {item.item_id}")


def search_items(manager):
    print("\n--- Search Items ---")
    query = input("Keyword (press Enter for all): ").strip()
    item_type = get_choice(
        "Type [all/lost/found]: ", ["all", "lost", "found"]
    )
    results = manager.search(query, item_type)
    if not results:
        print("\nNo matching items found.")
    else:
        for item in results:
            print_item(item)
    pause()


def find_matches(manager):
    print("\n--- Smart Match ---")
    item_id = get_non_empty("Enter lost item ID: ")
    matches = manager.find_matches(item_id)
    if not matches:
        print("\nNo possible matches found.")
    else:
        for match in matches:
            print(
                f"\nFound ID: {match['item'].item_id}"
                f"\nItem: {match['item'].name}"
                f"\nMatch Score: {match['score']}%"
                f"\nReasons: {', '.join(match['reasons'])}"
            )
    pause()


def show_report(manager):
    print("\n--- Statistics Report ---")
    report = manager.statistics()
    print(f"Total records : {report['total']}")
    print(f"Lost reports  : {report['lost']}")
    print(f"Found reports : {report['found']}")
    print(f"Possible pairs: {report['possible_pairs']}")
    print(f"Matched pairs : {report['matched_pairs']}")
    pause()


def main():
    manager = LostFoundManager()

    while True:
        print("\n==============================")
        print("       CAMPUSFIND")
        print(" Smart Lost & Found System")
        print("==============================")
        print("1. Report lost item")
        print("2. Report found item")
        print("3. Search items")
        print("4. Find possible matches")
        print("5. View statistics")
        print("6. Exit")

        choice = input("Choose an option: ").strip()

        try:
            if choice == "1":
                register_lost(manager)
            elif choice == "2":
                register_found(manager)
            elif choice == "3":
                search_items(manager)
            elif choice == "4":
                find_matches(manager)
            elif choice == "5":
                show_report(manager)
            elif choice == "6":
                print("Thank you for using CampusFind.")
                break
            else:
                print("Invalid option. Please choose 1-6.")
        except ValueError as exc:
            print(f"Input error: {exc}")
        except Exception as exc:
            print(f"Unexpected error: {exc}")


if __name__ == "__main__":
    main()
