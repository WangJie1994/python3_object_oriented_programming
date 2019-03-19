class SecretString:
    """
    一个不安全的方法
    """
    def __init__(self, plain_string, pass_phrase):
        self.__plain_string = plain_string
        self.__pass_phrase = pass_phrase

    def decrypt(self, pass_phrase):
        if pass_phrase == self.__pass_phrase:
            return self.__plain_string
        else:
            return ""


secret_string = SecretString("ACME", "password")
print(secret_string.decrypt("password"))
# print(secret_string.__plain_string) # 报错
print(secret_string._SecretString__plain_string)
