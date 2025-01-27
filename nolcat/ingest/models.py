"""These classes represent all the relations used only in the `ingest` blueprint."""

from sqlalchemy import Column
from sqlalchemy import Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from nolcat.models import Base


class FiscalYears(Base):
    """A relation representing the fiscal years for which data has been collected."""
    __tablename__ = 'fiscalYears'
    __table_args__ = {'schema': 'nolcat'}

    fiscal_year_id = Column()  #ToDo: INT PRIMARY KEY AUTO_INCREMENT NOT NULL
    fiscal_year = Column()  #ToDo: CHAR(4) NOT NULL
    start_date = Column()  #ToDo: DATE NOT NULL
    end_date = Column()  #ToDo: DATE NOT NULL
    acrl_60b = Column()  #ToDo: SMALLINT
    acrl_63 = Column()  #ToDo: SMALLINT
    arl_18 = Column()  #ToDo: SMALLINT
    arl_19 = Column()  #ToDo: SMALLINT
    arl_20 = Column()  #ToDo: SMALLINT
    notes_on_corrections_after_submission = Column()  #ToDo: TEXT


    def __repr__(self):
        #ToDo: Create an f-string to serve as a printable representation of the record
        pass


    def calculate_ACRL_60b():
        pass


    def calculate_ACRL_63():
        pass


    def calculate_ARL_18():
        pass

    
    def calculate_ARL_19():
        pass


    def calculate_ARL_20():
        pass


    def create_usage_tracking_records_for_fiscal_year():
        #ToDo: For every stats source that doesn't have deactivation date earlier than FY start date, create a record in annual usage collection tracking relation with this FY and the stats source as the composite key
        pass


    def collect_fiscal_year_usage_statistics(self):
        """A method invoking the RawCOUNTERReport constructor for all of a fiscal year's usage.

        A helper method encapsulating `_harvest_R5_SUSHI` to change its return value from a dataframe to a RawCOUNTERReport object.

        Returns:
            RawCOUNTERReport: a RawCOUNTERReport object for all the usage for the given fiscal year
        """
        #ToDo: dfs = []
        #ToDo: For every AnnualUsageCollectionTracking object with the given FY where usage_is_being_collected=True and manual_collection_required=False
            #ToDo: statistics_source = Get the matching StatisticsSources object
            #ToDo: df = statistics_source._harvest_R5_SUSHI(self.start_date, self.end_date)
            #ToDo: dfs.append(df)
        #ToDo: df = pd.concat(dfs)
        #ToDo: return RawCOUNTERReport(df)
        pass


class Vendors(Base):
    """A relation representing resource providers."""
    __tablename__ = 'vendors'
    __table_args__ = {'schema': 'nolcat'}

    vendor_id = Column()  #ToDo: INT PRIMARY KEY AUTO_INCREMENT NOT NULL
    vendor_name = Column()  #ToDo: VARCHAR(80) NOT NULL
    alma_vendor_code = Column()  #ToDo: VARCHAR(10)


    def __repr__(self):
        #ToDo: Create an f-string to serve as a printable representation of the record
        pass


    def get_SUSHI_credentials_from_Alma():
        pass


    def get_SUSHI_credentials_from_JSON():
        pass


class VendorNotes(Base):
    """A relation containing notes about vendors."""
    __tablename__ = 'vendorNotes'
    __table_args__ = {'schema': 'nolcat'}

    vendor_notes_id = Column()  #ToDo: INT PRIMARY KEY AUTO_INCREMENT NOT NULL
    note = Column()  #ToDo: TEXT
    written_by = Column()  #ToDo: VARCHAR(100)
    date_written = Column()  #ToDo: TIMESTAMP
    vendor_id = Column(ForeignKey('nolcat.Vendors.vendor_id'))  #ToDo: INT NOT NULL

    vendors_FK_vendorNotes = relationship('Vendors', backref='vendor_id')


    def __repr__(self):
        #ToDo: Create an f-string to serve as a printable representation of the record
        pass


