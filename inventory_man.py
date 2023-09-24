class Item:
    """
    Represents an item that can be picked up by a player.

    Attributes:
        name (str): The name of the item.
    """

    def __init__(self, name):
        """
        Initializes a new Item with the given name.

        Args:
            name (str): The name of the item.
        """
        self.name = name


class Player:
    """
    Represents a player who can pick up and manage items in their inventory.

    Attributes:
        inventory (list): A list to store the player's items.
    """

    def __init__(self):
        """Initializes a new Player with an empty inventory."""
        self.inventory = []

    def pick_up_item(self, item):
        """
        Allows the player to pick up an item and add it to their inventory.

        Args:
            item (Item): The item to pick up and add to the inventory.
        """
        self.inventory.append(item)
        print(f"You picked up {item.name}.")

    def discard_item(self, item_name):
        """
        Allows the player to discard an item from their inventory.

        Args:
            item_name (str): The name of the item to discard.
        """
        for item in self.inventory:
            if item.name == item_name:
                self.inventory.remove(item)
                print(f"You discarded {item_name}.")
                break
        else:
            print("Item not found in your inventory.")

    def show_inventory(self):
        """Displays the player's current inventory."""
        print("Your Inventory:")
        for item in self.inventory:
            print(f"- {item.name}")


def main():
    # Create a player
    player = Player()

    # Simulate a battle where items are dropped
    dropped_item1 = Item("Health Potion")
    dropped_item2 = Item("Sword")
    dropped_item3 = Item("Gold Coin")

    # Player picks up the dropped items after the battle
    player.pick_up_item(dropped_item1)
    player.pick_up_item(dropped_item2)
    player.pick_up_item(dropped_item3)

    # Player decides to discard an item
    player.show_inventory()
    player.discard_item("Sword")

    # Player checks their updated inventory
    player.show_inventory()


if __name__ == "__main__":
    main()
