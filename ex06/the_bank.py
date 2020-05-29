class Account(object):

    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
        if hasattr(self, 'value'):
            self.value = 0
        Account.ID_COUNT += 1

    def transfer(self, amount):
        self.value += amount


class Bank:
    """The bank"""

    def __init__(self):
        self.account = []

    def add(self, account):
        self.account.append(account)

    def check_account(self, account):
        """
            check if the account is valid

            @account: Account(account)
            @return         True if valid, False if invalid
        """
        if not isinstance(account, Account) or account not in self.account:
            return False

        attrs = dir(account)

        if len(attrs) % 2 == 0:
            return False

        for a in attrs:
            if a.startswith('b'):
                return False

        if not all(a in attrs for a in ('name', 'id', 'value')):
            return False

        return True

    def get_account(self, account):
        """
            @origin:  int(id) or str(name) of the account
            @return         Account or None
        """
        if isinstance(account, int):
            result = next((a for a in self.account if a.id == account), None)
        elif isinstance(account, str):
            result = next((a for a in self.account if a.name == account), None)
        else:
            raise TypeError("Account should be int(id) or str(name)")

        if result and (self.check_account(result) or self.fix_account(result)):
            return result
        else:
            return None

    def transfer(self, origin, dest, amount):
        """
            @origin:  int(id) or str(name) of the first account
            @dest:    int(id) or str(name) of the destination account
            @amount:  float(amount) amount to transfer
            @return         True if success, False if an error occured
        """
        if amount < 0:
            return False
        orig_account = get_account(origin)
        dest_account = get_account(dest)
        if not (orig_account and dest_account) or amount > orig_account.value:
            return False
        orig_account.value -= amount
        dest_account.value += amount
        return True

    def fix_account(self, account):
        """
            fix the corrupted account

            @account: int(id) or str(name) of the account
            @return         True if success, False if an error occured
        """
        if not isinstance(account, Account) or account not in self.account:
            return False

        attrs = dir(account)

        if len(attrs) % 2 == 0:
            if 'fixed' in attrs:
                delattr(account, 'fixed')
            else:
                account.fixed = True

        for a in attrs:
            if a.startswith('b'):
                delattr(account, a)
                return fix_account(account)

        if not all(a in attrs for a in ('name', 'id', 'value')):
            return False

        return True
