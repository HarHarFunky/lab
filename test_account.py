from account import Account

def test_init():
    account_one = Account('john')
    assert account_one.get_name() == 'john'
    assert account_one.get_balance() == 0

def test_deposit():
    account_one = Account('john')
    assert account_one.deposit(1000000) is True
    assert account_one.get_balance() == 1000000

def test_withdraw():
    account_one = Account('john')
    assert account_one.deposit(1000000) is True
    assert account_one.withdraw(500000) is True
    assert account_one.withdraw(750000) is False
    assert account_one.get_balance() == 500000
