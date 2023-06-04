class Currency:
    def __init__(self, value:float, rate:float) -> None:
        self._value = value
        self._rate = rate

    def calc_rate(self):
        """Multiply value on rate"""
        return round(self._value * self._rate, 4)

    def __str__(self) -> str:
        return str(round(self._value, 4))