class StatisticsSources(Base):
    """A relation containing information about sources of usage statistics."""
    __tablename__ = 'statisticsSources'
    __table_args__ = {'schema': 'nolcat'}

    statistics_source_id = Column()  #ToDo: INT PRIMARY KEY AUTO_INCREMENT NOT NULL
    statistics_source_name = Column()  #ToDo: VARCHAR(100) NOT NULL
    statistics_source_retrieval_code = Column()  #ToDo: VARCHAR(30)
    current_access = Column()  #ToDo: BOOLEAN NOT NULL
    access_stop_date = Column()  #ToDo: TIMESTAMP
    vendor_id = Column(ForeignKey('nolcat.Vendors.vendor_id'))  #ToDo: INT NOT NULL

    vendors_FK_statisticsSources = relationship('Vendors', backref='vendor_id')


    def __repr__(self):
        #ToDo: Create an f-string to serve as a printable representation of the record
        pass


    def show_SUSHI_credentials():
        #ToDo: Need a way to display SUSHI base URL and parameters (requestor ID, customer ID, API key, platform)--is a method for the record class the best way to do it?
        pass


    def _harvest_R5_SUSHI(self, usage_start_date, usage_end_date):
        """Collects the COUNTER R5 reports for the given statistics source and loads it into the database.

        For a given statistics source and date range, this method uses SUSHI to harvest all available COUNTER R5 reports at their most granular level, then combines them in a RawCOUNTERReport object for loading into the database. This is a private method meant to be called by other methods which will provide additional context at the method call and wrap the result in the RawCOUNTERReport class.

        Args:
            usage_start_date (datetime.date): the first day of the usage collection date range, which is the first day of the month 
            usage_end_date (datetime.date): the last day of the usage collection date range, which is the last day of the month
        
        Returns:
            dataframe: a dataframe containing all of the R5 COUNTER data
        """
        #Section: Get API Call URL and Parameters
        #ToDo: Determine if info for API calls is coming from the Alma API or a file saved in a secure location
        #ToDo: Using self.statistics_source_retrieval_code, create dict SUSHI_info with the following key-value pairs:
            #ToDo: URL=the URL for the API call
            #ToDo: customer_ID=the customer ID
            #ToDo: requestor_ID=the requestor ID, if an API call parameter
            #ToDo: API_key=the API key, if an API call parameter
            #ToDo: SUSHI_platform=the platform parameter value, if part of the API call
        #ToDo: SUSHI_parameters = {key: value for key, value in SUSHI_info.items() if key != "URL"}


        #Section: Confirm SUSHI API Functionality
        #ToDo: SUSHICallAndResponse(SUSHI_info['URL'], "status", SUSHI_parameters)
        #ToDo: Figure out methods and return values for above class


        #Section: Get List of Resources
        #Subsection: Make API Call
        #ToDo: SUSHICallAndResponse(SUSHI_info['URL'], "reports", SUSHI_parameters)
        #ToDo: Figure out methods and return values for above class so the ultimate result is all_available_reports = a list of all available reports

        #Subsection: Get List of Master Reports
        #ToDo: available_reports = [report for report in all_available_reports if report not matching regex /\w{2}_\w{2}/]
        #ToDo: available_master_reports = [master_report for master_report in available_reports if "_" not in master_report]

        #Subsection: Add Any Standard Reports Not Corresponding to a Master Report
        #ToDo: represented_by_master_report = set()
        #ToDo: for master_report in available_master_reports:
            #ToDo: for report in available_reports:
                #ToDo: if report[0:2] == master_report:
                    #ToDo: Add report to represented_by_master_report
        #ToDo: not_represented_by_master_report = [report for report in available_reports if report not in represented_by_master_report]
        #ToDo: Figure out inspecting to see if pulling usage from reports in not_represented_by_master_report is appropriate


        #Section: Make Master Report SUSHI Calls
        #Subsection: Add Date Parameters
        #ToDo: SUSHI_parameters['begin_date'] = usage_start_date
        #toDo: SUSHI_parameters['end_date'] = usage_end_date

        #Subsection: Set Up Loop Through Master Reports
        #ToDo: master_report_dataframes = []
        #ToDo: for master_report in available_master_reports:
            #ToDo: master_report_name = master_report short name in uppercase letters

            #Subsection: Check if Usage Is Already in Database
            #ToDo: for month in <the range of months the usage time span represents>
                #ToDo: Get number of records in usage data relation with self.statistics_source_id, the month, and master_report
                #ToDo: If the above returns data
                    #ToDo: Ask if data should be loaded
            #ToDo: If any months shouldn't be loaded, check if the date range is still contiguous; if not, figure out a way to make call as many times as necessary to call for all dates that need to be pulled

            #Subsection: Add Parameters for Master Report Type
            #ToDo: if master_report_name == "PR":
                #ToDo: SUSHI_parameters["attributes_to_show"] = "Data_Type|Access_Method"
                #ToDo: try:
                    #ToDo: del SUSHI_parameters["include_parent_details"]
                    #ToDo: del SUSHI_parameters["include_component_details"]
            #ToDo: if master_report_name == "DR":
                #ToDo: SUSHI_parameters["attributes_to_show"] = "Data_Type|Access_Method"
                    #ToDo: try:
                        #ToDo: del SUSHI_parameters["include_parent_details"]
                        #ToDo: del SUSHI_parameters["include_component_details"]
            #ToDo: if master_report_name == "TR":
                #ToDo: SUSHI_parameters["attributes_to_show"] = "Data_Type|Access_Method|YOP|Access_Type|Section_Type"
                #ToDo: try:
                    #ToDo: del SUSHI_parameters["include_parent_details"]
                    #ToDo: del SUSHI_parameters["include_component_details"]
            #ToDo: if master_report_name == "IR":
                #ToDo: SUSHI_parameters["attributes_to_show"] = "Data_Type|Access_Method|YOP|Access_Type"
                #ToDo: SUSHI_parameters["include_parent_details"] = "True"
                #ToDo: SUSHI_parameters["include_component_details"] = "True"
            
            #Subsection: Make Master Report API Call
            #ToDo: SUSHICallAndResponse(SUSHI_info['URL'], f"reports/{master_report_name.lower()}", SUSHI_parameters)
            #ToDo: Figure out methods and return values for above class
            #ToDo: Ultimately need a dataframe for master_report_dataframes.append()
        

        #Section: Return a Single Dataframe
        #ToDo: return pd.concat(master_report_dataframes)
        pass


    def collect_usage_statistics(self, usage_start_date, usage_end_date):
        """A method invoking the RawCOUNTERReport constructor for usage in the specified time range.

        A helper method encapsulating `_harvest_R5_SUSHI` to change its return value from a dataframe to a RawCOUNTERReport object.

        Args:
            usage_start_date (datetime.date): the first day of the usage collection date range, which is the first day of the month 
            usage_end_date (datetime.date): the last day of the usage collection date range, which is the last day of the month
        
        Returns:
            RawCOUNTERReport: a RawCOUNTERReport object for all the usage from the given statistics source in the given date range
        """
        #ToDo: a dataframe of all the reports = self._harvest_R5_SUSHI(usage_start_date, usage_end_date)
        #ToDo: return RawCOUNTERReport(above dataframe)
        pass


    def add_access_stop_date():
        #ToDo: Put value in access_stop_date when current_access goes from True to False
        pass


    def remove_access_stop_date():
        #ToDo: Null value in access_stop_date when current_access goes from False to True
        pass


