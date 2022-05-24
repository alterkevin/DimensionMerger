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
	INFILE 'C:/Users/Administrator/Desktop/DimensionData/Destino/d.standard.merged/{fecha_carpeta_ayer}/EMP_{fecha_archivo_ayer}_EMPOTSLS.csv' IGNORE
    INTO TABLE twf.stdexp_empotsls
    CHARACTER SET UTF8mb4
    FIELDS TERMINATED BY '|'
    LINES TERMINATED BY '\n'

   (
	twf.stdexp_empotsls.Record_Type,
    twf.stdexp_empotsls.StoreID,
    twf.stdexp_empotsls.Date,
    twf.stdexp_empotsls.RVC_name,
    twf.stdexp_empotsls.RVC_num,
    twf.stdexp_empotsls.RVC_MasterName,
    twf.stdexp_empotsls.RVC_MasterNum,
    twf.stdexp_empotsls.EMP_name,
    twf.stdexp_empotsls.EMP_Surname,
    twf.stdexp_empotsls.EMP_number,
    twf.stdexp_empotsls.OT_name,
    twf.stdexp_empotsls.OT_number,
    twf.stdexp_empotsls.OT_MasterName,
    twf.stdexp_empotsls.OT_MasterNum,
    twf.stdexp_empotsls.OT_TotalDayTransactions,
    twf.stdexp_empotsls.OT_TotalDayGuests,
    twf.stdexp_empotsls.OT_TablesTurned,
    twf.stdexp_empotsls.OT_TotalDayTables,
    twf.stdexp_empotsls.OT_TotalDayNetSales,
    twf.stdexp_empotsls.OT_TotalDaySrvcChrg,
    twf.stdexp_empotsls.OT_TotalDayVoid,
    twf.stdexp_empotsls.OT_TotalDayVoidCount,
    twf.stdexp_empotsls.OT_TotalDayReturns,
    twf.stdexp_empotsls.OT_TotalDayReturnCount,
    twf.stdexp_empotsls.OT_TotalDayTax,
    twf.stdexp_empotsls.OT_Credit,
    twf.stdexp_empotsls.OT_TableTime,
    twf.stdexp_empotsls.OT_ErrorCorrectAmount,
    twf.stdexp_empotsls.OT_ErrorCorrectCount,
    twf.stdexp_empotsls.OT_MngrVoidAmount,
    twf.stdexp_empotsls.OT_MngrVoidCount,
    twf.stdexp_empotsls.OT_CancelAmount,
    twf.stdexp_empotsls.OT_CancelCount,
    twf.stdexp_empotsls.OT_ChecksOpenAmount,
    twf.stdexp_empotsls.OT_ChecksOpenCount,
    twf.stdexp_empotsls.OT_ChecksClosedAmount,
    twf.stdexp_empotsls.OT_ChecksClosedCount,
    twf.stdexp_empotsls.OT_ChecksTransferInAmount,
    twf.stdexp_empotsls.OT_ChecksTransferInCount,
    twf.stdexp_empotsls.OT_ChecksTransferOutAmount,
    twf.stdexp_empotsls.OT_ChecksTransferOutCount,
    twf.stdexp_empotsls.OT_NonRevenueSrvcChrg,
    twf.stdexp_empotsls.OT_DscTotal,
    twf.stdexp_empotsls.OT_GrossS
	)
	SET twf.stdexp_empotsls.ID = NULL;""")
        conexion.commit()
        print("Carga de datos exitosa")



except Error as ex:
    print(f"error durante la conexion: {ex}")



finally:
    if conexion.is_connected():
        conexion.close()    #Se cerro la conexion a la base de datos
        print("la conexion ha finalizado")