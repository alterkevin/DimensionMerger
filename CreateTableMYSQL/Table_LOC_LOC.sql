create table twf.stdexp_loc(
	ID INT NOT NULL AUTO_INCREMENT,
	Record_Type VARCHAR(45) NOT NULL,
	StoreLvl VARCHAR(45) NOT NULL,
	Date Date NOT NULL,
    LOC_Name VARCHAR(45),
    LOC_ID VARCHAR(45),
    Organization_Lvl VARCHAR(45),
    Source VARCHAR(45),
    Open_Date DATE,
    Timezone VARCHAR(45),
    Currency VARCHAR(45),
    Date_Current DATE,
    Date_Before DATE,
	PRIMARY KEY(ID)
);
