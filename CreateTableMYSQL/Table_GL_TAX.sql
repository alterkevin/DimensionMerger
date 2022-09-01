create table twf.stdexp_tax(
	ID INT NOT NULL AUTO_INCREMENT,
	Record_Type VARCHAR(45) NOT NULL,
	StoreID VARCHAR(45) NOT NULL,
	Date Date NOT NULL,
	RVC_num int,
    TAX_number int,
    TAX_name VARCHAR(45),
	TAX_Rate decimal(15,6),
    TAX_TotalDay decimal(15,6),
    TAX_TaxableSls decimal(15,6),
    TAX_ExemptSls decimal(15,6),
    TAX_MasterName VARCHAR(45),
    TAX_MasterNum INT,
    RVC_name VARCHAR(45),
	RVC_MasterName VARCHAR(45),
	RVC_MasterNum int,
    TAX_Type int,
    TAX_RateVat decimal(15,6),
    TAX_GrossS decimal(15,6),
    TAX_NetSales decimal(15,6),
    TAX_TotalPrcnt decimal(15,6),
    TAX_TotalTaxableSls decimal(15,6),
    TAX_TotalTaxableSlsVat decimal(15,6),
    TAX_VatAfterDscnt decimal(15,6),
    TAX_SlsNetVatAfterDscnt decimal(15,6),
	PRIMARY KEY(ID)
);