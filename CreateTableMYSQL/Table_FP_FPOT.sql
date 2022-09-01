create table twf.stdexp_fpot(
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
    OT_TotalDayNetSales DECIMAL(15,6),
    OT_TotalDaySrvcChrg DECIMAL(15,6),
    OT_TotalDayVoid DECIMAL(15,6),
    OT_TotalDayVoidCount INT,
    OT_TotalDayReturns DECIMAL(15,6),
    OT_CountDayReturns INT,
    OT_TotalDayTax DECIMAL(15,6),
    OT_TotalChecks INT,
    OT_TotalGuests INT,
    OT_TablesTurned INT,
    OT_TotalDayTables INT,
    OT_TotalOrderTime INT,
    OT_ForecastedSls DECIMAL(15,6),
    OT_PrepCost DECIMAL(15,6),
    OT_LastYearSls DECIMAL(15,6),
    OT_LastYearGuests INT,
    OT_LastYearChecks INT,
    OT_TableTime INT,
    OT_ErrorCorrectAmount DECIMAL(15,6),
    OT_ErrorCorrectCount INT,
    OT_MngrVoidAmount DECIMAL(15,6),
    OT_MngrVoidCount INT,
    OT_CancelAmount DECIMAL(15,6),
    OT_CancelCount INT,
    OT_ChecksOpenAmount DECIMAL(15,6),
    OT_ChecksOpenCount INT,
    OT_ChecksClosedAmount DECIMAL(15,6),
    OT_ChecksClosedCount INT,
    OT_ChecksTransferInAmount DECIMAL(15,6),
    OT_ChecksTransferInCount INT,
    OT_ChecksTransferOutAmount DECIMAL(15,6),
    OT_ChecksTransferOutCount INT,
    OT_NonRevenueSrvcChrg DECIMAL(15,6),
    OT_Credit DECIMAL(15,6),
    OT_BusinessHour INT,
    OT_FixedPeriod INT,
    OT_GrossS_beforediscount DECIMAL(15,6),
    OT_TotalDscnt DECIMAL(15,6),
    OT_GrossVatDscnt DECIMAL(15,6),
    OT_TotalVat DECIMAL(15,6),
    OT_NetSlsVat DECIMAL(15,6),
    OT_ForecastedGrossSls DECIMAL(15,6),
    OT_ForecastedNetSls DECIMAL(15,6),
    OT_ForecastedTotalDscnt DECIMAL(15,6),
    OT_ForecastedTotalChecks DECIMAL(15,6),
    OT_ForecastedTotalTableTurns DECIMAL(15,6),
    OT_ForecastedAvgTotalChecks DECIMAL(15,6),
    OT_ForecastedSlsNetVatBeforeDscnt DECIMAL(15,6),
    OT_ForecastedSlsNetVatAfterDscnt DECIMAL(15,6),
	PRIMARY KEY(ID)
);