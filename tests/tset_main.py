import json

from pathlib import Path

import pandas as pd
import pytest

from get_data.main import read_csv, save_json, main


@pytest.fixture(name='mock_source_file')
def fixture_mock_source_file(mock_path) -> Path:
    """ """
    a = [90214000, 90219011]
    dataframe = pd.DataFrame({'id': a})
    source_file = mock_path / 'test_file.csv'
    dataframe.to_csv('%s/test_file.csv' % mock_path, index=False, sep=',')
    yield source_file


def test_read_csv(mock_source_file):
    """Test read csv file"""
    result = read_csv(mock_source_file)
    assert result == [90214000, 90219011]


def test_save_json(mock_path):
    """test save json file"""
    dest_file = mock_path / 'result_data_json.json'
    tmp_json = [
        {
            "id": "10011900",
            "product_name": "其他硬粒小麦",
            "first_q": "601",
            "first_n": "澳大利亚",
            "second_q": "10",
            "second_n": "一般贸易",
            "rmb": "51"
        }
    ]
    save_json(tmp_json, dest_file)
    with open(dest_file, 'r', encoding='utf-8') as obj:
        j = json.load(obj)
        assert '10011900' in j[0].get('id')


def test_main(mock, mock_path, mock_source_file):
    """test main"""
    mock_read_csv = mock.patch(
        'get_data.main.read_csv',
    )
    mock_save_json = mock.patch(
        'get_data.main.save_json',
    )
    dest_file = mock_path / 'result_data_json.json'
    main(str(mock_source_file), '2021', '1', '12', dest_file)
    mock_read_csv.assert_called_once_with(mock_source_file)
    mock_save_json.assert_called_once_with(dest_file)
