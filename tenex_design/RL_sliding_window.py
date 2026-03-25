# from collections import defaultdict, deque
#
# class RateLimit:
#     def __init__(self, window_size, max_allowed):
#         self.window_size = window_size
#         self.max_allowed = max_allowed
#         self.logs = defaultdict(deque)
#
#     def is_allowed(self, user, timestamp):
#         q = self.logs[user]
#         while q and q[0] <= (timestamp - self.window_size):
#             q.popleft()
#
#         if len(q) >= self.max_allowed:
#             # print(q)
#             return False
#
#         q.append(timestamp)
#         # print(q)
#         return True
#
#
# if __name__ == "__main__":
#     rl = RateLimit(4, 2)
#     print(rl.is_allowed("A", 1)) # True
#     print(rl.is_allowed("A", 2)) # True
#     print(rl.is_allowed("A", 3)) # False
#     print(rl.is_allowed("A", 4)) # False
#     print(rl.is_allowed("A", 5)) # True
from collections import defaultdict, deque
from enum import Enum


class RateLimiter:
    def __init__(self, window_size = 4, max_allowed = 2):
        self.window_size = window_size
        self.max_allowed = max_allowed
        self.user_count = defaultdict(deque) # {user_id : queue([])}

    def is_allowed(self, user_id, timestamp):
        q = self.user_count[user_id]
        while q and q[0] <= timestamp-self.window_size:
            q.popleft()
        if len(q) >= self.max_allowed:
            # other_info: q[0] + self.window_size + 1
            return False # 429
        else:
            q.append(timestamp)
            return True



class USERSTATUS(Enum):
    NORMAL= 1
    PREMIUM= 2

def get_user_ststus(user_id):
    data = {
        "A": USERSTATUS.NORMAL,
        "B": USERSTATUS.PREMIUM
    }
    return data.get(user_id, None)


if __name__ == "__main__":
    # different user RateLimiter:
    normal_user = RateLimiter(4, 2)
    premium_user = RateLimiter(4, 4)
    print()
    user_rl_mapper = {
        USERSTATUS.NORMAL : normal_user,
        USERSTATUS.PREMIUM : premium_user
    }

    user_id = "A"
    status = get_user_ststus(user_id)
    print(status)
    if not status:
        print("user is not registered")
    rl = user_rl_mapper[status]
    print(rl.is_allowed(user_id, 1))
    print(rl.is_allowed(user_id, 2))
    print(rl.is_allowed(user_id, 3))
    print(rl.is_allowed(user_id, 4))
    print(rl.is_allowed(user_id, 5))
    print(rl.is_allowed(user_id, 6))
    print(rl.is_allowed(user_id, 7))
    print(rl.is_allowed(user_id, 12))


