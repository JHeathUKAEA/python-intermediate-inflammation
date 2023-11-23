import pytest
from pathlib import Path
import numpy as np
import numpy.testing as npt
from unittest.mock import Mock
import math

def test_analyse_data():
    from inflammation.compute_data import analyse_data, CSVDataSource, JSONDataSource
    path = Path.cwd() / "data"
    #print(path)
    data_holder=CSVDataSource(path)
    #data_holder=JSONDataSource(path)
    result = analyse_data(data_holder)
    print("DBG1", repr(result))
    expected_output = [0.,0.22510286,0.18157299,0.1264423,0.9495481,0.27118211,
                       0.25104719,0.22330897,0.89680503,0.21573875,1.24235548,0.63042094,
                       1.57511696,2.18850242,0.3729574,0.69395538,2.52365162,0.3179312,
                       1.22850657,1.63149639,2.45861227,1.55556052,2.8214853,0.92117578,
                       0.76176979,2.18346188,0.55368435,1.78441632,0.26549221,1.43938417,
                       0.78959769,0.64913879,1.16078544,0.42417995,0.36019114,0.80801707,
                       0.50323031,0.47574665,0.45197398,0.22070227]
    # expected_output = [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
    #                     0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
    #                     0., 0., 0., 0., 0., 0. ]
    # TODO: add an assert for the value of result
    #npt.assert_array_equal(result, [[1, 2, 3], [4, 5, 6]])
    npt.assert_array_almost_equal(result, expected_output,decimal=6)



@pytest.mark.parametrize(
    "test, expected",
    [
        ([[[0, 1, 0], [0, 2, 0]]], [0, 0, 0]),
        ([[[0, 1, 0], [0, 2, 0]], [[0, 1, 0], [0, 2, 0]]], [0, 0, 0]),
        ([[[0.0, 1.0, 0.0], [0.0, 2.0, 0.0]], [[0.0, 1.0, 0.0], [0.0, 2.0, 0.0]]], [0.0, 0.0, 0.0]),
        
    ])
def test_daily_std_dev_calc(test, expected):
    from inflammation.compute_data import daily_std_dev_calc
    print(daily_std_dev_calc(np.array(test)))
    npt.assert_array_equal(daily_std_dev_calc(np.array(test)), np.array(expected))

def test_with_mocks():
    mock_shape1=Mock()
    mock_shape1.get_area().return_value = 10

    mock_shape2=Mock()
    mock_shape2.get_area().return_value = 20

    shapes=[mock_shape1,mock_shape2]
    
    for shape in shapes:
        print(shape.get_area())

def test_compute_data_mock_source():
    from inflammation.compute_data import analyse_data
    data_holder = Mock()
    data_holder.load_data.return_value= [[[0, 2, 0]],
                                                     [[0, 1, 0]]]

  # TODO: configure data_source mock
    result = analyse_data(data_holder)

  # TODO: add assert on the contents of result
    npt.assert_array_equal(result,[0, math.sqrt(0.25) ,0])