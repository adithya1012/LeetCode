from .lib.email import send_email
from .lib.slack_message import post_slack_message
from .lib.log import log
from .lib.db import create_user, find_user

def upgarde_plan(email):
    user = find_user(email)
    post_slack_message("sales",f"User {user} upgrading the Plan")
    send_email(user.name, user.email, f"Thank you {user.name} for upgrading plan !")
    log(f"User {user} upgraded")


# NOTE:
#