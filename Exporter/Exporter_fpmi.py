import mysql.connector
from datetime import datetime,timedelta
from mysql.connector import Error



fecha_actual= datetime.now()
diadelta=timedelta(days=1)

fecha_carpeta_actual=datetime.strftime(fecha_actual,"%B_%Y")
fecha_carpeta_ayer=fecha_actual-diadelta
fecha_carpeta_ayer=datetime.strftime(fecha_carpeta_ayer,"%B_%Y")

fecha_archivo_actual=datetime.strftime(fecha_actual,"%d-%m-%y")
fecha_archivo_ayer=fecha_actual-diadelta
fecha_archivo_ayer=datetime.strftime(fecha_archivo_ayer,"%d-%m-%y")



try:
    conexion = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="mymicros2205",
        database="twf"
    )
    if conexion.is_connected():
        print("conexion exitosa")
        cursor=conexion.cursor()
        cursor.execute(f"""LOAD DATA 
    INFILE 'C:/Users/Administrator/Desktop/DimensionData/Destino/d.standard.merged/{fecha_carpeta_ayer}/FP_{fecha_archivo_ayer}_FPMI.csv' IGNORE
    INTO TABLE twf.stdexp_fpmi
    CHARACTER SET UTF8mb4
    FIELDS TERMINATED BY '|'
    LINES TERMINATED BY '\n'

   (
	twf.stdexp_fpmi.Record_Type,
    twf.stdexp_fpmi.StoreID,
    twf.stdexp_fpmi.Date,
    twf.stdexp_fpmi.RVC_name,
    twf.stdexp_fpmi.RVC_num,
    twf.stdexp_fpmi.RVC_MasterName,
    twf.stdexp_fpmi.RVC_MasterNum,
    twf.stdexp_fpmi.MI_name1,
    twf.stdexp_fpmi.MI_name2,
    twf.stdexp_fpmi.MI_number,
    twf.stdexp_fpmi.MI_MasterName1,
    twf.stdexp_fpmi.MI_MasterName2,
    twf.stdexp_fpmi.MI_MasterNumber,
    twf.stdexp_fpmi.MI_majorgroup_name,
    twf.stdexp_fpmi.MI_majorgroup_number,
    twf.stdexp_fpmi.MI_MasterMajorgroup_name,
    twf.stdexp_fpmi.MI_Master_majorgroup_number,
    twf.stdexp_fpmi.MI_familygroup_name,
    twf.stdexp_fpmi.MI_familygroup_num,
    twf.stdexp_fpmi.MI_Master_familygroup_name,
    twf.stdexp_fpmi.MI_Master_familygroup_num,
    twf.stdexp_fpmi.OT_name,
    twf.stdexp_fpmi.OT_num,
    twf.stdexp_fpmi.OT_Master_name,
    twf.stdexp_fpmi.OT_Master_num,
    twf.stdexp_fpmi.TRTN_GrossS_beforediscount,
    twf.stdexp_fpmi.DSC_total,
    twf.stdexp_fpmi.TRTN_GrossS,
    twf.stdexp_fpmi.TRTN_VAT_beforediscount,
    twf.stdexp_fpmi.DSC_VAT,
    twf.stdexp_fpmi.TRTN_VAT,
    twf.stdexp_fpmi.TRTN_NetSales_beforediscount,
    twf.stdexp_fpmi.DSC_netVAT,
    twf.stdexp_fpmi.TRTN_NetSales,
    twf.stdexp_fpmi.MI_pricelevel,
    twf.stdexp_fpmi.TRTN_SalesTotal,
    twf.stdexp_fpmi.TRTN_SalesCount,
    twf.stdexp_fpmi.TRTN_ReturnCount,
    twf.stdexp_fpmi.TRTN_volume,
    twf.stdexp_fpmi.TRTN_VAT_total,
    twf.stdexp_fpmi.TRTN_PrepCost,
    twf.stdexp_fpmi.TRTN_FixedPeriod,
    twf.stdexp_fpmi.TRTN_Hour
	)
	SET twf.stdexp_fpmi.ID = NULL;""")
        conexion.commit()
        print("Carga de datos exitosa")



except Error as ex:
    print(f"error durante la conexion: {ex}")



finally:
    if conexion.is_connected():
        conexion.close()    #Se cerro la conexion a la base de datos
        print("la conexion ha finalizado")