create table twf.stdexp_svc(
	ID INT NOT NULL AUTO_INCREMENT,
	Record_Type VARCHAR(45) NOT NULL,
	StoreID VARCHAR(45) NOT NULL,
	Date Date NOT NULL,
    RVC_num INT,
    SVC_Number INT,
    SVC_Name VARCHAR(45),
    SVC_Total DECIMAL(15,6),
    SVC_Count INT,
    SVC_MasterName VARCHAR(45),
    SVC_MasterNum INT,
    RVC_name VARCHAR(45),
    RVC_MasterName VARCHAR(45),
    RVC_MasterNum INT,
    SVC_Type INT,
	PRIMARY KEY(ID)
);