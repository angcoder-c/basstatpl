import numpy as np
import pandas as pd
import pandas._testing as tm
import basstatpl as bst

ls = [51,51,53,53,53,53,53,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,57,57,57,57,57,57,59]
a = bst.analysis(ls)

def test_frequency_table():
    expl = {'Xi': {0: 51, 1: 53, 2: 54, 3: 57, 4: 59}, 
            'Fi': {0: 2, 1: 5, 2: 15, 3: 6, 4: 1}, 
            'Fa': {0: 2, 1: 7, 2: 22, 3: 28, 4: 29}, 
            'Fr': {0: 0.06896551724137931, 1: 0.1724137931034483, 2: 0.5172413793103449, 3: 0.20689655172413793, 4: 0.034482758620689655}, 
            'FrP': {0: 6.896551724137931, 1: 17.24137931034483, 2: 51.724137931034484, 3: 20.689655172413794, 4: 3.4482758620689653}, 
            'FG': {0: 24.82758620689655, 1: 62.06896551724138, 2: 186.20689655172416, 3: 74.48275862068965, 4: 12.413793103448276}}

    df = pd.DataFrame(expl)
    tm.assert_frame_equal(a.frequency_table, df, check_dtype = False)

dict_num = {51:2, 53:5, 54:15, 57:6, 59:1}
a2 = bst.analysis(dict_num)

def test_frequency_table2():
    expl = {'Xi': {0: 51, 1: 53, 2: 54, 3: 57, 4: 59}, 
            'Fi': {0: 2, 1: 5, 2: 15, 3: 6, 4: 1}, 
            'Fa': {0: 2, 1: 7, 2: 22, 3: 28, 4: 29}, 
            'Fr': {0: 0.06896551724137931, 1: 0.1724137931034483, 2: 0.5172413793103449, 3: 0.20689655172413793, 4: 0.034482758620689655}, 
            'FrP': {0: 6.896551724137931, 1: 17.24137931034483, 2: 51.724137931034484, 3: 20.689655172413794, 4: 3.4482758620689653}, 
            'FG': {0: 24.82758620689655, 1: 62.06896551724138, 2: 186.20689655172416, 3: 74.48275862068965, 4: 12.413793103448276}}
    df = pd.DataFrame(expl)
    tm.assert_frame_equal(a2.frequency_table, df, check_dtype = False)

dct_tup = {(15.0, 18.0):1,(18.0,21.0):4,(21.0,24.0):7,(24.0,27.0):8,(27.0,30.0):6,(30.0,33.0):4}
a3 = bst.analysis(dct_tup)

def test_frequency_table2():
    df = pd.DataFrame({'Lr': {0: pd.Interval(15.0, 18.0, closed='left'), 
                   1: pd.Interval(18.0, 21.0, closed='left'),
                   2: pd.Interval(21.0, 24.0, closed='left'),
                   3: pd.Interval(24.0, 27.0, closed='left'),
                   4: pd.Interval(27.0, 30.0, closed='left'),
                   5: pd.Interval(30.0, 33.0, closed='left')},

            'La_float': {0: pd.Interval(14.5, 17.5, closed='both'),
                         1: pd.Interval(17.5, 20.5, closed='both'),
                         2: pd.Interval(20.5, 23.5, closed='both'),
                         3: pd.Interval(23.5, 26.5, closed='both'),
                         4: pd.Interval(26.5, 29.5, closed='both'),
                         5: pd.Interval(29.5, 32.5, closed='both')},

            'La': {0: pd.Interval(15.0, 17.0, closed='both'),
                   1: pd.Interval(18.0, 20.0, closed='both'),
                   2: pd.Interval(21.0, 23.0, closed='both'),
                   3: pd.Interval(24.0, 26.0, closed='both'),
                   4: pd.Interval(27.0, 29.0, closed='both'),
                   5: pd.Interval(30.0, 32.0, closed='both')},

            'Xi': {0: 16.0, 1: 19.0,
                   2: 22.0, 3: 25.0,
                   4: 28.0, 5: 31.0},

            'Fi': {0: 1, 1: 4, 
                   2: 7, 3: 8,
                   4: 6, 5: 4},

            'Fa': {0: 1, 1: 5,
                   2: 12, 3: 20,
                   4: 26, 5: 30},

            'Fr': {0: 0.03333333333333333, 1: 0.13333333333333333,
                   2: 0.23333333333333334, 3: 0.26666666666666666,
                   4: 0.2, 5: 0.13333333333333333},

            'FrP': {0: 3.3333333333333335, 1: 13.333333333333334,
                    2: 23.333333333333332, 3: 26.666666666666668, 
                    4: 20.0, 5: 13.333333333333334},

            'FG': {0: 12.0, 1: 48.0, 
                   2: 84.0, 3: 96.0, 
                   4: 72.0, 5: 48.0}})
    tm.assert_frame_equal(a3.frequency_table, df, check_dtype = False)

dct_num2 = {15:1,18:2,19:1,20:1,22:3,23:4,24:4,25:3,26:1,27:3,28:1,29:2,30:4}
a3 = bst.GroupedData(dct_num2)

def test_frequency_table3():
    df = pd.DataFrame({'Lr': {0: pd.Interval(15.0, 18.0, closed='left'), 
                   1: pd.Interval(18.0, 21.0, closed='left'),
                   2: pd.Interval(21.0, 24.0, closed='left'),
                   3: pd.Interval(24.0, 27.0, closed='left'),
                   4: pd.Interval(27.0, 30.0, closed='left'),
                   5: pd.Interval(30.0, 33.0, closed='left')},

            'La_float': {0: pd.Interval(14.5, 17.5, closed='both'),
                         1: pd.Interval(17.5, 20.5, closed='both'),
                         2: pd.Interval(20.5, 23.5, closed='both'),
                         3: pd.Interval(23.5, 26.5, closed='both'),
                         4: pd.Interval(26.5, 29.5, closed='both'),
                         5: pd.Interval(29.5, 32.5, closed='both')},

            'La': {0: pd.Interval(15.0, 17.0, closed='both'),
                   1: pd.Interval(18.0, 20.0, closed='both'),
                   2: pd.Interval(21.0, 23.0, closed='both'),
                   3: pd.Interval(24.0, 26.0, closed='both'),
                   4: pd.Interval(27.0, 29.0, closed='both'),
                   5: pd.Interval(30.0, 32.0, closed='both')},

            'Xi': {0: 16.0, 1: 19.0,
                   2: 22.0, 3: 25.0,
                   4: 28.0, 5: 31.0},

            'Fi': {0: 1, 1: 4, 
                   2: 7, 3: 8,
                   4: 6, 5: 4},

            'Fa': {0: 1, 1: 5,
                   2: 12, 3: 20,
                   4: 26, 5: 30},

            'Fr': {0: 0.03333333333333333, 1: 0.13333333333333333,
                   2: 0.23333333333333334, 3: 0.26666666666666666,
                   4: 0.2, 5: 0.13333333333333333},

            'FrP': {0: 3.3333333333333335, 1: 13.333333333333334,
                    2: 23.333333333333332, 3: 26.666666666666668, 
                    4: 20.0, 5: 13.333333333333334},

            'FG': {0: 12.0, 1: 48.0, 
                   2: 84.0, 3: 96.0, 
                   4: 72.0, 5: 48.0}})
    tm.assert_frame_equal(a3.frequency_table, df, check_dtype = False)