class AnnualUsageCollectionTracking():
    """A relation for tracking the usage statistics collection process. """
    __tablename__ = 'annualUsageCollectionTracking'
    __table_args__ = {'schema': 'nolcat'}

    auct_statistics_source = Column(ForeignKey('nolcat.StatisticsSources.statistics_source_id'))  #ToDo: INT NOT NULL
    auct_fiscal_year = Column(ForeignKey('nolcat.FiscalYears.fiscal_year_id'))  #ToDo: INT NOT NULL
    usage_is_being_collected = Column()  #ToDo: BOOLEAN NOT NULL
    manual_collection_required = Column()  #ToDo: BOOLEAN
    collection_via_email = Column()  #ToDo: BOOLEAN
    is_counter_compliant = Column()  #ToDo: BOOLEAN
    collection_status = Column()  #ToDo: ENUM(
        #'N/A: Paid by Law',
        #'N/A: Paid by Med',
        #'N/A: Paid by Music',
        #'N/A: Open access',
        #'N/A: Other (see notes)',
        #'Collection not started',
        #'Collection in process (see notes)',
        #'Collection issues requiring resolution',
        #'Collection complete',
        #'Usage not provided',
        #'No usage to report'
    usage_file_path = Column()  #ToDo: VARCHAR(150)
    notes = Column()  #ToDo: TEXT

    statisticsSources_FK_annualUsageCollectionTracking = relationship('StatisticsSources', backref='statistics_source_id')
    fiscalYears_FK_annualUsageCollectionTracking = relationship('FiscalYears', backref='fiscal_year_id')


    def __repr__(self):
        #ToDo: Create an f-string to serve as a printable representation of the record
        pass


    def collect_annual_usage_statistics(self):
        """A method invoking the RawCOUNTERReport constructor for the given resource's fiscal year usage.

        A helper method encapsulating `_harvest_R5_SUSHI` to change its return value from a dataframe to a RawCOUNTERReport object.

        Returns:
            RawCOUNTERReport: a RawCOUNTERReport object for all the usage from the given statistics source in the given fiscal year
        """
        #ToDo: start_date = start date for FY
        #ToDo: end_date = end date for FY
        #ToDo: statistics_source = StatisticSources object for self.auct_statistics_source value
        #ToDo: df = statistics_source._harvest_R5_SUSHI(start_date, end_date)
        #ToDo: Change `collection_status` to "Collection complete"
        #ToDo: return RawCOUNTERReport(df)
        pass


    def upload_nonstandard_usage_file():
        pass