##### Without
from enum import Enum


# class User:
#     def __init__(self, id, name):
#         self.id = id
#         self.name = name
#
# class slack_login:
#     def new_user(self, user):
#         print(f"[Email] Welcome email: {user.name}")
#         print(f"[Log] user Logged_in: {user.name}")
#
#
#     def pass_reset(self, user):
#         print(f"collect password from {user.name}")
#         print(f"[Email] New Password: {user.name}")
#         print(f"[Log] user Password Reset: {user.name}")


#### With

class EventType(Enum):
    NEW_USER = "new_user"
    RESET_PASS = "reset_pass"

class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Email_Service:
    def welcome_email(self, user: User):
        print("Welcome email : ", user.name)

    def promotinal_email(self, user: User):
        print("Promo email : ", user.name)

class Log_Service:
    def User_login(self, user: User):
        print("User Account created: ", user.name)

    def User_reset_password(self, user: User):
        print("User reset the Password:", user.name)


class Pub_Sub:
    def __init__(self):
        self.subscribe = {}

    def event_subscribe(self, event_name: EventType, fn):
        if event_name in self.subscribe:
            self.subscribe[event_name].add(fn)
        self.subscribe[event_name] = {fn}

    def event_publisher(self, event, user):
        for fn in self.subscribe.get(event, {}):
            fn(user)


class Slack:
    def __init__(self, event_bus):
        self.event_bus = event_bus

    def user_created_account(self, user):
        self.event_bus.event_publisher(EventType.NEW_USER, user)

    def user_reset_password(self, user):
        self.event_bus.event_publisher(EventType.RESET_PASS, user)

event_bus = Pub_Sub()
app = Slack(event_bus)


user1 = User("ABC", 1)
user2 = User("XYZ", 2)

email = Email_Service()
log = Log_Service()

# user created account
event_bus.event_subscribe(EventType.NEW_USER, email.welcome_email)
event_bus.event_subscribe(EventType.NEW_USER, email.promotinal_email)
event_bus.event_subscribe(EventType.NEW_USER, log.User_login)

# Reset password
event_bus.event_subscribe(EventType.RESET_PASS, log.User_reset_password)

app.user_created_account(user1)
app.user_reset_password(user1)









