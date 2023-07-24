from datetime import datetime


class FourDigitYearConverter:
    regex = "[0-9]{4}"

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return "%04d" % value


class MyFloatConverter:
    regex = "[+-]?(\d*\.)?\d+"

    def to_python(self, value):
        return float(value)

    def to_url(self, value):
        return str(value)


class MyDateConverter:
    regex = "(0[1-9]|[1-2][0-9]|3[0-1])-(0[1-9]|1[0-2])-[0-9]{4}"
    # regex = "\d\d-\d\d-\d\d\d\d"

    def to_python(self, value):
        return datetime.strptime(value, '%d-%m-%Y')

    def to_url(self, value):
        return value.strftime('%d-%m-%Y')
