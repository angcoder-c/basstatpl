from typing import Dict
import pandas as pd
import basstatpl as bst
import pandas._testing as tm

ls = [27,23,22,24,24,30,25,23,22,15,18,18,29,28,27,27,23,19,26,30,25,29,24,30,20,23,24,30,22,25]
g = bst.GroupedData(ls)

def test_data():
    assert g.source == ls
    assert g.n == 30
    assert g.minimum == 15
    assert g.maximum == 30

def test_constitution():
    assert g.sturges_rule == 5.874500140574885
    assert g.rank == 15
    assert g.interval == 2.5
    assert g.amplitude == 3

def test_frequency_table():
    expl = {'Lr': {0: pd.Interval(15.0, 18.0, closed='left'), 
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
                   4: 72.0, 5: 48.0}}
    df = pd.DataFrame(expl)
    tm.assert_frame_equal(g.frequency_table, df, check_dtype = False)

def test_mean():
    assert g.mean() == 24.6

def test_median():
    assert g.median() == 24.625

def test_mode():
    assert g.mode() == 24.5

def test_position():
    assert g.position(3, 4) == 27.75

def test_var():
    assert g.var() == 16.2

def test_std():
    assert g.std() == 4.024922359499621

def test_cv():
    assert g.cv() == 16.099689437998485

def test_kurtosis_coefficient():
    assert g.kurtosis_coefficient() == 0.2746031746031745

def test_bowley_coefficient():
    assert g.bowley_coefficient() == 0.011560693641618746