def try_int(value):
    if(int(value) == float(value)):
        return int(value)
    else:
        return round(float(value),2)