from .lib.log import log
from .event import subscribe

def handle_user_registered_event(user):
    log(f"{user.name} is registered !")

def handle_forgot_password_event(user):
    log(f"{user.name} Updated Password")

def handle_plan_upgrade_event(user):
    log(f"{user.name} Updated Password")

def setup_log_event_listener():
    subscribe("user_registered", handle_user_registered_event)
    subscribe("forgot_password", handle_forgot_password_event)
    subscribe("plan_upgrade", handle_plan_upgrade_event)





