from abc import ABC, abstractmethod
from collections import defaultdict


# -------------------------------------------------------------------
# 1. Data models
# -------------------------------------------------------------------

class User:
    def __init__(self, user_id, name, preferences=None):
        self.user_id = user_id
        self.name = name
        self.preferences = preferences if preferences is not None else []

    def __repr__(self):
        return f"User({self.name})"


class Order:
    def __init__(self, order_id, user):
        self.order_id = order_id
        self.user = user          # the owner of this order

    def __repr__(self):
        return f"Order({self.order_id}, owner={self.user.name})"


class Notification:
    def __init__(self, event_type, message, user):
        self.event_type = event_type
        self.message = message
        self.user = user


# -------------------------------------------------------------------
# 2. Channel abstraction (Strategy pattern)
# -------------------------------------------------------------------

class Channel(ABC):
    @abstractmethod
    def send(self, notification):
        pass


class EmailChannel(Channel):
    def send(self, notification):
        print(f"[EMAIL] To: {notification.user.name} | {notification.message}")


class SMSChannel(Channel):
    def send(self, notification):
        print(f"[SMS]   To: {notification.user.name} | {notification.message}")


class PushChannel(Channel):
    def send(self, notification):
        print(f"[PUSH]  To: {notification.user.name} | {notification.message}")


# -------------------------------------------------------------------
# 3. NotificationService
#    Subscription key is (event_type, user_id) — so only the
#    relevant user gets notified, not everyone subscribed to the event.
# -------------------------------------------------------------------

class NotificationService:
    def __init__(self):
        # (event_type, user_id) -> User
        self._subscribers = {}
        self._channels = {
            "email": EmailChannel(),
            "sms":   SMSChannel(),
            "push":  PushChannel(),
        }

    def subscribe(self, user, event_type):
        """Subscribe a specific user to a specific event type."""
        key = (event_type, user.user_id)
        self._subscribers[key] = user

    def send(self, event_type, user, message):
        """
        Send to a specific user for a specific event.
        Only fires if that user actually subscribed to this event.
        """
        key = (event_type, user.user_id)
        if key not in self._subscribers:
            print(f"[INFO] {user.name} is not subscribed to: {event_type}")
            return
        notification = Notification(event_type, message, user)
        self._dispatch(notification)

    def _dispatch(self, notification):
        for pref in notification.user.preferences:
            channel = self._channels.get(pref)
            if channel:
                channel.send(notification)
            else:
                print(f"[WARN] Unknown channel: {pref}")

    def register_channel(self, name, channel):
        self._channels[name] = channel


# -------------------------------------------------------------------
# 4. OrderService — raises events when order status changes
# -------------------------------------------------------------------

class OrderService:
    def __init__(self, notification_service):
        self.notification_service = notification_service
        self._orders = {}

    def place_order(self, order):
        self._orders[order.order_id] = order
        # Auto-subscribe the order owner to updates for their order
        self.notification_service.subscribe(order.user, f"order.{order.order_id}.shipped")
        self.notification_service.subscribe(order.user, f"order.{order.order_id}.cancelled")
        print(f"[ORDER] Placed {order} for {order.user.name}")

    def ship_order(self, order_id):
        order = self._orders.get(order_id)
        if not order:
            print(f"[ERROR] Order {order_id} not found")
            return
        self.notification_service.send(
            event_type=f"order.{order_id}.shipped",
            user=order.user,
            message=f"Your order #{order_id} has shipped!",
        )

    def cancel_order(self, order_id):
        order = self._orders.get(order_id)
        if not order:
            print(f"[ERROR] Order {order_id} not found")
            return
        self.notification_service.send(
            event_type=f"order.{order_id}.cancelled",
            user=order.user,
            message=f"Your order #{order_id} has been cancelled.",
        )


# -------------------------------------------------------------------
# 5. Example usage
# -------------------------------------------------------------------

if __name__ == "__main__":
    notif_service = NotificationService()
    order_service = OrderService(notif_service)

    alice = User("u1", "Alice", preferences=["email", "push"])
    bob   = User("u2", "Bob",   preferences=["sms"])

    order_a = Order("1001", alice)
    order_b = Order("1002", bob)
    order_c = Order("1003", alice)

    order_service.place_order(order_a)
    order_service.place_order(order_b)
    order_service.place_order(order_c)

    print("\n=== Shipping order 1001 (Alice's) ===")
    order_service.ship_order("1001")

    print("\n=== Shipping order 1002 (Bob's) ===")
    order_service.ship_order("1002")

    print("\n=== Cancelling order 1003 (Alice's) ===")
    order_service.cancel_order("1003")

    print("\n=== Trying to ship unknown order ===")
    order_service.ship_order("9999")