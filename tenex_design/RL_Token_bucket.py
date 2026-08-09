# import time
#
#
# class TokenBucket:
#     """
#     Token Bucket rate limiter.
#     Bucket holds up to `capacity` tokens.
#     Tokens refill at `refill_rate` per `window_seconds`.
#     Each allowed request consumes one token.
#     """
#
#     def __init__(self, capacity: int = 4, refill_rate: int = 2, window_seconds: float = 4):
#         self.capacity = capacity           # max tokens the bucket can hold
#         self.refill_rate = refill_rate     # tokens added per window
#         self.window_seconds = window_seconds
#         self.tokens = capacity             # BUG 2 FIX: start full, not at refill_rate
#         self.last_refill_time = 0.0
#
#     def _refill(self, now: float):
#         elapsed = now - self.last_refill_time
#         if elapsed >= self.window_seconds:
#             windows_passed = int(elapsed // self.window_seconds)   # BUG 3 FIX: scale by windows
#             self.tokens = min(
#                 self.capacity,
#                 self.tokens + windows_passed * self.refill_rate
#             )
#             self.last_refill_time = now   # BUG 1 FIX: update the refill timestamp
#
#     def is_allowed(self, timestamp: float = None) -> bool:
#         now = timestamp if timestamp is not None else time.time()
#         self._refill(now)
#         if self.tokens > 0:
#             self.tokens -= 1
#             return True
#         return False
#
#
# # --- Factory functions (Strategy pattern — same interface, different configs) ---
#
# def create_normal_user() -> TokenBucket:
#     return TokenBucket(capacity=4, refill_rate=2, window_seconds=4)
#
# def create_premium_user() -> TokenBucket:
#     return TokenBucket(capacity=20, refill_rate=10, window_seconds=4)
#
#
# # --- Example usage ---
#
# if __name__ == "__main__":
#     users = {
#         "A": create_normal_user(),
#         "B": create_normal_user(),
#     }
#
#     print("--- Draining user A's bucket ---")
#     for t in [1, 2, 3, 4, 5]:
#         result = users["A"].is_allowed(timestamp=t)
#         tokens_left = users["A"].tokens
#         print(f"  t={t}: {'allowed' if result else 'REJECTED'} | tokens remaining: {tokens_left}")
#
#     print("\n--- Waiting for refill (t=10, one full window later) ---")
#     result = users["A"].is_allowed(timestamp=10)
#     print(f"  t=10: {'allowed' if result else 'REJECTED'} | tokens remaining: {users['A'].tokens}")



from collections import defaultdict, deque
from enum import Enum

class RateLimitter:
    def __init__(self, capacity: int = 4, refill_rate: int = 2, window = 4):
        self.capacity = capacity
        self.refill_rate = refill_rate
        self.window = window
        self.users = defaultdict(list) # userid: [rem, last_hit_time]

    def _refill(self, user_id, timestamp):
        if not self.users[user_id]:
            self.users[user_id] = [self.capacity-1, timestamp]
            return True
        rem, last_hit_time = self.users[user_id]
        window_passed = (timestamp - last_hit_time) // self.window
        rem = min(rem+(window_passed * self.refill_rate),  self.capacity)
        if rem:
            rem -= 1
            self.users[user_id] = [rem, timestamp]
            return True
        else:
            return False

    def is_allowed(self, user_id, timestamp):
        return self._refill(user_id, timestamp)



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