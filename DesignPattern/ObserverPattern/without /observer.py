from api.user import register_new_user, password_forgot
from api.plan import upgarde_plan

register_new_user("Adithya", "password","seesa01@pfw.edu")
print()
register_new_user("test1", "password","test1@pfw.edu")
print()
register_new_user("test2", "password","test2@pfw.edu")
print()
password_forgot("test1@pfw.edu", "NewPassword")
print()
upgarde_plan("test2@pfw.edu")


