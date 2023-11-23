import datetime
from django.core.validators import MaxValueValidator


def max_value_current_year(value):
    """
    Возвращает валидатор с текущим годом, в качестве
    максимального значения.
    """
    return MaxValueValidator(datetime.date.today().year)(value)
