from external import CurrencyProject as CP

class Deposit:
    def __init__(self, client:str) -> None:
        self._client = client
        self._balance = list()

    def deposit(self, currency:CP.Currency):
        self._balance.append(currency)

    def balance(self):
        total:float = 0.0
        currency:CP.Currency
        for currency in self._balance:
            total += currency.calc_rate()
        return total

    def withdraw(self) -> CP.Currency:
        raise NotImplementedError("Sorry, withdrawing is not available yet")

    def __str__(self) -> str:
        return self._client + ' ' + str(self.balance())