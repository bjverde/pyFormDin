from babel.numbers import format_decimal

class NumberHelper():
    def __init__(self, locale_default=None, number_decimals_default=None):
        self.locale_default = locale_default if locale_default is not None else "pt_BR"
        self.number_decimals_default = number_decimals_default if number_decimals_default is not None else 2

    def format_number(self, value: float, casas: int = 2, locale: str = "pt_BR") -> str:
        """
        Formata um número com quantidade de casas decimais definida.
        
        :param value: valor numérico a formatar
        :param casas: quantidade de casas decimais
        :param locale: padrão de formatação (ex: 'pt_BR', 'en_US')
        :return: número formatado como string
        """
        formato = f"#,##0.{''.join(['0'] * casas)}" if casas > 0 else "#,##0"
        return format_decimal(value, format=formato, locale=locale)
    
    def format_number_default(self, value: float, casas: int = None) -> str:
        casas = casas if casas is not None else self.number_decimals_default
        return self.format_number(value, casas=casas, locale=self.locale_default)

    def format_number_brazil(self, value: float, casas: int = 2) -> str:
        """
        Formata um número para o padrão brasileiro (pt_BR).
        """
        return self.format_number(value, casas=casas, locale="pt_BR")

    def format_number_usa(self, value: float, casas: int = 2) -> str:
        """
        Formata um número para o padrão americano (en_US).
        """
        return self.format_number(value, casas=casas, locale="en_US")
