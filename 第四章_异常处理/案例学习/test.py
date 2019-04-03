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
auth.authorizor.permit_user("test program", "joe")


class Editor:
    def __init__(self):
        self.username = None
        self.menu_map = {
            "login": self.login,
            "test": self.test,
            "change": self.change,
            "quit": self.quit
        }

    def login(self):
        logged_in = False
        while not logged_in:
            username = input("username:")
            password = input("password:")
            try:
                logged_in = auth.authenticator.login(username, password)
            except auth.InvalidUsername:
                print("sorry, invalid username")
            except auth.InvalidPassword:
                print("sorry, invalid password")
            else:
                self.username = username

    def is_permitted(self, permission):
        try:
            auth.authorizor.check_permission(permission, self.username)
        except auth.NotLoggedInError as e:
            print("{} is not logged in".format(e.username))
            return False
        except auth.NotPermittedError as e:
            print("{} cannot {}".format(e.username, permission))
            return False
        else:
            return True

    def test(self):
        if self.is_permitted("test program"):
            print("testing program now...")

    def change(self):
        if self.is_permitted("change program"):
            print("changing program now...")

    def quit(self):
        raise SystemExit()

    def menu(self):
        try:
            answer = ""
            while True:
                print("""
                please enter a command:
                \tlogin\tLogin
                \ttest\tTest the program
                \tchange\tChange the program
                \tquit\tQuit
                """)
                answer = input("enter a command").lower()
                try:
                    func = self.menu_map[answer]
                except KeyError:
                    print("{} is not a valid option".format(answer))
                else:
                    func()
        finally:
            print("thank you")


Editor().menu()
