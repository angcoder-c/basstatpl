import pandas as pd
import decimal

def approach(num):
    return int(decimal.Decimal(num).quantize(decimal.Decimal('1'), rounding=decimal.ROUND_HALF_UP))

def first_greater_than(f, ref):
    ls = list(f)
    fgt = list(f[f >= ref])[0]
    fgti = ls.index(fgt)
    return pd.Series({'index' : fgti, 'value': fgt})

def max_interval(obj):
    max = obj.minimum + (obj.classes * obj.amplitude) + 1
    return (obj.minimum, max)