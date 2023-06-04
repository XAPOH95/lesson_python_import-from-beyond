from external import CurrencyProject as CP

class NWO(CP.Currency):
    def __str__(self) -> str:
        return super().__str__() + ' W'