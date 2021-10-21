import numpy as np
import pandas as pd
import basstatpl as bst
import pandas._testing as tm

ls = [51,51,51,53,53,53,53,53,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,57,57,57,57,57,57,59]
s = bst.SimpleData(ls)

def test_data():
    tm.assert_series_equal(s.source, pd.Series(ls), check_dtype = False)
    assert s.n == 30
    assert s.minimum == 51
    assert s.maximum == 59

def test_constitution():
    assert s.classes == 5.874500140574885
    assert s.rank == 8
    assert s.interval == 1.3333333333333333
    assert s.amplitude == 1

def test_frequency_table():
    expl = {'Xi': {0: 51, 1: 53, 2: 54, 3: 57, 4: 59}, 
            'Fi': {0: 3, 1: 5, 2: 15, 3: 6, 4: 1}, 
            'Fa': {0: 3, 1: 8, 2: 23, 3: 29, 4: 30}, 
            'Fr': {0: 0.1, 1: 0.16666666666666666, 2: 0.5, 3: 0.2, 4: 0.03333333333333333}, 
            'FrP': {0: 10.0, 1: 16.666666666666664, 2: 50.0, 3: 20.0, 4: 3.3333333333333335}, 
            'FG': {0: 36.0, 1: 60.0, 2: 180.0, 3: 72.0, 4: 12.0}
            }
    df = pd.DataFrame(expl)
    tm.assert_frame_equal(s.frequency_table, df, check_dtype = False)

def test_mean():
    assert s.mean() == 54.3

def test_median():
    assert s.median() == 54.0

def test_mode():
    tm.assert_series_equal(s.mode(), pd.Series([54]), check_dtype = False)

def test_mean_deviation():
    assert s.mean_deviation() == 0.4

def test_var():
    assert s.var() == 1.4666666666666666

def test_std():
    assert s.std() == 1.2110601416389966

def test_position():
    assert s.position(10,100) == 51

def test_cv():
    assert s.cv() == 1.8518518518518516

def test_kurtosis_coefficient():
    assert s.kurtosis_coefficient() == 0.08333333333333333

def test_bowley_coefficient():
    assert s.bowley_coefficient() == -1.0

def test_add_total():
    expl = {'Xi': {0: 51.0, 1: 53.0, 2: 54.0, 3: 57.0, 4: 59.0, 5: 274.0}, 
            'Fi': {0: 3.0, 1: 5.0, 2: 15.0, 3: 6.0, 4: 1.0, 5: 30.0}, 
            'Fa': {0: 3.0, 1: 8.0, 2: 23.0, 3: 29.0, 4: 30.0, 5: 93.0}, 
            'Fr': {0: 0.1, 1: 0.16666666666666666, 2: 0.5, 3: 0.2, 4: 0.03333333333333333, 5: 0.9999999999999999}, 
            'FrP': {0: 10.0, 1: 16.666666666666664, 2: 50.0, 3: 20.0, 4: 3.3333333333333335, 5: 99.99999999999999}, 
            'FG': {0: 36.0, 1: 60.0, 2: 180.0, 3: 72.0, 4: 12.0, 5: 360.0}}

    df = pd.DataFrame(expl)
    tm.assert_frame_equal(s.add_total(), df, check_dtype = False)

dict_num = {51:3, 53:5, 54:15, 57:6, 59:1}
s2 = bst.SimpleData(dict_num)

def test_frequency_table2():
    expl = {'Xi': {0: 51, 1: 53, 2: 54, 3: 57, 4: 59}, 
            'Fi': {0: 3, 1: 5, 2: 15, 3: 6, 4: 1}, 
            'Fa': {0: 3, 1: 8, 2: 23, 3: 29, 4: 30}, 
            'Fr': {0: 0.1, 1: 0.16666666666666666, 2: 0.5, 3: 0.2, 4: 0.03333333333333333}, 
            'FrP': {0: 10.0, 1: 16.666666666666664, 2: 50.0, 3: 20.0, 4: 3.3333333333333335}, 
            'FG': {0: 36.0, 1: 60.0, 2: 180.0, 3: 72.0, 4: 12.0}
            }
    df = pd.DataFrame(expl)
    tm.assert_frame_equal(s2.frequency_table, df, check_dtype = False)

def test_mean2():
    assert s2.mean() == 54.3

def test_median2():
    assert s2.median() == 54.0

def test_mode2():
    tm.assert_series_equal(s2.mode(), pd.Series([54]), check_dtype = False)

def test_mean_deviation2():
    assert s2.mean_deviation() == 0.4

def test_var2():
    assert s2.var() == 1.4666666666666666

def test_std2():
    assert s2.std() == 1.2110601416389966

def test_position2():
    assert s2.position(10,100) == 51

def test_cv2():
    assert s2.cv() == 1.8518518518518516

def test_kurtosis_coefficient2():
    assert s2.kurtosis_coefficient() == 0.08333333333333333

def test_bowley_coefficient2():
    assert s2.bowley_coefficient() == -1.0

def test_add_total():
    expl = {'Xi': {0: 51.0, 1: 53.0, 2: 54.0, 3: 57.0, 4: 59.0, 5: 274.0}, 
            'Fi': {0: 3.0, 1: 5.0, 2: 15.0, 3: 6.0, 4: 1.0, 5: 30.0}, 
            'Fa': {0: 3.0, 1: 8.0, 2: 23.0, 3: 29.0, 4: 30.0, 5: 93.0}, 
            'Fr': {0: 0.1, 1: 0.16666666666666666, 2: 0.5, 3: 0.2, 4: 0.03333333333333333, 5: 0.9999999999999999}, 
            'FrP': {0: 10.0, 1: 16.666666666666664, 2: 50.0, 3: 20.0, 4: 3.3333333333333335, 5: 99.99999999999999}, 
            'FG': {0: 36.0, 1: 60.0, 2: 180.0, 3: 72.0, 4: 12.0, 5: 360.0}}

    df = pd.DataFrame(expl)
    tm.assert_frame_equal(s2.add_total(), df, check_dtype = False)