from .lib.email import send_email
from .lib.slack_message import post_slack_message
from .lib.log import log
from .lib.db import create_user, find_user

def register_new_user(name, password, email):
    user = create_user(name, password, email)

    # NOTE THIS IS NOT CORRECT. IN API LOT OF IMPORTS AND LOT OF PLACES FUNCTION CALLS. THIS NEED TO BE IMPLIMENTED USING THE
    # OBSERVABILITY PATTERN
    post_slack_message("sales", f"{user.name} registered with email: {user.email}. You can spam this person")
    send_email(user.name, user.email, f"Welcome {user.name}! Thank you for Registering")
    log(f"User registered with email: {user.email}")

def password_forgot(email, password):
    user = find_user(email)
    if user:
        user.reset_password(password)
        send_email(user.name, user.email, f"{user.name}! Password Updated")
        log(f"User {user} password updated !")
    else:
        raise f"User not found with {email}"



