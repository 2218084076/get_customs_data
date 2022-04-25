from pathlib import Path

import pytest

# from get_data.main import read_csv, mouse_action, mark_edge, crop_image

import pandas as pd


@pytest.fixture(name='mock_source_file')
def fixture_mock_source_file(mock_path) -> Path:
    """ """
    a = [90214000, 90219011]
    dataframe = pd.DataFrame({'id': a})
    source_file = mock_path / 'test_file.csv'
    dataframe.to_csv('%s/test_file.csv' % mock_path, index=False, sep=',')
    yield source_file

