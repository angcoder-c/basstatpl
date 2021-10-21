from math import log
import pandas as pd
from basstatpl.core.base.calculations import BaseCalcs
from basstatpl.core.util.tools import approach, first_greater_than, max_interval
import matplotlib.pyplot as plt

class GroupedData(BaseCalcs):
  def __init__(self, data=None):
    BaseCalcs.__init__(self, data)

    if str(type(data)) == "<class 'list'>":
      self.source = pd.Series(data)

    elif str(type(data)) == "<class 'dict'>":
          x = list(data.keys())
          f = list(data.values())
          r = range(len(data))
          
          if str(type(x[0])) == "<class 'int'>" or str(type(x[0])) == "<class 'float'>":
                nx = "".join([(str(x[i]) + ' ') * f[i] for i in r]).split()
                self.source = pd.Series(list(map(int, nx)))  

          elif str(type(x[0])) == "<class 'tuple'>":
                self.source = pd.Series(data)
                intervals = [pd.Interval(i[0], i[1], closed='left') for i in x]
                freq = f
    
    if str(type(self.source.index[0])) == "<class 'int'>":
      intervals = pd.interval_range(start= self.minimum,
                                  end= max_interval(self)[1],
                                  freq= self.amplitude,
                                  closed="left")
      dist = [list(filter(lambda x: x in i, self.source)) for i in intervals]
      freq = [len(j) for j in dist]   

    df = pd.DataFrame({'Lr':list(intervals)})
    df['La_float'] = [pd.Interval(i.left - 0.5, i.right - 0.5, closed = 'both')
                      for i in df['Lr']]
    df['La'] = [pd.Interval(i.left, i.right - 1, closed = 'both')
                for i in df['Lr']]                    
    df['Xi'] = [(i.left + i.right)/2 for i in df['La']]
    df['Fi'] = freq
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

  def add_total(self):
    df = self.frequency_table.copy()
    types = [[i, str(df[i].dtype)] for i in df.columns.to_list()]
    col = []
    for i in types:
      if i[1] == 'int64' or i[1] == 'float64':
        col.append(i[0])
    f = col[0]
    t = col[-1]
    df.loc[len(df), f:t] = df.loc[:, f:t].sum()
    return df