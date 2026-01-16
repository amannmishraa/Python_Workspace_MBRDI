# Scoops & Scripts - Ice Cream Shop Management System

BASIC_FLAVORS = ("Vanilla", "Chocolate", "Strawberry")

FLAVOR_PRICES = {
    "Vanilla": 20,
    "Chocolate": 25,
    "Strawberry": 30
}

SERVING_TYPES = frozenset({"Cone", "Cup"})


transaction_history = []


def create_order(flavor, serving, toppings):

    # Validate flavor
    if flavor not in BASIC_FLAVORS:
        raise ValueError("Invalid flavor selected.")

    # Validate serving type
    if serving not in SERVING_TYPES:
        raise ValueError("Invalid serving type. Must be Cone or Cup.")

    toppings_set = set(toppings)

    base_price = FLAVOR_PRICES[flavor]
    topping_price = 0.50 * len(toppings_set)
    total_price = base_price + topping_price

    # Record transaction
    order = {
        "flavor": flavor,
        "serving": serving,
        "toppings": toppings_set,
        "total_price": round(total_price, 2)
    }

    transaction_history.append(order)
    return order


def get_transaction_history():
    return transaction_history

if __name__ == "__main__":
    order1 = create_order(
        flavor="Vanilla",
        serving="Cone",
        toppings=["nuts", "sprinkles", "nuts"]  # duplicates auto-removed
    )

    order2 = create_order(
        flavor="Chocolate",
        serving="Cup",
        toppings=["caramel"]
    )

    print("Orders placed:")
    for t in get_transaction_history():
        print(t)
