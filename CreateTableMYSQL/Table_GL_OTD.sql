create table twf.stdexp_otd(
	ID INT NOT NULL AUTO_INCREMENT,
	Record_Type VARCHAR(45) NOT NULL,
	StoreID VARCHAR(45) NOT NULL,
	Date Date NOT NULL,
    RVC_name VARCHAR(45),
    RVC_num INT,
    RVC_MasterName VARCHAR(45),
    RVC_MasterNum INT,
    OT_name VARCHAR(45),
    OT_number INT,
    OT_MasterName VARCHAR(45),
    OT_MasterNum INT,
    OTD_TotalDayNetSales DECIMAL(15,6),
    OTD_TotalDaySrvcChrg DECIMAL(15,6),
    OTD_TotalDayVoid DECIMAL(15,6),
    OTD_TotalDayVoidCount INT,
    OTD_TotalDayReturns DECIMAL(15,6),
    OTD_CountDayReturns INT,
    OTD_TotalDayTax DECIMAL(15,6),
    OTD_TotalChecks INT,
    OTD_TotalDayGuests INT,
    OTD_TablesTurned INT,
    OTD_TotalDayTables INT,
    OTD_TotalOrderTime INT,
    OTD_ForecastedSls DECIMAL(15,6),
    OTD_PrepCost DECIMAL(15,6),
    OTD_LastYearSls DECIMAL(15,6),
    OTD_LastYearGuest INT,
    OTD_LastYearChecks INT,
    OTD_TableTime INT,
    OTD_ErrorCorrectAmount DECIMAL(15,6),
    OTD_ErrorCorrectCount INT,
    OTD_MngrVoidAmount DECIMAL(15,6),
    OTD_MngrVoidCount INT,
    OTD_CancelAmount DECIMAL(15,6),
    OTD_CancelCount INT,
    OTD_ChecksOpenCount INT,
    OTD_ChecksClosedCount INT,
    OTD_NonRevenueSrvcChrg DECIMAL(15,6),
    OTD_GrossS_beforediscount DECIMAL(15,6),
    OTD_TotalDscnt DECIMAL(15,6),
    OTD_DscntGrossVat DECIMAL(15,6),
    OTD_GrossS_AfterDscnt DECIMAL(15,6),
    OTD_TotalVat DECIMAL(15,6),
    OTD_NetSales DECIMAL(15,6),
    OTD_ForecastedGrossSls DECIMAL(15,6),
    OTD_ForecastedNetSls DECIMAL(15,6),
    OTD_ForecastedTotalDscnt DECIMAL(15,6),
    OTD_ForecastedTotalChecks DECIMAL(15,6),
    OTD_ForecastedTableTurns DECIMAL(15,6),
    OTD_ForecastedAvgCheckAmount DECIMAL(15,6),
    OTD_ForecastedSlsNetVatBeforeDscnt DECIMAL(15,6),
    OTD_ForecastedSlsNetVatAfterDscnt DECIMAL(15,6),
	PRIMARY KEY(ID)
);