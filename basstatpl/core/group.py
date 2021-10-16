from math import log
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import decimal

def approach(num):
    return int(decimal.Decimal(num).quantize(decimal.Decimal('1'), rounding=decimal.ROUND_HALF_UP))

def max_interval(obj):
    max = obj.minimum + (obj.sturges_rule * obj.amplitude) + 1
    return (obj.minimum,max)

class GroupedData:
  def __init__(self, data=None):
    self.source = data
    self.n = len(data)
    self.minimum = min(data)
    self.maximum = max(data)
    self.sturges_rule = 1 + (3.3 * log(self.n,10))
    self.rank = self.maximum - self.minimum
    self.interval = self.rank/approach(self.sturges_rule)
    self.amplitude = approach(self.interval)

    intervals = pd.interval_range(start= self.minimum,
                                       end= max_interval(self)[1],
                                       freq= self.amplitude,
                                       closed="left")
    df = pd.DataFrame({'Lr':list(intervals)})
    df['La_float'] = [pd.Interval(i.left - 0.5, i.right - 0.5, closed = 'both')
                      for i in df['Lr']]
    df['La'] = [pd.Interval(i.left, i.right - 1, closed = 'both')
                for i in df['Lr']]                    
    df['Xi'] = [(i.left + i.right)/2 for i in df['La']]

    dist = [list(filter(lambda x: x in i, self.source)) for i in df['Lr']]
    df['Fi'] = [len(j) for j in dist]
    df['Fa'] = df['Fi'].cumsum()
    df['Fr'] = df['Fi'] / self.n
    df['FrP'] = df['Fr'] * 100
    df['FG'] = df['Fr'] * 360

    self.frequency_table = df

  def __str__(self):
    message = f'''Count: {self.n}\nMin: {self.minimum}\nMax: {self.maximum}'''
    return f'{message}'

  def mean(self, procedure = False):
    if procedure:
      df = self.frequency_table 
    else:
      df = self.frequency_table.copy()

    df['Xi*Fi'] = df['Xi'] * df['Fi']
    return df['Xi*Fi'].sum() / self.n

  def median(self):
    df = self.frequency_table 
    fa = df['Fa']
    fa_ls = list(fa)
    first_greater = list(fa[fa >= (self.n/2)])[0]
    first_greater_index = fa_ls.index(first_greater)

    lri = df['La_float'].iloc[first_greater_index].left
    faa = fa_ls[first_greater_index - 1]
    f = df['Fi'].iloc[first_greater_index]

    return (lri + ( ((self.n/2)-faa) / f ) * self.amplitude)

  def mode(self):
    df = self.frequency_table 
    mayor_fi = df['Fi'].max()
    fila_fi = list(df['Fi']).index(mayor_fi)

    lri = df['La_float'].iloc[fila_fi].left
    uno = mayor_fi - df['Fi'].iloc[fila_fi - 1]
    dos = mayor_fi - df['Fi'].iloc[fila_fi + 1]

    return (lri + ((uno)/(uno + dos)) * self.amplitude)

  def position(self, p, m):
    df = self.frequency_table
    q = (p * self.n) / m
    fa = df['Fa']
    elem = list(fa[fa >= (q)])[0]
    elem_index = list(fa).index(elem)

    faa = fa.iloc[elem_index -1]
    fi = df['Fi'].iloc[elem_index]
    lri = df['La_float'].iloc[elem_index].left

    return lri + ((q - faa) / fi) * self.amplitude

  def var(self, procedure = False):
    if procedure:
      df = self.frequency_table 
    else:
      df = self.frequency_table.copy()
    df['(xi-X)^2*fi'] = abs(( (df['Xi'] - approach(self.mean())) ** 2) * df['Fi'] )
    
    return df['(xi-X)^2*fi'].sum() / self.n

  def std(self, procedure = False):
    return self.var(procedure) ** 0.5
  
  def cv(self):
    return (self.std() / approach(self.mean())) * 100
  
  def kurtosis_coefficient(self):
    q1 = self.position(1,4)
    q3 = self.position(3,4)
    p10 = self.position(10,100)
    p90 = self.position(90,100)

    kc = (1/2) * ((q3 - q1) / (p90 - p10))
    return kc

  def bowley_coefficient(self):
    q1 = self.position(1,4)
    q2 = self.position(2,4)
    q3 = self.position(3,4)

    bc = (q1 - (2 * q2) + q3) / (q3 - q1)
    return bc