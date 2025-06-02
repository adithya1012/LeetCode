from .lib.db import create_user, find_user
from .event import post_event
def register_new_user(name, password, email):
    user = create_user(name, password, email)
    post_event("user_registered", user)

def password_forgot(email, password):
    user = find_user(email)
    if user:
        post_event("forgot_password", user)
    else:
        raise f"User not found with {email}"



