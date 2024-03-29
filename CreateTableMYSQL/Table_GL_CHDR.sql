create table twf.stdexp_chdr(
	ID INT NOT NULL AUTO_INCREMENT,
	Record_Type VARCHAR(45) NOT NULL,
	StoreID VARCHAR(45) NOT NULL,
	Date Date NOT NULL,
    RVC_num INT,
    CHDR_OrderType INT,
    CHDR_CheckNumber INT,
    CHDR_OpenDate DATE,
    CHDR_ClosedDate DATE,
    CHDR_OpenDateCheck DATE,
    CHDR_ClosedDateCheck DATE,
    CHDR_Emp VARCHAR(45),
    CHDR_NumGuests INT,
    CHDR_CheckReference VARCHAR(45),
    CHDR_TotalCheck DECIMAL(15,6),
    CHDR_TotalTax DECIMAL(15,6),
    CHDR_TotalExemptTax DECIMAL(15,6),
    CHDR_TotalDayVoid DECIMAL(15,6),
    CHDR_TotalTip DECIMAL(15,6),
    CHDR_ManagerVoidTotal DECIMAL(15,6),
    CHDR_TotalDayReturns DECIMAL(15,6),
    CHDR_ErrorCorrectTotal DECIMAL(15,6),
    CHDR_TransferStatus VARCHAR(45),
    CHDR_TransferCheckNum INT,
    CHDR_TotalDaySrvcChrg DECIMAL(15,6),
    CHDR_TotalDscnt DECIMAL(15,6),
    CHDR_subtotal DECIMAL(15,6),
    RVC_name VARCHAR(45),
    RVC_MasterName VARCHAR(45),
    RVC_MasterNum INT,
    OT_name VARCHAR(45),
    OT_MasterName VARCHAR(45),
    OT_MasterNum INT,
    EMP_name VARCHAR(45),
    EMP_Surname VARCHAR(45),
    CHDR_EventName VARCHAR(45),
    CHDR_EventNum INT,
    CHDR_EventAreaName VARCHAR(45),
    CHDR_EventAreaNum INT,
    CHDR_EventTypeName VARCHAR(45),
    CHDR_EventTypeNum INT,
    CHDR_EventSubtypeName VARCHAR(45),
    CHDR_EventSubtypeNum INT,
    CHDR_LastTransferDate DATE,
    CHDR_MiscellaneousInfo VARCHAR(45),
    CHDR_ReopenFromCheckNum INT,
    CHDR_ReopenToCheckNum INT,
    CHDR_CheckDuration INT,
    CHDR_TableTime INT,
    CHDR_OpenFixPeriod INT,
    CHDR_CloseFixPeriod INT,
    CHDR_GuestCheckNum INT,
    CHDR_TableGroupNum INT,
    CHDR_TableReference VARCHAR(45),
    CHDR_TaxExemptReference VARCHAR(45),
    CHDR_NumberSrvRound INT,
    CHDR_ItemNumbers INT,
    CHDR_Total_InfoLine INT,
    CHDR_TotalCheckPrinted INT,
    CHDR_SrvcChargeExemptTotal DECIMAL(15,6),
    CHDR_OtherTotal DECIMAL(15,6),
    CHDR_AmountDue DECIMAL(15,6),
    CHDR_AutoSrvcChargeTotal DECIMAL(15,6),
    CHDR_ErrorCorrectCount INT,
    CHDR_FiscalKey VARCHAR(45),
    CHDR_CheckInclusiveTax DECIMAL(15,6),
    CHDR_ItemInclusiveTax DECIMAL(15,6),
    CHDR_CashFlag INT,
    CHDR_EmployeeMealFlag INT,
    CHDR_ReopenCloseCheckFlag INT,
    CHDR_CheckSplitFlag INT,
	PRIMARY KEY(ID)
);