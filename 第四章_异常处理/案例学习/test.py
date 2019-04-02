from 第四章_异常处理.案例学习 import auth

# auth.authenticator.add_user('shucheng', 'shucheng_password')
# auth.authorizor.add_permissions("paint")
# auth.authorizor.check_permission("paint", "shucheng")
# auth.authenticator.is_logged_in("shucheng")
# auth.authenticator.login("shucheng", "shucheng_password")
# auth.authorizor.check_permission("paint", "shucheng")
# auth.authorizor.check_permission("mix", "shucheng")
# auth.authorizor.permit_user("mix", "shucheng")
# auth.authorizor.permit_user("paint", "shucheng")
# auth.authorizor.check_permission("paint", "shucheng")

# 创建一个测试用户并设置权限
auth.authenticator.add_user('joe', 'joepassword')
auth.authorizor.add_permissions("test program")
auth.authorizor.add_permissions("change program")
auth.authorizor.permit_user("test program")

class Editor:
    def __init__(self):
        pass