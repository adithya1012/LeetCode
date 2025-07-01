# operates numerous warehouses, with each warehouse i holding inventoryli] units of a particu product. You and your co-worker are responsible for dispatching these items to fulfill customer orders following a specific process:
# 1. When dispatching from warehouse i, you begin by reducing the inventory of the th warehouse by dispatch 1 units.
# 2. After your dispatch, your co-worker reduces the inventory by dispatch2 units.
# 3. This process repeats until the inventory of the ith warehouse reaches zero or becomes negative (i.e., inventory[i] ≤ 0).
# 4. For every warehouse that is emptied during your dispatch, you and your co-worker collectively earn 1 credi
# Your co-worker has the option to skip their turn, but they can only do this a limited number of times, defined by skips.
# Your task is to determine the best strategy to maximize the total credits that both you and your co-work can earn together.

# Example
# n = 6
# inventory = [10, 6, 12, 8, 15, 1]
# dispatch1 = 2
# dispatch2 = 3
# skips = 3

#
# An optimal dispatch strategy is as follows:
#
# 1. Your co-worker skips 2 turns, allowing you to empty the inventory of the 1st warehouse (Inventory: 10 → 8 → 5
# → 3 → 1 → -1).
#
# 2. Your co-worker doesn't skip any turns, and you empty the inventory of the 2nd warehouse (Inventory: 6 → 4 -
# 1 → -1).
#
# 3. Your co-worker doesn't skip any turns, and you empty the inventory of the 3rd warehouse (Inventory: 12 → 10
# → 7 → 5 → 2 → 0).
#
# 4. Your co-worker skips 1 turn, and you drain the inventory of the 4th warehouse (Inventory: 8 → 6 → 3 → 1 →
# -1).
#
# 5. Your co-worker doesn't skip any turns, and they empty the inventory of the 5th warehouse (Inventory: 15 → 13
# → 10 → 8 → 5 → 3 → 0).
#
# 6. Your co-worker doesn't skip any turns, and you empty the inventory of the 6th warehouse (Inventory: 1 → -1).
#
# As a result, the 1st, 2nd
# 1, 3rd
# 1, 4th, and 6th warehouses were completely dispatched by you, and the two of
# you collectively earned 5 credits, which is the maximum possible in this scenario.
#
# Hence, the answer is 5.

