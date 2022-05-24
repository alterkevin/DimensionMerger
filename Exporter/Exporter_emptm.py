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
    INFILE 'C:/Users/Administrator/Desktop/DimensionData/Destino/d.standard.merged/{fecha_carpeta_ayer}/EMP_{fecha_archivo_ayer}_EMPTM.csv' IGNORE
    INTO TABLE twf.stdexp_emptm
    CHARACTER SET UTF8mb4
    FIELDS TERMINATED BY '|'
    LINES TERMINATED BY '\n'

   (
	twf.stdexp_emptm.Record_Type,
    twf.stdexp_emptm.StoreID,
    twf.stdexp_emptm.RVC_name,
    twf.stdexp_emptm.RVC_num,
    twf.stdexp_emptm.RVC_MasterName,
    twf.stdexp_emptm.RVC_MasterNum,
    twf.stdexp_emptm.EMP_name,
    twf.stdexp_emptm.EMP_Surname,
    twf.stdexp_emptm.EMP_number,
    twf.stdexp_emptm.TM_name,
    twf.stdexp_emptm.TN_number,
    twf.stdexp_emptm.TM_MasterName,
    twf.stdexp_emptm.TM_MasterNum,
    twf.stdexp_emptm.TM_type,
    twf.stdexp_emptm.TM_total,
    twf.stdexp_emptm.TM_count
	)
	SET twf.stdexp_emptm.ID = NULL;""")
        conexion.commit()
        print("Carga de datos exitosa")



except Error as ex:
    print(f"error durante la conexion: {ex}")



finally:
    if conexion.is_connected():
        conexion.close()    #Se cerro la conexion a la base de datos
        print("la conexion ha finalizado")