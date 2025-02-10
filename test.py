class BeverageManager:
    def __init__(self): 
        self.store_orders = {}  # {storeId: {beverageName: quantity}}
        self.limits = {"number_of_stores": 0, "per_beverage_total": 0}

    def update_limit(self, number_of_stores, per_beverage_total):
        # self.limits["number_of_stores"] = number_of_stores
        # self.limits["per_beverage_total"] = per_beverage_total
        super()
        # Check if current state exceeds limits
        if len(self.store_orders) > number_of_stores:
            self.store_orders.clear()
        else:
            # Check each beverage against new limits
            for store in self.store_orders.values():
                for beverage, total in store.items():
                    if total > per_beverage_total:
                        self.store_orders.clear()
                        return

    def process_order(self, unique_id, store_id, beverage_name, quantity):
        # Check store limit
        if store_id not in self.store_orders:
            if len(self.store_orders) >= self.limits["number_of_stores"]:
                print(f"reject_order: {unique_id}")
                return
            self.store_orders[store_id] = {}

        # Calculate new total including the current order
        current_total = sum(store.get(beverage_name, 0) for store in self.store_orders.values())
        if store_id in self.store_orders:
            current_total -= self.store_orders[store_id].get(beverage_name, 0)

        if current_total + quantity > self.limits["per_beverage_total"]:
            print(f"reject_order: {unique_id}")
            return

        if quantity == 0:
            self.store_orders[store_id].pop(beverage_name, None)
        else:
            self.store_orders[store_id][beverage_name] = quantity

        if not self.store_orders[store_id]:
            del self.store_orders[store_id]

    def close_store(self, store_id):
        self.store_orders.pop(store_id, None)

    def print_state(self):
        number_of_stores = len(self.store_orders)
        number_of_orders = sum(len(orders) for orders in self.store_orders.values())
        beverage_counts = {}

        for orders in self.store_orders.values():
            for bev, qty in orders.items():
                beverage_counts[bev] = beverage_counts.get(bev, 0) + qty

        number_of_different_beverages = len(beverage_counts)
        number_of_beverages = sum(beverage_counts.values())

        print(f"number_of_stores: {number_of_stores}, number_of_orders: {number_of_orders}, "
              f"number_of_different_beverages: {number_of_different_beverages}, "
              f"number_of_beverages: {number_of_beverages}")


# Sample Input
# manager = BeverageManager()
# manager.update_limit(100, 1000)
# manager.process_order(1, 1, "lemonade", 100)
# manager.process_order(2, 2, "hot_chocolate", 50)
# manager.print_state()
# manager.process_order(3, 3, "lemonade", 75)
# manager.process_order(4, 1, "lemonade", 150)
# manager.process_order(5, 1, "water", 50)
# manager.print_state()

print()

# Sample Input
# manager = BeverageManager()
# manager.update_limit(2, 100)
# manager.process_order(1, 1, "lemonade", 100)
# manager.process_order(2, 2, "hot_chocolate", 50)
# manager.process_order(3, 2, "lemonade", 1)
# manager.process_order(4, 3, "hot_chocolate", 1)

# Sample Input
# manager = BeverageManager()
BeverageManager.update_limit(1, 100)
BeverageManager.process_order(1, 1, "lemonade", 100)
BeverageManager.update_limit(1, 50)
BeverageManager.print_state()