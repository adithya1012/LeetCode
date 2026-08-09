from collections import defaultdict, deque
from enum import Enum

class RateLimitter:
    def __init__(self, window_size: int = 1, max_allowd: int = 2):
        self.window_size = window_size
        self.max_allowd = max_allowd
        self.users = defaultdict(deque) # userid: q

    def is_allowed(self, user_id, timestamp):
        q = self.users[user_id]
        while q and q[0] <= timestamp-self.window_size:
            q.popleft()
        if len(q) >= self.max_allowd:
            return False # 429
            # other info : q[0]+self.window_size
        q.append(timestamp)
        return True

premioum_rl = RateLimitter(4, 4)
normal_rl = RateLimitter(4, 2)

class Status(Enum):
    NORMAL = 1
    PREMIUM = 2
def get_user_status(user):
    mapper = {
        "A" : normal_rl,
        "B" : premioum_rl
    }
    # TODO: Validate User
    return mapper[user]

if __name__ == "__main__":
    user1 = "A"
    rl = get_user_status(user1)
    print(rl.is_allowed(user1, 1))
    print(rl.is_allowed(user1, 2))
    print(rl.is_allowed(user1, 3))
    print(rl.is_allowed(user1, 4))
    print(rl.is_allowed(user1, 5))
    print(rl.is_allowed(user1, 6))
    print(rl.is_allowed(user1, 7))
    print(rl.is_allowed(user1, 11))



# from collections import defaultdict, deque
# from enum import Enum
#
#
# class RateLimiter:
#     def __init__(self, window_size = 4, max_allowed = 2):
#         self.window_size = window_size
#         self.max_allowed = max_allowed
#         self.user_count = defaultdict(deque) # {user_id : queue([])}
#
#     def is_allowed(self, user_id, timestamp):
#         q = self.user_count[user_id]
#         while q and q[0] <= timestamp-self.window_size:
#             q.popleft()
#         if len(q) >= self.max_allowed:
#             # other_info: q[0] + self.window_size + 1
#             return False # 429
#         else:
#             q.append(timestamp)
#             return True
#
#
#
# class USERSTATUS(Enum):
#     NORMAL= 1
#     PREMIUM= 2
#
# def get_user_ststus(user_id):
#     data = {
#         "A": USERSTATUS.NORMAL,
#         "B": USERSTATUS.PREMIUM
#     }
#     return data.get(user_id, None)
#
#
# if __name__ == "__main__":
#     # different user RateLimiter:
#     normal_user = RateLimiter(4, 2)
#     premium_user = RateLimiter(4, 4)
#     print()
#     user_rl_mapper = {
#         USERSTATUS.NORMAL : normal_user,
#         USERSTATUS.PREMIUM : premium_user
#     }
#
#     user_id = "A"
#     status = get_user_ststus(user_id)
#     print(status)
#     if not status:
#         print("user is not registered")
#     rl = user_rl_mapper[status]
#     print(rl.is_allowed(user_id, 1))
#     print(rl.is_allowed(user_id, 2))
#     print(rl.is_allowed(user_id, 3))
#     print(rl.is_allowed(user_id, 4))
#     print(rl.is_allowed(user_id, 5))
#     print(rl.is_allowed(user_id, 6))
#     print(rl.is_allowed(user_id, 7))
#     print(rl.is_allowed(user_id, 12))
#
#
