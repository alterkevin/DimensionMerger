from datetime import datetime,timedelta
import mysql.connector
from mysql.connector import Error
from shutil import move
from glob import glob



path=("\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\Basechan\\Station")
lista=glob(f"{path}\\*.csv")


fecha_actual= datetime.now()
diadelta=timedelta(days=1)

fecha_carpeta_actual=datetime.strftime(fecha_actual,"%b_%Y")
fecha_carpeta_ayer=fecha_actual-diadelta
fecha_carpeta_ayer=datetime.strftime(fecha_carpeta_ayer,"%b_%Y")

fecha_archivo_actual=datetime.strftime(fecha_actual,"%d-%m-%y")
fecha_archivo_ayer=fecha_actual-diadelta
fecha_archivo_ayer=datetime.strftime(fecha_archivo_ayer,"%d-%m-%y")


#EMPTM

for na in lista:
    if na[74:79]=="EMPTM":
        archivo=na[61:83]
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
            INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Basechan/Station/{archivo}' IGNORE
            INTO TABLE twf.stdexp_emptm
            CHARACTER SET UTF8mb4
            FIELDS TERMINATED BY '|'
            LINES TERMINATED BY '\n'
            (
            twf.stdexp_emptm.Record_Type,
            twf.stdexp_emptm.StoreID,
            twf.stdexp_emptm.Date,
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
                print("Carga de datos EMPTM exitosa")


        except Error as ex:
            print(f"error durante la conexion EMPTM: {ex}")

        finally:
            if conexion.is_connected():
                conexion.close()    #Se cerro la conexion a la base de datos
                print("la conexion ha finalizado")


#EMPDSC

    elif na[74:80]=="EMPDSC":
        archivo=na[61:84]
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
            INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Basechan/Station/{archivo}' IGNORE
            INTO TABLE twf.stdexp_empdsc
            CHARACTER SET UTF8mb4
            FIELDS TERMINATED BY '|'
            LINES TERMINATED BY '\n'
            (
            twf.stdexp_empdsc.Record_Type,
            twf.stdexp_empdsc.StoreID,
            twf.stdexp_empdsc.Date,
	        twf.stdexp_empdsc.RVC_name,
            twf.stdexp_empdsc.RVC_num,
            twf.stdexp_empdsc.RVC_MasterName,
            twf.stdexp_empdsc.RVC_MasterNum,
            twf.stdexp_empdsc.EMP_Surname,
            twf.stdexp_empdsc.EMP_Name,
            twf.stdexp_empdsc.EMP_number,
            twf.stdexp_empdsc.DSC_name,
            twf.stdexp_empdsc.DSC_number,
            twf.stdexp_empdsc.DSC_MasterName,
            twf.stdexp_empdsc.DSC_MasterNum,
            twf.stdexp_empdsc.DSC_total,
            twf.stdexp_empdsc.DSC_count,
            twf.stdexp_empdsc.DSC_GrossVat
            )
            SET twf.stdexp_empdsc.ID = NULL;""")
                conexion.commit()
                print("Carga de datos EMPDSC exitosa")


        except Error as ex:
            print(f"error durante la conexion EMPDSC: {ex}")

        finally:
            if conexion.is_connected():
                conexion.close()    #Se cerro la conexion a la base de datos
                print("la conexion ha finalizado")


#EMPOTSLS

    elif na[74:82]=="EMPOTSLS":
        archivo=na[61:86]
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
            INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Basechan/Station/{archivo}' IGNORE
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
            twf.stdexp_empotsls.EMP_surname,
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
                print("Carga de datos EMPOTSLS exitosa")


        except Error as ex:
            print(f"error durante la conexion EMPOTSLS: {ex}")


        finally:
            if conexion.is_connected():
                conexion.close()    #Se cerro la conexion a la base de datos
                print("la conexion ha finalizado")


#FPMI

    elif na[73:77]=="FPMI":
        archivo=na[61:81]
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
            INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Basechan/Station/{archivo}' IGNORE
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
                print("Carga de datos FPMI exitosa")


        except Error as ex:
            print(f"error durante la conexion FPMI: {ex}")


        finally:
            if conexion.is_connected():
                conexion.close()    #Se cerro la conexion a la base de datos
                print("la conexion ha finalizado")



    move(na,"\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\Basechan\\DestinoRevenge")
print("well done boy!")