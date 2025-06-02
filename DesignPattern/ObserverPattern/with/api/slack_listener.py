from .lib.slack_message import post_slack_message
from .event import subscribe

def handle_user_registered_event(user):
    post_slack_message("sales", f" {user.name} has registered with email {user.email}")

def handle_plan_upgrade_event(user):
    post_slack_message("sales", f" {user.email} Upgraded the plan ")

def setup_slack_event_handler():
    subscribe("user_registered", handle_user_registered_event)
    subscribe("plan_upgrade", handle_plan_upgrade_event)









