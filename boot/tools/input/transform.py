# Convertir un float en un int en caso de ser posible
def float_or_int(value: int|float) -> int | float:
    if value.is_integer():
        return int(value)
    return round(float(value), 2)

