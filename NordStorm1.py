data = {
  "id": "item1",
  "category": "shoes",
  "variants": [
    {
      "id": 1,
      "size": "M",
      "color": "red",
      "cost": 100,
      "stock": 4
    },
    {
      "id": 2,
      "size": "M",
      "color": "blue",
      "cost": 110,
      "stock": 2
    },
    {
      "id": 3,
      "size": "L",
      "color": "red",
      "cost": 120,
      "stock": 3
    },
    {
      "id": 4,
      "size": "L",
      "color": "blue",
      "cost": 100,
      "stock": 1
    },
    {
      "id": 5,
      "size": "M",
      "color": "blue",
      "cost": 100,
      "stock": 1
    }
  ]
}

class Backend:
    def __init__(self):
        pass

    def request_validate(self):
        pass

    def DB_fetch(self):
        return data

    def match(self, filter):
        data = self.DB_fetch()
        data = data["variants"]
        result = []
        for var in data:
            not_match = False
            for key, val in filter.items():
                if key in var:
                    if filter[key] != var[key]:
                        not_match = True
                        break
            if not not_match:
                result.append([var["cost"],var["id"]])
        result = [j for i,j in sorted(result)]
        return result


filter = {
    "category": "shoes",
    "color": "blue",
    "size": "M",
}

b = Backend()
print(b.match(filter))

