create table twf.stdexp_xfer(
	ID INT NOT NULL AUTO_INCREMENT,
	Record_Type VARCHAR(45) NOT NULL,
	StoreID VARCHAR(45) NOT NULL,
	Date Date NOT NULL,
    XFER_TransferNum INT,
    XFER_TransferRefNum VARCHAR(45),
    XFER_TransferExtRefNum VARCHAR(45),
    XFER_CostCenterSourceName VARCHAR(45),
    XFER_CostCenterSourceNum INT,
    XFER_CostCenterSourceMasterName VARCHAR(45),
    XFER_CostCenterSourceMasterNum INT,
    XFER_CostCenterDestName VARCHAR(45),
    XFER_CostCenterDestNum INT,
    XFER_CostCenterDestMasterName VARCHAR(45),
    XFER_CostCenterDestMasterNum INT,
    XFER_TransferAmount DECIMAL(15,6),
    XFER_TransferStatus INT,
    XFER_TransferDate DATE,      
	PRIMARY KEY(ID)
);