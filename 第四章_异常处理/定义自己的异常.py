# class InvalidWithdrawal(Exception):
#     pass
#
# raise InvalidWithdrawal("you don't have $50 in your account")


class InvalidWithdrawal(Exception):
    def __init__(self, balance, amount):
        super().__init__("account doesn't have ${}.".format(amount))
        self.amount = amount
        self.balance = balance

    def overage(self):
        return self.amount - self.balance


try:
    raise InvalidWithdrawal(25, 50)
except InvalidWithdrawal as e:
    print("you are over {}".format(e.overage()))
