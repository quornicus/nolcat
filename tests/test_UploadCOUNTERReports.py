"""Test using `UploadCOUNTERReports`."""

import io
import os
from pathlib import Path
import pytest
from wtforms import MultipleFileField
from wtforms.validators import DataRequired
from pandas.testing import assert_frame_equal

# `conftest.py` fixtures are imported automatically
from nolcat.upload_COUNTER_reports import UploadCOUNTERReports
from data import COUNTER_reports


#Section: Fixtures
@pytest.fixture
def sample_COUNTER_report_workbooks():
    """Creates a Flask-WTF MultipleFileField object containing all of the Excel workbooks in `\\nolcat\\tests\\bin\\COUNTER_workbooks_for_tests`."""
    folder_path = Path('tests', 'bin', 'COUNTER_workbooks_for_tests')
    data_attribute = []

    for workbook in os.listdir(folder_path):
        file_path = folder_path / workbook
        with open(file_path, mode='rb') as file:
            data_attribute.append(io.BytesIO(file.read()))

    fixture = MultipleFileField({
        'data': data_attribute,
        'id': 'COUNTER_reports',
        'label': "Select the COUNTER report workbooks. If all the files are in a single folder and that folder contains no other items, navigate to that folder, then use `Ctrl + a` to select all the files in the folder.",
        'name': 'COUNTER_reports',
        'type': 'MultipleFileField',
        'validators': DataRequired(),
    })
    return fixture


@pytest.fixture
def sample_COUNTER_reports():
    """Creates a dataframe with the data from all the COUNTER reports."""
    yield COUNTER_reports.sample_COUNTER_reports()


#Section: Tests
def test_create_dataframe(sample_COUNTER_report_workbooks, sample_COUNTER_reports):
    """Tests transforming multiple Excel workbooks with tabular COUNTER data into a single dataframe ready for the RawCOUNTERReport class."""
    df = UploadCOUNTERReports(sample_COUNTER_report_workbooks).create_dataframe()  #ALERT: `RuntimeError: Working outside of request context.` upon running test
    assert assert_frame_equal(df, sample_COUNTER_reports)