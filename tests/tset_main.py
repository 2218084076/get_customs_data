from pathlib import Path

import pytest

from get_data.main import read_csv,crop_image

import pandas as pd

import cv2

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

def test_crop_image():
    image_path = './get_data/page.png'
    crop_image(image_path)
    size = cv2.imread('./get_data/1.jpg').shape