"""This module outputs the test data used in the relations as CSVs. By running this module to create a CSV file, committing the file, and pushing the commit to GitHub, these file can be downloaded to a local machine for further manipulation in a spreadsheet program, like Excel."""

import os
from pathlib import Path
import pyinputplus as pyip
import pandas as pd

from data import relations
from data import COUNTER_reports
from data import deduplication_data

relation_name = pyip.inputMenu(
    prompt="Enter the number of the test data dataframe that should be output to a CSV.\n",
    choices=[
        "fiscalYears_relation",
        "vendors_relation",
        "vendorNotes_relation",
        "statisticsSources_relation",
        "statisticsSourceNotes_relation",
        "resourceSources_relation",
        "resourceSourceNotes_relation",
        "statisticsResourceSources_relation",
        "annualUsageCollectionTracking_relation",
        "resources_relation",
        "resourceMetadata_relation",
        "resourcePlatforms_relation",
        "usageData_relation",
        "sample_COUNTER_reports",
        "sample_normalized_resource_data",
        "matched_records",
        "matches_to_manually_confirm",
        "matched_records_including_sample_normalized_resource_data",
        "matches_to_manually_confirm_including_sample_normalized_resource_data",
    ],
    numbered=True,
)

if relation_name == "fiscalYears_relation":
    relation_data = relations.fiscalYears_relation()
elif relation_name == "vendors_relation":
    relation_data = relations.vendors_relation()
elif relation_name == "vendorNotes_relation":
    relation_data = relations.vendorNotes_relation()
elif relation_name == "statisticsSources_relation":
    relation_data = relations.statisticsSources_relation()
elif relation_name == "statisticsSourceNotes_relation":
    relation_data = relations.statisticsSourceNotes_relation()
elif relation_name == "resourceSources_relation":
    relation_data = relations.resourceSources_relation()
elif relation_name == "resourceSourceNotes_relation":
    relation_data = relations.resourceSourceNotes_relation()
elif relation_name == "statisticsResourceSources_relation":
    relation_data = relations.statisticsResourceSources_relation()
elif relation_name == "annualUsageCollectionTracking_relation":
    relation_data = relations.annualUsageCollectionTracking_relation()
elif relation_name == "resources_relation":
    relation_data = relations.resources_relation()
elif relation_name == "resourceMetadata_relation":
    relation_data = relations.resourceMetadata_relation()
elif relation_name == "resourcePlatforms_relation":
    relation_data = relations.resourcePlatforms_relation()
elif relation_name == "usageData_relation":
    relation_data = relations.usageData_relation()
elif relation_name == "sample_COUNTER_reports":
    relation_data = COUNTER_reports.sample_COUNTER_reports()
elif relation_name == "sample_normalized_resource_data":
    relation_data = deduplication_data.sample_normalized_resource_data()
elif relation_name == "matched_records":
    relation_data = deduplication_data.matched_records()
elif relation_name == "matches_to_manually_confirm":
    relation_data = deduplication_data.matches_to_manually_confirm()
elif relation_name == "matched_records_including_sample_normalized_resource_data":
    relation_data = deduplication_data.matched_records_including_sample_normalized_resource_data()
elif relation_name == "matches_to_manually_confirm_including_sample_normalized_resource_data":
    relation_data = deduplication_data.matches_to_manually_confirm_including_sample_normalized_resource_data()

# Ideally, this module can run in the container in the AWS instance, but an inability to authenticate from that command line to GitHub makes running the module on the local machine the only way to access the CSVs on the local machine. This module is thus set up to determine if it's running in the AWS instance or on a local machine and create a `pathlib.Path` object for the absolute path of the file based on the environment and folder the module is run from.
file_name = Path('/', 'nolcat', 'tests', 'data')
if file_name.exists():
    file_name = file_name / f'{relation_name}.csv'
else:
    file_name_start_elements = os.getcwd().split('nolcat')[0].split('\\')
    file_name_start = Path(file_name_start_elements[0], '/')
    for element in file_name_start_elements[1:-1]:  # This removes the drive letter from the beginning and the empty string from the end
        file_name_start = file_name_start / element
    file_name = file_name_start / 'nolcat' / 'tests' / 'data' / f'{relation_name}.csv'

file = relation_data.to_csv(
    file_name,
    encoding='utf-8',  # Previously, this was `utf-16` because when saving Excel files as TSVs retaining non-Latin alphabet characters, the TSVs defaulted to UTF-16
    # `None` values in dataframes meet Excel's `isblank` criteria in TSVs, so `na_rep=` argument left as default
    # Dates are ISO-formatted strings when opened in text editors and date data types when opened in Excel, so `date_format=` argument left as default
)