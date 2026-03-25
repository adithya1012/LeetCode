# Simulated DB fetch
def fetch_from_db():
    return [
        {"id": 1, "name": "Alice", "age": 30, "city": "New York"},
        {"id": 2, "name": "Bob",   "age": 25, "city": "Chicago"},
        {"id": 3, "name": "Carol", "age": 35, "city": "New York"},
        {"id": 4, "name": "Dave",  "age": 25, "city": "Houston"},
        {"id": 5, "name": "Eve",   "age": 40, "city": "Chicago"},
    ]


# ---------- Generic Filter Engine ----------

OPERATORS = {
    "eq":  lambda a, b: a == b,
    "ne":  lambda a, b: a != b,
    "gt":  lambda a, b: a >  b,
    "lt":  lambda a, b: a <  b,
    "gte": lambda a, b: a >= b,
    "lte": lambda a, b: a <= b,
    "in":  lambda a, b: a in b,
    "contains": lambda a, b: b in str(a),
}

def apply_filter(record: dict, filters: list[dict]) -> bool:
    """
    Each filter is: {"field": "age", "op": "gt", "value": 28}
    All filters are AND-ed together.
    """
    for f in filters:
        field   = f["field"]
        op      = f["op"]
        value   = f["value"]

        if field not in record:
            return False                          # field doesn't exist → skip record

        operator_fn = OPERATORS.get(op)
        if not operator_fn:
            raise ValueError(f"Unsupported operator: {op}")

        if not operator_fn(record[field], value): # attribute-agnostic comparison
            return False

    return True  # passed all filters


def query(filters: list[dict]) -> list[dict]:
    data = fetch_from_db()
    return [record for record in data if apply_filter(record, filters)]


# ---------- Driver / Demo ----------

if __name__ == "__main__":

    # Q1: age > 28
    print("age > 28:")
    print(query([{"field": "age", "op": "gt", "value": 28}]))

    # Q2: city == "Chicago"
    print("\ncity == Chicago:")
    print(query([{"field": "city", "op": "eq", "value": "Chicago"}]))

    # Q3: age >= 30 AND city == "New York"   (multi-filter / AND)
    print("\nage >= 30 AND city == New York:")
    print(query([
        {"field": "age",  "op": "gte", "value": 30},
        {"field": "city", "op": "eq",  "value": "New York"},
    ]))

    # Q4: id in [1, 3, 5]
    print("\nid in [1, 3, 5]:")
    print(query([{"field": "id", "op": "in", "value": [1, 3, 5]}]))