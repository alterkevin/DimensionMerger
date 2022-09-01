create table twf.stdexp_cmb(
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
    OT_MasterNumber INT,
    CMB_MainComboItemName VARCHAR(45),
    CMB_MainComboItemNum INT,
    CMB_MainComboItemMasterName VARCHAR(45),
    CMB_MainComboItemMasterNum INT,
    CMB_Component_ItemName VARCHAR(45),
    CMB_Component_ItemNum INT,
    CMB_Component_ItemMasterName VARCHAR(45),
    CMB_Component_ItemMasterNum INT,
    CMB_Original_ItemName VARCHAR(45),
    CMB_Original_itemNum INT,
    CMB_Original_ItemMasterName VARCHAR(45),
    CMB_Original_ItemMasterNum INT,
    CMB_SalesTotal DECIMAL(15,6),
    CMB_SalesCount INT,
    CMB_GrossS_beforediscount DECIMAL(15,6),
    CMB_TotalDscnt DECIMAL(15,6),
    CMB_DscntGrossVat DECIMAL(15,6),
    CMB_GrossS_AfterDscnt DECIMAL(15,6),
    CMB_VAT_beforediscount DECIMAL(15,6),
    CMB_DscntVAT DECIMAL(15,6),
    CMB_VatAfterDscnt DECIMAL(15,6),
    CMB_TotalVat DECIMAL(15,6),
    CMB_NetSales_beforediscount DECIMAL(15,6),
    CMB_DscntNetVat DECIMAL(15,6),
    CMB_NetVatSales DECIMAL(15,6),
	PRIMARY KEY(ID)
);