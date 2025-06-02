from api.user import register_new_user, password_forgot
from api.plan import upgarde_plan
from api.log_listener import setup_log_event_listener
from api.slack_listener import setup_slack_event_handler


# Now it is easy to unsubscribe the functions from the event.
# Say if slack is not necessary we can comment it so no slack will be sent. We can also define a remove-event which removes or
# unsubscribe the function from event.

setup_log_event_listener()
setup_slack_event_handler()

# all the associated functions will be called with user data when the event is posted.

register_new_user("Adithya", "password","seesa01@pfw.edu")
print()
register_new_user("test1", "password","test1@pfw.edu")
print()
register_new_user("test2", "password","test2@pfw.edu")
print()
password_forgot("test1@pfw.edu", "NewPassword")
print()
upgarde_plan("test2@pfw.edu")

# https://www.youtube.com/watch?v=oNalXg67XEE&ab_channel=ArjanCodes


# NOTE: plan is not updated with oberver pattern


