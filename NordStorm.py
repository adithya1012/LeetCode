from collections import defaultdict

def process_orders(orders):
    table_orders = defaultdict(lambda: defaultdict(int))
    menu_items = set()

    for order in orders:
        parts = [part.strip() for part in order.split(',')]

        if len(parts) != 3:
            continue  # skip invalid input

        name, table_str, item = parts
        table = int(table_str)

        table_orders[table][item] += 1
        menu_items.add(item)

    print(table_orders)

    sorted_menu = sorted(menu_items)
    sorted_tables = sorted(table_orders.keys())

    # Build the header
    output = []
    header = ['Table'] + sorted_menu
    output.append(', '.join(header))

    for table in sorted_tables:
        row = [str(table)]
        for item in sorted_menu:
            row.append(str(table_orders[table].get(item, 0)))
        output.append(', '.join(row))

    return '\n'.join(output)



orders = [
    "Sarah, 7, Green Salad",
    "Sarah, 7, Cappuccino",
    "Michael, 2, Club Sandwich",
    "Marcus, 5, Sparkling Water"
]

# print(process_orders(orders))