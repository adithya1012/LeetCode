import heapq

class node:
  def __init__(self):
    pass
test = [[1, node()], [1, node()]]
heapq.heapify(test)
print(test)