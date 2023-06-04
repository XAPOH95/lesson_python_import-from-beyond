from src import Deposit, NWO

def test_can_deposit_currency():
    deposit = Deposit('Cheebs')
    deposit.deposit(NWO(3.14, 321))
    deposit.deposit(NWO(4.2, 214))
    print(deposit)

def test_can_deposit_balance():
    deposit = Deposit('Cheebs')
    deposit.deposit(NWO(9, 100))
    deposit.deposit(NWO(4, 200))
    print(deposit.balance())