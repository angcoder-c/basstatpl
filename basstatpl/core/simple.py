import pandas as pd
from math import log
from basstatpl.core.base.calculations import BaseCalcs
from basstatpl.core.util.tools import approach, first_greater_than, max_interval
import matplotlib.pyplot as plt

class SimpleData(BaseCalcs):
  def __init__(self, data = None):
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
    
    df = pd.DataFrame({'Xi':self.source}).groupby('Xi').agg(Fi=('Xi','count'))
    df = df.reset_index()
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
    return self.source.mean()
  
  def median(self):
    return self.source.median()

  def mode(self):
    return self.source.mode()
  
  def mean_deviation(self, procedure = False):
    if procedure:
      df = self.frequency_table 
    else:
      df = self.frequency_table.copy()

    df['Xi-Me'] = abs(df['Xi'] - approach(self.mean()))
    return df['Xi-Me'].sum() / self.n

  def var(self, procedure = False):
    dfi = self.frequency_table.copy()
    dfi['Xi-Me'] = abs(dfi['Xi'] - approach(self.mean()))

    if procedure:
      df = self.frequency_table
    else:
      df = dfi 

    df['(Xi-Me)^2'] = dfi['Xi-Me'] ** 2
    return df['(Xi-Me)^2'].sum() / self.n

  def std(self, procedure = False):
    return self.var(procedure) ** 0.5

  def cv(self):
    return (approach(self.std())/approach(self.mean())) * 100

  def position(self, p, m):
    df = self.frequency_table
    q = (p * self.n) / m
    fg = first_greater_than(df['Fa'], q)
    xi = df['Xi'].iloc[fg[0]]
    return xi

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
      return df.append(df.sum(), ignore_index=True)