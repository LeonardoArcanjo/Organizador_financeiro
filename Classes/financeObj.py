"""
The finances object is a python class and it has attributes:
    - name: str
    - value: float
    - category: str
    - numberInstalment: str
"""


def float2str_value(value: float) -> str:
    return f'R$ {value:,.2f}'


class finance:

    def __init__(self: object, name: str, value: float, category: str, numberInstalment: str) -> None:
        self.__name: str = name
        self.__value: float = value
        self.__category: str = category

        if numberInstalment.isnumeric():
            self.__numberInstalment: int = int(numberInstalment)
        else:
            self.__numberInstalment: str = "fixed"

    @property
    def name(self: object) -> str:
        return self.__name

    @property
    def value(self: object) -> float:
        return self.__value

    @value.setter
    def value(self: object, value: float) -> None:
        self.__value = value

    @property
    def category(self: object) -> str:
        return self.__category

    @category.setter
    def category(self: object, category: str) -> None:
        self.__category = category

    @property
    def numberInstalment(self: object) -> str:
        return str(self.__numberInstalment)

    @numberInstalment.setter
    def numberInstalment(self: object, numberInstalment: str) -> None:
        if numberInstalment.isnumeric():
            self.__numberInstalment: int = int(numberInstalment)
        else:
            self.__numberInstalment: str = "fixed"

    def __str__(self: object) -> str:
        return f'Finance item:\n' \
               f'name: {self.name}\n' \
               f'value: {float2str_value(self.value)}\n' \
               f'category: {self.category}\n'\
               f'Instalment: {self.numberInstalment}'
