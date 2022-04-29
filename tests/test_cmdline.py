"""Test cmdline"""
import sys

import pytest

from get_data.cmdline import main


@pytest.mark.parametrize(
    '_help, csv_file_path, year, start_month, end_month, dest_file, raise_value, count_called',
    [
        ('-h', '', '', '', '', '', 0, False),
        ('', 'f', '', '', '', '', 2, False),
        ('', '', '2021', '', '', '', 2, False),
        ('', '', '', '1', '', '', 2, False),
        ('', '', '', '', '3', '', 2, False),
        ('', '', '', '', '', 'b', 2, False),
        ('', 'f', 2021, 1, 3, 'b', None, True),  # Normal argument.

    ]
)
def test_main(mocker, _help, csv_file_path, year, start_month, end_month, dest_file, raise_value, count_called):
    """Test main"""
    args = ['program']
    if _help:
        args.append(_help)
    if csv_file_path:
        args.extend(['-f', csv_file_path])
    if year:
        args.extend(['-y', year])
    if start_month:
        args.extend(['-s', start_month])
    if end_month:
        args.extend(['-e', end_month])
    if dest_file:
        args.extend(['-d', dest_file])

    mocker.patch.object(sys, 'argv', args)
    mock_count = mocker.patch('get_data.cmdline.main')

    if raise_value is not None:
        # If use -h, will raise SystemExit(0)
        # If some require argument miss, exit code > 0
        with pytest.raises(SystemExit) as ex:
            main()
        assert ex.value.code == raise_value
    else:
        # Normal exc
        main()
        assert mock_count.called == count_called
