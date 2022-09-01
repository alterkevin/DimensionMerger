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
        move(na,f"\\Users\\Administrator\\Desktop\\DimensionData\\Destination\\{fecha_carpeta_ayer}\\")


#EMP

    elif na[74:81]=="EMP.csv":
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
            INTO TABLE twf.stdexp_emp
            CHARACTER SET UTF8mb4
            FIELDS TERMINATED BY '|'
            LINES TERMINATED BY '\n'
            (
            twf.stdexp_emp.Record_Type,
            twf.stdexp_emp.StoreID,
            twf.stdexp_emp.Date,
            twf.stdexp_emp.RVC_name,
            twf.stdexp_emp.RVC_num,
            twf.stdexp_emp.RVC_MasterName,
            twf.stdexp_emp.RVC_MasterNum,
            twf.stdexp_emp.EMP_Name,
            twf.stdexp_emp.EMP_Surname,
            twf.stdexp_emp.EMP_number,
            twf.stdexp_emp.EMP_TotalDayTransactions,
            twf.stdexp_emp.EMP_TotalDayGuests,
            twf.stdexp_emp.EMP_TablesTurned,
            twf.stdexp_emp.EMP_TableTime,
            twf.stdexp_emp.EMP_TotalDayNetSales,
            twf.stdexp_emp.EMP_TotalDaySrvcChrg,
            twf.stdexp_emp.EMP_TotalDayVoid,
            twf.stdexp_emp.EMP_TotalDayVoidCount,
            twf.stdexp_emp.EMP_TotalDayReturns,
            twf.stdexp_emp.EMP_TotalDayReturnCount,
            twf.stdexp_emp.EMP_Credit,
            twf.stdexp_emp.EMP_Round,
            twf.stdexp_emp.EMP_ErrorCorrectAmount,
            twf.stdexp_emp.EMP_ErrorCorrectCount,
            twf.stdexp_emp.EMP_MngrVoidAmount,
            twf.stdexp_emp.EMP_MngrVoidCount,
            twf.stdexp_emp.EMP_CancelAmount,
            twf.stdexp_emp.EMP_CancelCount,
            twf.stdexp_emp.EMP_ChecksOpenAmount,
            twf.stdexp_emp.EMP_ChecksOpenCount,
            twf.stdexp_emp.EMP_ChecksClosedAmount,
            twf.stdexp_emp.EMP_ChecksClosedCount,
            twf.stdexp_emp.EMP_ChecksTransferInAmount,
            twf.stdexp_emp.EMP_ChecksTransferInCount,
            twf.stdexp_emp.EMP_ChecksTransferOutAmount,
            twf.stdexp_emp.EMP_ChecksTransferOutCount,
            twf.stdexp_emp.EMP_NonRevenueSrvcChrg,
            twf.stdexp_emp.EMP_TipTotal,
            twf.stdexp_emp.EMP_Cary_Over_Total,
            twf.stdexp_emp.EMP_Cary_Over_Count,
            twf.stdexp_emp.EMP_GrossS_beforediscount,
            twf.stdexp_emp.EMP_DSC_total,
            twf.stdexp_emp.EMP_DSC_GrossVat,
            twf.stdexp_emp.EMP_GrossS
            )
            SET twf.stdexp_emp.ID = NULL;""")
                conexion.commit()
                print("Carga de datos EMP exitosa")


        except Error as ex:
            print(f"error durante la conexion EMP: {ex}")

        finally:
            if conexion.is_connected():
                conexion.close()    #Se cerro la conexion a la base de datos
                print("la conexion ha finalizado")
        move(na,f"\\Users\\Administrator\\Desktop\\DimensionData\\Destination\\{fecha_carpeta_ayer}\\")


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
        move(na,f"\\Users\\Administrator\\Desktop\\DimensionData\\Destination\\{fecha_carpeta_ayer}\\")


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
        move(na,f"\\Users\\Administrator\\Desktop\\DimensionData\\Destination\\{fecha_carpeta_ayer}\\")


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
        move(na,f"\\Users\\Administrator\\Desktop\\DimensionData\\Destination\\{fecha_carpeta_ayer}\\")


#FPOT

    elif na[73:77]=="FPOT":
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
            INTO TABLE twf.stdexp_fpot
            CHARACTER SET UTF8mb4
            FIELDS TERMINATED BY '|'
            LINES TERMINATED BY '\n'
            (
            twf.stdexp_fpot.Record_Type,
            twf.stdexp_fpot.StoreID,
            twf.stdexp_fpot.Date,
            twf.stdexp_fpot.RVC_name,
            twf.stdexp_fpot.RVC_num,
            twf.stdexp_fpot.RVC_MasterName,
            twf.stdexp_fpot.RVC_MasterNum,
            twf.stdexp_fpot.OT_name,
            twf.stdexp_fpot.OT_number,
            twf.stdexp_fpot.OT_MasterName,
            twf.stdexp_fpot.OT_MasterNum,
            twf.stdexp_fpot.OT_TotalDayNetSales,
            twf.stdexp_fpot.OT_TotalDaySrvcChrg,
            twf.stdexp_fpot.OT_TotalDayVoid,
            twf.stdexp_fpot.OT_TotalDayVoidCount,
            twf.stdexp_fpot.OT_TotalDayReturns,
            twf.stdexp_fpot.OT_CountDayReturns,
            twf.stdexp_fpot.OT_TotalDayTax,
            twf.stdexp_fpot.OT_TotalChecks,
            twf.stdexp_fpot.OT_TotalGuests,
            twf.stdexp_fpot.OT_TablesTurned,
            twf.stdexp_fpot.OT_TotalDayTables,
            twf.stdexp_fpot.OT_TotalOrderTime,
            twf.stdexp_fpot.OT_ForecastedSls,
            twf.stdexp_fpot.OT_PrepCost,
            twf.stdexp_fpot.OT_LastYearSls,
            twf.stdexp_fpot.OT_LastYearGuests,
            twf.stdexp_fpot.OT_LastYearChecks,
            twf.stdexp_fpot.OT_TableTime,
            twf.stdexp_fpot.OT_ErrorCorrectAmount,
            twf.stdexp_fpot.OT_ErrorCorrectCount,
            twf.stdexp_fpot.OT_MngrVoidAmount,
            twf.stdexp_fpot.OT_MngrVoidCount,
            twf.stdexp_fpot.OT_CancelAmount,
            twf.stdexp_fpot.OT_CancelCount,
            twf.stdexp_fpot.OT_ChecksOpenAmount,
            twf.stdexp_fpot.OT_ChecksOpenCount,
            twf.stdexp_fpot.OT_ChecksClosedAmount,
            twf.stdexp_fpot.OT_ChecksClosedCount,
            twf.stdexp_fpot.OT_ChecksTransferInAmount,
            twf.stdexp_fpot.OT_ChecksTransferInCount,
            twf.stdexp_fpot.OT_ChecksTransferOutAmount,
            twf.stdexp_fpot.OT_ChecksTransferOutCount,
            twf.stdexp_fpot.OT_NonRevenueSrvcChrg,
            twf.stdexp_fpot.OT_Credit,
            twf.stdexp_fpot.OT_BusinessHour,
            twf.stdexp_fpot.OT_FixedPeriod,
            twf.stdexp_fpot.OT_GrossS_beforediscount,
            twf.stdexp_fpot.OT_TotalDscnt,
            twf.stdexp_fpot.OT_GrossVatDscnt,
            twf.stdexp_fpot.OT_TotalVat,
            twf.stdexp_fpot.OT_NetSlsVat,
            twf.stdexp_fpot.OT_ForecastedGrossSls,
            twf.stdexp_fpot.OT_ForecastedNetSls,
            twf.stdexp_fpot.OT_ForecastedTotalDscnt,
            twf.stdexp_fpot.OT_ForecastedTotalChecks,
            twf.stdexp_fpot.OT_ForecastedTotalTableTurns,
            twf.stdexp_fpot.OT_ForecastedAvgTotalChecks,
            twf.stdexp_fpot.OT_ForecastedSlsNetVatBeforeDscnt,
            twf.stdexp_fpot.OT_ForecastedSlsNetVatAfterDscnt
            )
            SET twf.stdexp_fpot.ID = NULL;""")
                conexion.commit()
                print("Carga de datos FPOT exitosa")


        except Error as ex:
            print(f"error durante la conexion FPOT: {ex}")


        finally:
            if conexion.is_connected():
                conexion.close()    #Se cerro la conexion a la base de datos
                print("la conexion ha finalizado")
        move(na,f"\\Users\\Administrator\\Desktop\\DimensionData\\Destination\\{fecha_carpeta_ayer}\\")


#FPSUM

    elif na[73:78]=="FPSUM":
        archivo=na[61:82]
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
            INTO TABLE twf.stdexp_fpsum
            CHARACTER SET UTF8mb4
            FIELDS TERMINATED BY '|'
            LINES TERMINATED BY '\n'
            (
            twf.stdexp_fpsum.Record_Type,
            twf.stdexp_fpsum.StoreID,
            twf.stdexp_fpsum.Date,
            twf.stdexp_fpsum.RVC_name,
            twf.stdexp_fpsum.RVC_num,
            twf.stdexp_fpsum.RVC_MasterName,
            twf.stdexp_fpsum.RVC_MasterNum,
            twf.stdexp_fpsum.SUM_TotalDayNetSales,
            twf.stdexp_fpsum.SUM_TotalDaySrvcChrg,
            twf.stdexp_fpsum.SUM_TotalDayVoid,
            twf.stdexp_fpsum.SUM_TotalDayVoidCount,
            twf.stdexp_fpsum.SUM_TotalDayReturns,
            twf.stdexp_fpsum.SUM_CountDayReturns,
            twf.stdexp_fpsum.SUM_TotalDayTax,
            twf.stdexp_fpsum.SUM_TotalDayTransactions,
            twf.stdexp_fpsum.SUM_TotalDayGuests,
            twf.stdexp_fpsum.SUM_TablesTurned,
            twf.stdexp_fpsum.SUM_TotalDayTables,
            twf.stdexp_fpsum.SUM_TotalOrderTime,
            twf.stdexp_fpsum.SUM_ForecastedSls,
            twf.stdexp_fpsum.SUM_PrepCost,
            twf.stdexp_fpsum.SUM_LastYearSls,
            twf.stdexp_fpsum.SUM_LastYearGuests,
            twf.stdexp_fpsum.SUM_LastYearChecks,
            twf.stdexp_fpsum.SUM_TableTime,
            twf.stdexp_fpsum.SUM_ErrorCorrectTotal,
            twf.stdexp_fpsum.SUM_ErrorCorrectCount,
            twf.stdexp_fpsum.SUM_MngrVoidAmount,
            twf.stdexp_fpsum.SUM_MngrVoidCount,
            twf.stdexp_fpsum.SUM_CancelAmount,
            twf.stdexp_fpsum.SUM_CancelCount,
            twf.stdexp_fpsum.SUM_ChecksOpenAmount,
            twf.stdexp_fpsum.SUM_ChecksOpenCount,
            twf.stdexp_fpsum.SUM_ChecksClosedAmount,
            twf.stdexp_fpsum.SUM_ChecksClosedCount,
            twf.stdexp_fpsum.SUM_ChecksTransferInAmount,
            twf.stdexp_fpsum.SUM_ChecksTransferInCount,
            twf.stdexp_fpsum.SUM_ChecksTransferOutAmount,
            twf.stdexp_fpsum.SUM_ChecksTransferOutCount,
            twf.stdexp_fpsum.SUM_NonRevenueSrvcChrg,
            twf.stdexp_fpsum.SUM_Credit,
            twf.stdexp_fpsum.SUM_Hour,
            twf.stdexp_fpsum.SUM_FixedPeriod,
            twf.stdexp_fpsum.SUM_GrossS_beforediscount,
            twf.stdexp_fpsum.SUM_TotalDscnt,
            twf.stdexp_fpsum.SUM_DscntGrossVat,
            twf.stdexp_fpsum.SUM_VAT_total,
            twf.stdexp_fpsum.SUM_NetSales,
            twf.stdexp_fpsum.SUM_ForecastedGrossSls,
            twf.stdexp_fpsum.SUM_ForecastedNetSls,
            twf.stdexp_fpsum.SUM_ForecastedTotalDscnt,
            twf.stdexp_fpsum.SUM_ForecastedTotalChecks,
            twf.stdexp_fpsum.SUM_ForecastedTableTurns,
            twf.stdexp_fpsum.SUM_ForecastedAvgTotalChecks,
            twf.stdexp_fpsum.SUM_ForecastedSlsNetVatBeforeDscnt,
            twf.stdexp_fpsum.SUM_ForecastedSlsNetVatAfterDscnt
            )
            SET twf.stdexp_fpsum.ID = NULL;""")
                conexion.commit()
                print("Carga de datos FPSUM exitosa")


        except Error as ex:
            print(f"error durante la conexion FPSUM: {ex}")


        finally:
            if conexion.is_connected():
                conexion.close()    #Se cerro la conexion a la base de datos
                print("la conexion ha finalizado")
        move(na,f"\\Users\\Administrator\\Desktop\\DimensionData\\Destination\\{fecha_carpeta_ayer}\\")


#DSC

    elif na[73:76]=="DSC":
        archivo=na[61:80]
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
            INTO TABLE twf.stdexp_dsc
            CHARACTER SET UTF8mb4
            FIELDS TERMINATED BY '|'
            LINES TERMINATED BY '\n'
            (
            twf.stdexp_dsc.Record_Type,
            twf.stdexp_dsc.StoreID,
            twf.stdexp_dsc.Date,
            twf.stdexp_dsc.RVC_num,
            twf.stdexp_dsc.DSC_number,
            twf.stdexp_dsc.DSC_name,
            twf.stdexp_dsc.DSC_Total,
            twf.stdexp_dsc.DSC_Count,
            twf.stdexp_dsc.DSC_MasterName,
            twf.stdexp_dsc.DSC_MasterNum,
            twf.stdexp_dsc.RVC_name,
            twf.stdexp_dsc.RVC_MasterName,
            twf.stdexp_dsc.RVC_MasterNum,
            twf.stdexp_dsc.DSC_GrossVat
            )
            SET twf.stdexp_dsc.ID = NULL;""")
                conexion.commit()
                print("Carga de datos DSC exitosa")


        except Error as ex:
            print(f"error durante la conexion DSC: {ex}")


        finally:
            if conexion.is_connected():
                conexion.close()    #Se cerro la conexion a la base de datos
                print("la conexion ha finalizado")
        move(na,f"\\Users\\Administrator\\Desktop\\DimensionData\\Destination\\{fecha_carpeta_ayer}\\")


#TND

    elif na[73:76]=="TND":
        archivo=na[61:80]
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
            INTO TABLE twf.stdexp_tnd
            CHARACTER SET UTF8mb4
            FIELDS TERMINATED BY '|'
            LINES TERMINATED BY '\n'
            (
            twf.stdexp_tnd.Record_Type,
            twf.stdexp_tnd.StoreID,
            twf.stdexp_tnd.Date,
            twf.stdexp_tnd.RVC_num,
            twf.stdexp_tnd.TND_number,
            twf.stdexp_tnd.TND_name,
            twf.stdexp_tnd.TND_Type,
            twf.stdexp_tnd.TND_Total,
            twf.stdexp_tnd.TND_Count,
            twf.stdexp_tnd.TND_MasterName,
            twf.stdexp_tnd.TND_MasterNum,
            twf.stdexp_tnd.RVC_name,
            twf.stdexp_tnd.RVC_MasterName,
            twf.stdexp_tnd.RVC_MasterNum
            )
            SET twf.stdexp_tnd.ID = NULL;""")
                conexion.commit()
                print("Carga de datos TND exitosa")


        except Error as ex:
            print(f"error durante la conexion TND: {ex}")


        finally:
            if conexion.is_connected():
                conexion.close()    #Se cerro la conexion a la base de datos
                print("la conexion ha finalizado")
        move(na,f"\\Users\\Administrator\\Desktop\\DimensionData\\Destination\\{fecha_carpeta_ayer}\\")


#NONSLS

    elif na[73:79]=="NONSLS":
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
            INTO TABLE twf.stdexp_nonsls
            CHARACTER SET UTF8mb4
            FIELDS TERMINATED BY '|'
            LINES TERMINATED BY '\n'
            (
            twf.stdexp_nonsls.Record_Type,
            twf.stdexp_nonsls.StoreID,
            twf.stdexp_nonsls.Date,
            twf.stdexp_nonsls.RVC_name,
            twf.stdexp_nonsls.RVC_num,
            twf.stdexp_nonsls.RVC_MasterName,
            twf.stdexp_nonsls.RVC_MasterNum,
            twf.stdexp_nonsls.EMP_name,
            twf.stdexp_nonsls.EMP_Surname,
            twf.stdexp_nonsls.EMP_number,
            twf.stdexp_nonsls.EMP_ShiftNumber,
            twf.stdexp_nonsls.NON_WorkstationName,
            twf.stdexp_nonsls.NON_WorkstationNum,
            twf.stdexp_nonsls.NON_ReasonCodeName,
            twf.stdexp_nonsls.NON_ReasonCodeNum,
            twf.stdexp_nonsls.NON_ReasonCodeMasterName,
            twf.stdexp_nonsls.NON_ReasonCodeMasterNum,
            twf.stdexp_nonsls.NON_CashierName,
            twf.stdexp_nonsls.NON_CashierNum,
            twf.stdexp_nonsls.NON_CashierMasterName,
            twf.stdexp_nonsls.NON_CashierMasterNum,
            twf.stdexp_nonsls.NON_CashierShiftNum,
            twf.stdexp_nonsls.NON_CashierDrawerNum,
            twf.stdexp_nonsls.NON_TransactionDate,
            twf.stdexp_nonsls.NON_FixedPeriod,
            twf.stdexp_nonsls.NON_SlsType,
            twf.stdexp_nonsls.NON_Reference,
            twf.stdexp_nonsls.NON_TotalAmount,
            twf.stdexp_nonsls.NON_TotalCount,
            twf.stdexp_nonsls.NON_TotalCancelCount,
            twf.stdexp_nonsls.NON_TotalCancel
            )
            SET twf.stdexp_nonsls.ID = NULL;""")
                conexion.commit()
                print("Carga de datos NONSLS exitosa")


        except Error as ex:
            print(f"error durante la conexion NONSLS: {ex}")


        finally:
            if conexion.is_connected():
                conexion.close()    #Se cerro la conexion a la base de datos
                print("la conexion ha finalizado")
        move(na,f"\\Users\\Administrator\\Desktop\\DimensionData\\Destination\\{fecha_carpeta_ayer}\\")


#CHDR

    elif na[73:77]=="CHDR":
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
            INTO TABLE twf.stdexp_chdr
            CHARACTER SET UTF8mb4
            FIELDS TERMINATED BY '|'
            LINES TERMINATED BY '\n'
            (
            twf.stdexp_chdr.Record_Type,
            twf.stdexp_chdr.StoreID,
            twf.stdexp_chdr.Date,
            twf.stdexp_chdr.RVC_num,
            twf.stdexp_chdr.CHDR_OrderType,
            twf.stdexp_chdr.CHDR_CheckNumber,
            twf.stdexp_chdr.CHDR_OpenDate,
            twf.stdexp_chdr.CHDR_ClosedDate,
            twf.stdexp_chdr.CHDR_OpenDateCheck,
            twf.stdexp_chdr.CHDR_ClosedDateCheck,
            twf.stdexp_chdr.CHDR_Emp,
            twf.stdexp_chdr.CHDR_NumGuests,
            twf.stdexp_chdr.CHDR_CheckReference,
            twf.stdexp_chdr.CHDR_TotalCheck,
            twf.stdexp_chdr.CHDR_TotalTax,
            twf.stdexp_chdr.CHDR_TotalExemptTax,
            twf.stdexp_chdr.CHDR_TotalDayVoid,
            twf.stdexp_chdr.CHDR_TotalTip,
            twf.stdexp_chdr.CHDR_ManagerVoidTotal,
            twf.stdexp_chdr.CHDR_TotalDayReturns,
            twf.stdexp_chdr.CHDR_ErrorCorrectTotal,
            twf.stdexp_chdr.CHDR_TransferStatus,
            twf.stdexp_chdr.CHDR_TransferCheckNum,
            twf.stdexp_chdr.CHDR_TotalDaySrvcChrg,
            twf.stdexp_chdr.CHDR_TotalDscnt,
            twf.stdexp_chdr.CHDR_subtotal,
            twf.stdexp_chdr.RVC_name,
            twf.stdexp_chdr.RVC_MasterName,
            twf.stdexp_chdr.RVC_MasterNum,
            twf.stdexp_chdr.OT_name,
            twf.stdexp_chdr.OT_MasterName,
            twf.stdexp_chdr.OT_MasterNum,
            twf.stdexp_chdr.EMP_name,
            twf.stdexp_chdr.EMP_Surname,
            twf.stdexp_chdr.CHDR_EventName,
            twf.stdexp_chdr.CHDR_EventNum,
            twf.stdexp_chdr.CHDR_EventAreaName,
            twf.stdexp_chdr.CHDR_EventAreaNum,
            twf.stdexp_chdr.CHDR_EventTypeName,
            twf.stdexp_chdr.CHDR_EventTypeNum,
            twf.stdexp_chdr.CHDR_EventSubtypeName,
            twf.stdexp_chdr.CHDR_EventSubtypeNum,
            twf.stdexp_chdr.CHDR_LastTransferDate,
            twf.stdexp_chdr.CHDR_MiscellaneousInfo,
            twf.stdexp_chdr.CHDR_ReopenFromCheckNum,
            twf.stdexp_chdr.CHDR_ReopenToCheckNum,
            twf.stdexp_chdr.CHDR_CheckDuration,
            twf.stdexp_chdr.CHDR_TableTime,
            twf.stdexp_chdr.CHDR_OpenFixPeriod,
            twf.stdexp_chdr.CHDR_CloseFixPeriod,
            twf.stdexp_chdr.CHDR_GuestCheckNum,
            twf.stdexp_chdr.CHDR_TableGroupNum,
            twf.stdexp_chdr.CHDR_TableReference,
            twf.stdexp_chdr.CHDR_TaxExemptReference,
            twf.stdexp_chdr.CHDR_NumberSrvRound,
            twf.stdexp_chdr.CHDR_ItemNumbers,
            twf.stdexp_chdr.CHDR_Total_InfoLine,
            twf.stdexp_chdr.CHDR_TotalCheckPrinted,
            twf.stdexp_chdr.CHDR_SrvcChargeExemptTotal,
            twf.stdexp_chdr.CHDR_OtherTotal,
            twf.stdexp_chdr.CHDR_AmountDue,
            twf.stdexp_chdr.CHDR_AutoSrvcChargeTotal,
            twf.stdexp_chdr.CHDR_ErrorCorrectCount,
            twf.stdexp_chdr.CHDR_FiscalKey,
            twf.stdexp_chdr.CHDR_CheckInclusiveTax,
            twf.stdexp_chdr.CHDR_ItemInclusiveTax,
            twf.stdexp_chdr.CHDR_CashFlag,
            twf.stdexp_chdr.CHDR_EmployeeMealFlag,
            twf.stdexp_chdr.CHDR_ReopenCloseCheckFlag,
            twf.stdexp_chdr.CHDR_CheckSplitFlag
            )
            SET twf.stdexp_chdr.ID = NULL;""")
                conexion.commit()
                print("Carga de datos CHDR exitosa")


        except Error as ex:
            print(f"error durante la conexion CHDR: {ex}")


        finally:
            if conexion.is_connected():
                conexion.close()    #Se cerro la conexion a la base de datos
                print("la conexion ha finalizado")
        move(na,f"\\Users\\Administrator\\Desktop\\DimensionData\\Destination\\{fecha_carpeta_ayer}\\")


#TAX

    elif na[73:76]=="TAX":
        archivo=na[61:80]
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
            INTO TABLE twf.stdexp_tax
            CHARACTER SET UTF8mb4
            FIELDS TERMINATED BY '|'
            LINES TERMINATED BY '\n'
            (
            twf.stdexp_tax.Record_Type,
            twf.stdexp_tax.StoreID,
            twf.stdexp_tax.Date,
            twf.stdexp_tax.RVC_num,
            twf.stdexp_tax.TAX_number,
            twf.stdexp_tax.TAX_name,
            twf.stdexp_tax.TAX_Rate,
            twf.stdexp_tax.TAX_TotalDay,
            twf.stdexp_tax.TAX_TaxableSls,
            twf.stdexp_tax.TAX_ExemptSls,
            twf.stdexp_tax.TAX_MasterName,
            twf.stdexp_tax.TAX_MasterNum,
            twf.stdexp_tax.RVC_name,
            twf.stdexp_tax.RVC_MasterName,
            twf.stdexp_tax.RVC_MasterNum,
            twf.stdexp_tax.TAX_Type,
            twf.stdexp_tax.TAX_RateVat,
            twf.stdexp_tax.TAX_GrossS,
            twf.stdexp_tax.TAX_NetSales,
            twf.stdexp_tax.TAX_TotalPrcnt,
            twf.stdexp_tax.TAX_TotalTaxableSls,
            twf.stdexp_tax.TAX_TotalTaxableSlsVat,
            twf.stdexp_tax.TAX_VatAfterDscnt,
            twf.stdexp_tax.TAX_SlsNetVatAfterDscnt
            )
            SET twf.stdexp_tax.ID = NULL;""")
                conexion.commit()
                print("Carga de datos TAX exitosa")


        except Error as ex:
            print(f"error durante la conexion TAX: {ex}")


        finally:
            if conexion.is_connected():
                conexion.close()    #Se cerro la conexion a la base de datos
                print("la conexion ha finalizado")
        move(na,f"\\Users\\Administrator\\Desktop\\DimensionData\\Destination\\{fecha_carpeta_ayer}\\")


#MNPR

    elif na[73:77]=="MNPR":
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
            INTO TABLE twf.stdexp_mnpr
            CHARACTER SET UTF8mb4
            FIELDS TERMINATED BY '|'
            LINES TERMINATED BY '\n'
            (
            twf.stdexp_mnpr.Record_Type,
            twf.stdexp_mnpr.StoreID,
            twf.stdexp_mnpr.Date,
            twf.stdexp_mnpr.RVC_num,
            twf.stdexp_mnpr.MI_number,
            twf.stdexp_mnpr.MNPR_LvlPrice,
            twf.stdexp_mnpr.MNPR_LvlName,
            twf.stdexp_mnpr.MNPR_Price,
            twf.stdexp_mnpr.MNPR_Cost,
            twf.stdexp_mnpr.MNPR_Efectivity,
            twf.stdexp_mnpr.MNPR_TaxClassNumber,
            twf.stdexp_mnpr.MNPR_MenuLvl,
            twf.stdexp_mnpr.RVC_name,
            twf.stdexp_mnpr.RVC_MasterName,
            twf.stdexp_mnpr.RVC_MasterNum,
            twf.stdexp_mnpr.MI_name,
            twf.stdexp_mnpr.MI_MasterName,
            twf.stdexp_mnpr.MI_MasterNum,
            twf.stdexp_mnpr.MNPR_majorgroup_name,
            twf.stdexp_mnpr.MNPR_majorgroup_number,
            twf.stdexp_mnpr.MNPR_MasterMajorgroup_name,
            twf.stdexp_mnpr.MI_Master_majorgroup_number,
            twf.stdexp_mnpr.MNPR_familygroup_name,
            twf.stdexp_mnpr.MNPR_familygroup_num,
            twf.stdexp_mnpr.MNPR_Master_familygroup_name,
            twf.stdexp_mnpr.MNPR_Master_familygroup_num
            )
            SET twf.stdexp_mnpr.ID = NULL;""")
                conexion.commit()
                print("Carga de datos MNPR exitosa")


        except Error as ex:
            print(f"error durante la conexion MNPR: {ex}")


        finally:
            if conexion.is_connected():
                conexion.close()    #Se cerro la conexion a la base de datos
                print("la conexion ha finalizado")
        move(na,f"\\Users\\Administrator\\Desktop\\DimensionData\\Destination\\{fecha_carpeta_ayer}\\")


#MID

    elif na[73:76]=="MID":
        archivo=na[61:80]
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
            INTO TABLE twf.stdexp_mid
            CHARACTER SET UTF8mb4
            FIELDS TERMINATED BY '|'
            LINES TERMINATED BY '\n'
            (
            twf.stdexp_mid.Record_Type,
            twf.stdexp_mid.StoreID,
            twf.stdexp_mid.Date,
            twf.stdexp_mid.RVC_num,
            twf.stdexp_mid.OT_number,
            twf.stdexp_mid.MI_number,
            twf.stdexp_mid.MI_Name,
            twf.stdexp_mid.MI_pricelevel,
            twf.stdexp_mid.MI_SlsCount,
            twf.stdexp_mid.MI_SlsTotal,
            twf.stdexp_mid.MI_TotalDscnt,
            twf.stdexp_mid.MI_ReturnCount,
            twf.stdexp_mid.MI_volume,
            twf.stdexp_mid.MI_PrepCost,
            twf.stdexp_mid.MI_MasterName,
            twf.stdexp_mid.MI_MasterNumber,
            twf.stdexp_mid.RVC_name,
            twf.stdexp_mid.RVC_MasterName,
            twf.stdexp_mid.RVC_MasterNum,
            twf.stdexp_mid.MI_name2,
            twf.stdexp_mid.MI_MasterName2,
            twf.stdexp_mid.MI_majorgroup_name,
            twf.stdexp_mid.MI_majorgroup_number,
            twf.stdexp_mid.MI_MasterMajorgroup_name,
            twf.stdexp_mid.MI_Master_majorgroup_number,
            twf.stdexp_mid.MI_familygroup_name,
            twf.stdexp_mid.MI_familygroup_num,
            twf.stdexp_mid.MI_Master_familygroup_name,
            twf.stdexp_mid.MI_Master_familygroup_num,
            twf.stdexp_mid.OT_name,
            twf.stdexp_mid.OT_MasterName,
            twf.stdexp_mid.OT_MasterNum,
            twf.stdexp_mid.MI_GrossS_beforediscount,
            twf.stdexp_mid.DSC_GrossVat,
            twf.stdexp_mid.MI_GrossS_afterdiscount,
            twf.stdexp_mid.MI_VAT_beforediscount,
            twf.stdexp_mid.MI_DscntVat,
            twf.stdexp_mid.MI_VatAfterDscnt,
            twf.stdexp_mid.MI_TotalVat,
            twf.stdexp_mid.MI_NetSales_beforediscount,
            twf.stdexp_mid.MI_DscntNetVat,
            twf.stdexp_mid.MI_SlsNetVat
            )
            SET twf.stdexp_mid.ID = NULL;""")
                conexion.commit()
                print("Carga de datos MID exitosa")


        except Error as ex:
            print(f"error durante la conexion MID: {ex}")


        finally:
            if conexion.is_connected():
                conexion.close()    #Se cerro la conexion a la base de datos
                print("la conexion ha finalizado")
        move(na,f"\\Users\\Administrator\\Desktop\\DimensionData\\Destination\\{fecha_carpeta_ayer}\\")


#OT

    elif na[73:79]=="OT.csv":
        archivo=na[61:79]
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
            INTO TABLE twf.stdexp_ot
            CHARACTER SET UTF8mb4
            FIELDS TERMINATED BY '|'
            LINES TERMINATED BY '\n'
            (
            twf.stdexp_ot.Record_Type,
            twf.stdexp_ot.StoreID,
            twf.stdexp_ot.Date,
            twf.stdexp_ot.RVC_num,
            twf.stdexp_ot.OT_Number,
            twf.stdexp_ot.OT_Name,
            twf.stdexp_ot.OT_Count,
            twf.stdexp_ot.OT_TotalDayNetSales,
            twf.stdexp_ot.OT_TotalGuests,
            twf.stdexp_ot.OT_TablesTurned,
            twf.stdexp_ot.OT_MasterName,
            twf.stdexp_ot.OT_MasterNum,
            twf.stdexp_ot.OT_TotalByPeriod,
            twf.stdexp_ot.RVC_name,
            twf.stdexp_ot.RVC_MasterName,
            twf.stdexp_ot.RVC_MasterNum,
            twf.stdexp_ot.OT_TotalDayTables,
            twf.stdexp_ot.OT_ServiceCharge,
            twf.stdexp_ot.OT_TableTime,
            twf.stdexp_ot.OT_TotalPrepCost,
            twf.stdexp_ot.OT_TotalDayReturns,
            twf.stdexp_ot.OT_CountDayReturns,
            twf.stdexp_ot.OT_TotalDayVoid,
            twf.stdexp_ot.OT_TotalDayVoidCount,
            twf.stdexp_ot.OT_ManagerVoidTotal,
            twf.stdexp_ot.OT_ManagerVoidCount,
            twf.stdexp_ot.OT_CancelAmount,
            twf.stdexp_ot.OT_CancelCount,
            twf.stdexp_ot.OT_ErrorCorrectTotal,
            twf.stdexp_ot.OT_ErrorCorrectCount,
            twf.stdexp_ot.OT_CheckOpenCount,
            twf.stdexp_ot.OT_CHeckClosedCount,
            twf.stdexp_ot.OT_Checks_inProgress,
            twf.stdexp_ot.OT_GrossS_beforediscount,
            twf.stdexp_ot.OT_TotalDscnt
            )
            SET twf.stdexp_ot.ID = NULL;""")
                conexion.commit()
                print("Carga de datos OT exitosa")


        except Error as ex:
            print(f"error durante la conexion OT: {ex}")


        finally:
            if conexion.is_connected():
                conexion.close()    #Se cerro la conexion a la base de datos
                print("la conexion ha finalizado")
        move(na,f"\\Users\\Administrator\\Desktop\\DimensionData\\Destination\\{fecha_carpeta_ayer}\\")


#SUM

    elif na[73:76]=="SUM":
        archivo=na[61:80]
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
            INTO TABLE twf.stdexp_sum
            CHARACTER SET UTF8mb4
            FIELDS TERMINATED BY '|'
            LINES TERMINATED BY '\n'
            (
            twf.stdexp_sum.Record_Type,
            twf.stdexp_sum.StoreID,
            twf.stdexp_sum.Date,
            twf.stdexp_sum.RVC_num,
            twf.stdexp_sum.RVC_name,
            twf.stdexp_sum.SUM_TotalDayNetSales,
            twf.stdexp_sum.SUM_TotalDiscount,
            twf.stdexp_sum.SUM_TotalDaySrvcChrg,
            twf.stdexp_sum.SUM_TotalDayVoid,
            twf.stdexp_sum.SUM_TotalDayVoidCount,
            twf.stdexp_sum.SUM_TotalDayReturns,
            twf.stdexp_sum.SUM_TotalDayReturnCount,
            twf.stdexp_sum.SUM_TotalDayTax,
            twf.stdexp_sum.SUM_NonTaxableSls,
            twf.stdexp_sum.SUM_TotalExemptTax,
            twf.stdexp_sum.SUM_TotalDayTransactions,
            twf.stdexp_sum.SUM_TotalDayGuests,
            twf.stdexp_sum.SUM_TablesTurned,
            twf.stdexp_sum.SUM_TotalOrderTime,
            twf.stdexp_sum.SUM_Total_OverShort,
            twf.stdexp_sum.SUM_ForecastedSls,
            twf.stdexp_sum.RVC_MasterName,
            twf.stdexp_sum.RVC_MasterNum,
            twf.stdexp_sum.SUM_Weather,
            twf.stdexp_sum.SUM_HighTemperature,
            twf.stdexp_sum.SUM_LowTemperature,
            twf.stdexp_sum.SUM_GrossS_beforediscount,
            twf.stdexp_sum.SUM_GrossVatDiscount,
            twf.stdexp_sum.SUM_TotalVat,
            twf.stdexp_sum.SUM_NetSlsVat,
            twf.stdexp_sum.SUM_TotalCredit,
            twf.stdexp_sum.SUM_TotalCostSls,
            twf.stdexp_sum.SUM_PrepCost,
            twf.stdexp_sum.SUM_TotalDayTables,
            twf.stdexp_sum.SUM_LastYearSls,
            twf.stdexp_sum.SUM_LastYearGuests,
            twf.stdexp_sum.SUM_LastYearChecks,
            twf.stdexp_sum.SUM_ForecastedGrossSls,
            twf.stdexp_sum.SUM_ForecastedNetSls,
            twf.stdexp_sum.SUM_ForecastedTotalDscnt,
            twf.stdexp_sum.SUM_ForecastedTotalChecks,
            twf.stdexp_sum.SUM_ForecastedTotalTables,
            twf.stdexp_sum.SUM_ForecastedAvgGuests,
            twf.stdexp_sum.SUM_ForecastedSlsNetVatBeforeDscnt,
            twf.stdexp_sum.SUM_ForecastedSlsNetVatAfterDscnt,
            twf.stdexp_sum.SUM_TableTime,
            twf.stdexp_sum.SUM_ErrorCorrectTotal,
            twf.stdexp_sum.SUM_ErrorCorrectCount,
            twf.stdexp_sum.SUM_MngrVoidAmount,
            twf.stdexp_sum.SUM_MngrVoidCount,
            twf.stdexp_sum.SUM_CancelAmount,
            twf.stdexp_sum.SUM_CancelCount,
            twf.stdexp_sum.SUM_ChecksOpenAmount,
            twf.stdexp_sum.SUM_ChecksOpenCount,
            twf.stdexp_sum.SUM_ChecksClosedAmount,
            twf.stdexp_sum.SUM_ChecksClosedCount,
            twf.stdexp_sum.SUM_ChecksTransferInAmount,
            twf.stdexp_sum.SUM_ChecksTransferInCount,
            twf.stdexp_sum.SUM_ChecksTransferOutAmount,
            twf.stdexp_sum.SUM_ChecksTransferOutCount,
            twf.stdexp_sum.SUM_NonRevenueSrvcChrg
            )
            SET twf.stdexp_sum.ID = NULL;""")
                conexion.commit()
                print("Carga de datos SUM exitosa")


        except Error as ex:
            print(f"error durante la conexion SUM: {ex}")


        finally:
            if conexion.is_connected():
                conexion.close()    #Se cerro la conexion a la base de datos
                print("la conexion ha finalizado")
        move(na,f"\\Users\\Administrator\\Desktop\\DimensionData\\Destination\\{fecha_carpeta_ayer}\\")


#CMB

    elif na[73:76]=="CMB":
        archivo=na[61:80]
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
            INTO TABLE twf.stdexp_cmb
            CHARACTER SET UTF8mb4
            FIELDS TERMINATED BY '|'
            LINES TERMINATED BY '\n'
            (
            twf.stdexp_cmb.Record_Type,
            twf.stdexp_cmb.StoreID,
            twf.stdexp_cmb.Date,
            twf.stdexp_cmb.RVC_name,
            twf.stdexp_cmb.RVC_num,
            twf.stdexp_cmb.RVC_MasterName,
            twf.stdexp_cmb.RVC_MasterNum,
            twf.stdexp_cmb.OT_name,
            twf.stdexp_cmb.OT_number,
            twf.stdexp_cmb.OT_MasterName,
            twf.stdexp_cmb.OT_MasterNumber,
            twf.stdexp_cmb.CMB_MainComboItemName,
            twf.stdexp_cmb.CMB_MainComboItemNum,
            twf.stdexp_cmb.CMB_MainComboItemMasterName,
            twf.stdexp_cmb.CMB_MainComboItemMasterNum,
            twf.stdexp_cmb.CMB_Component_ItemName,
            twf.stdexp_cmb.CMB_Component_ItemNum,
            twf.stdexp_cmb.CMB_Component_ItemMasterName,
            twf.stdexp_cmb.CMB_Component_ItemMasterNum,
            twf.stdexp_cmb.CMB_Original_ItemName,
            twf.stdexp_cmb.CMB_Original_itemNum,
            twf.stdexp_cmb.CMB_Original_ItemMasterName,
            twf.stdexp_cmb.CMB_Original_ItemMasterNum,
            twf.stdexp_cmb.CMB_SalesTotal,
            twf.stdexp_cmb.CMB_SalesCount,
            twf.stdexp_cmb.CMB_GrossS_beforediscount,
            twf.stdexp_cmb.CMB_TotalDscnt,
            twf.stdexp_cmb.CMB_DscntGrossVat,
            twf.stdexp_cmb.CMB_GrossS_AfterDscnt,
            twf.stdexp_cmb.CMB_VAT_beforediscount,
            twf.stdexp_cmb.CMB_DscntVAT,
            twf.stdexp_cmb.CMB_VatAfterDscnt,
            twf.stdexp_cmb.CMB_TotalVat,
            twf.stdexp_cmb.CMB_NetSales_beforediscount,
            twf.stdexp_cmb.CMB_DscntNetVat,
            twf.stdexp_cmb.CMB_NetVatSales
            )
            SET twf.stdexp_cmb.ID = NULL;""")
                conexion.commit()
                print("Carga de datos CMB exitosa")


        except Error as ex:
            print(f"error durante la conexion CMB: {ex}")


        finally:
            if conexion.is_connected():
                conexion.close()    #Se cerro la conexion a la base de datos
                print("la conexion ha finalizado")
        move(na,f"\\Users\\Administrator\\Desktop\\DimensionData\\Destination\\{fecha_carpeta_ayer}\\")


#OTD

    elif na[73:76]=="OTD":
        archivo=na[61:80]
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
            INTO TABLE twf.stdexp_otd
            CHARACTER SET UTF8mb4
            FIELDS TERMINATED BY '|'
            LINES TERMINATED BY '\n'
            (            
            twf.stdexp_otd.Record_Type,
            twf.stdexp_otd.StoreID,
            twf.stdexp_otd.Date,
            twf.stdexp_otd.RVC_name,
            twf.stdexp_otd.RVC_num,
            twf.stdexp_otd.RVC_MasterName,
            twf.stdexp_otd.RVC_MasterNum,
            twf.stdexp_otd.OT_name,
            twf.stdexp_otd.OT_number,
            twf.stdexp_otd.OT_MasterName,
            twf.stdexp_otd.OT_MasterNum,
            twf.stdexp_otd.OTD_TotalDayNetSales,
            twf.stdexp_otd.OTD_TotalDaySrvcChrg,
            twf.stdexp_otd.OTD_TotalDayVoid,
            twf.stdexp_otd.OTD_TotalDayVoidCount,
            twf.stdexp_otd.OTD_TotalDayReturns,
            twf.stdexp_otd.OTD_CountDayReturns,
            twf.stdexp_otd.OTD_TotalDayTax,
            twf.stdexp_otd.OTD_TotalChecks,
            twf.stdexp_otd.OTD_TotalDayGuests,
            twf.stdexp_otd.OTD_TablesTurned,
            twf.stdexp_otd.OTD_TotalDayTables,
            twf.stdexp_otd.OTD_TotalOrderTime,
            twf.stdexp_otd.OTD_ForecastedSls,
            twf.stdexp_otd.OTD_PrepCost,
            twf.stdexp_otd.OTD_LastYearSls,
            twf.stdexp_otd.OTD_LastYearGuest,
            twf.stdexp_otd.OTD_LastYearChecks,
            twf.stdexp_otd.OTD_TableTime,
            twf.stdexp_otd.OTD_ErrorCorrectAmount,
            twf.stdexp_otd.OTD_ErrorCorrectCount,
            twf.stdexp_otd.OTD_MngrVoidAmount,
            twf.stdexp_otd.OTD_MngrVoidCount,
            twf.stdexp_otd.OTD_CancelAmount,
            twf.stdexp_otd.OTD_CancelCount,
            twf.stdexp_otd.OTD_ChecksOpenCount,
            twf.stdexp_otd.OTD_ChecksClosedCount,
            twf.stdexp_otd.OTD_NonRevenueSrvcChrg,
            twf.stdexp_otd.OTD_GrossS_beforediscount,
            twf.stdexp_otd.OTD_TotalDscnt,
            twf.stdexp_otd.OTD_DscntGrossVat,
            twf.stdexp_otd.OTD_GrossS_AfterDscnt,
            twf.stdexp_otd.OTD_TotalVat,
            twf.stdexp_otd.OTD_NetSales,
            twf.stdexp_otd.OTD_ForecastedGrossSls,
            twf.stdexp_otd.OTD_ForecastedNetSls,
            twf.stdexp_otd.OTD_ForecastedTotalDscnt,
            twf.stdexp_otd.OTD_ForecastedTotalChecks,
            twf.stdexp_otd.OTD_ForecastedTableTurns,
            twf.stdexp_otd.OTD_ForecastedAvgCheckAmount,
            twf.stdexp_otd.OTD_ForecastedSlsNetVatBeforeDscnt,
            twf.stdexp_otd.OTD_ForecastedSlsNetVatAfterDscnt
            )
            SET twf.stdexp_otd.ID = NULL;""")
                conexion.commit()
                print("Carga de datos OTD exitosa")


        except Error as ex:
            print(f"error durante la conexion OTD: {ex}")


        finally:
            if conexion.is_connected():
                conexion.close()    #Se cerro la conexion a la base de datos
                print("la conexion ha finalizado")
        move(na,f"\\Users\\Administrator\\Desktop\\DimensionData\\Destination\\{fecha_carpeta_ayer}\\")


#SVC

    elif na[73:76]=="SVC":
        archivo=na[61:80]
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
            INTO TABLE twf.stdexp_svc
            CHARACTER SET UTF8mb4
            FIELDS TERMINATED BY '|'
            LINES TERMINATED BY '\n'
            (            
            twf.stdexp_svc.Record_Type,
            twf.stdexp_svc.StoreID,
            twf.stdexp_svc.Date,
            twf.stdexp_svc.RVC_num,
            twf.stdexp_svc.SVC_Number,
            twf.stdexp_svc.SVC_Name,
            twf.stdexp_svc.SVC_Total,
            twf.stdexp_svc.SVC_Count,
            twf.stdexp_svc.SVC_MasterName,
            twf.stdexp_svc.SVC_MasterNum,
            twf.stdexp_svc.RVC_name,
            twf.stdexp_svc.RVC_MasterName,
            twf.stdexp_svc.RVC_MasterNum,
            twf.stdexp_svc.SVC_Type
            )
            SET twf.stdexp_svc.ID = NULL;""")
                conexion.commit()
                print("Carga de datos SVC exitosa")


        except Error as ex:
            print(f"error durante la conexion SVC: {ex}")


        finally:
            if conexion.is_connected():
                conexion.close()    #Se cerro la conexion a la base de datos
                print("la conexion ha finalizado")
        move(na,f"\\Users\\Administrator\\Desktop\\DimensionData\\Destination\\{fecha_carpeta_ayer}\\")


#INV

    elif na[74:77]=="INV":
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
            INTO TABLE twf.stdexp_inv
            CHARACTER SET UTF8mb4
            FIELDS TERMINATED BY '|'
            LINES TERMINATED BY '\n'
            (
            twf.stdexp_inv.Record_Type,
            twf.stdexp_inv.StoreID,
            twf.stdexp_inv.Date,
            twf.stdexp_inv.INV_ItemName1,
            twf.stdexp_inv.INV_ItemName2,
            twf.stdexp_inv.INV_ItemNameNum,
            twf.stdexp_inv.INV_ItemMasterName1,
            twf.stdexp_inv.INV_ItemMasterName2,
            twf.stdexp_inv.INV_ItemMasterNum,
            twf.stdexp_inv.INV_Type,
            twf.stdexp_inv.INV_CostCenterName,
            twf.stdexp_inv.INV_CostCenterNum,
            twf.stdexp_inv.INV_CostCenterMasterName,
            twf.stdexp_inv.INV_CostCenterMasterNum,
            twf.stdexp_inv.INV_CostGroupName,
            twf.stdexp_inv.INV_CostGroupNumber,
            twf.stdexp_inv.INV_CostGroupMasterName,
            twf.stdexp_inv.INV_CostGroupMasterNum,
            twf.stdexp_inv.INV_StandardUnitMeasureName,
            twf.stdexp_inv.INV_StandardUnitMeasureNum,
            twf.stdexp_inv.INV_StandardUnitMeasureMasterName,
            twf.stdexp_inv.INV_StandardUnitMeasureMasterNum,
            twf.stdexp_inv.INV_BaseUnitMeasureName,
            twf.stdexp_inv.INV_BaseUnitMeasureNum,
            twf.stdexp_inv.INV_BaseUnitMeasureMasterName,
            twf.stdexp_inv.INV_BaseUnitMeasureMasterNum,
            twf.stdexp_inv.INV_OnHandQuantity,
            twf.stdexp_inv.INV_OnHandValue,
            twf.stdexp_inv.INV_ReceiptQuantity,
            twf.stdexp_inv.INV_ReceiptValue,
            twf.stdexp_inv.INV_UsageQuantity,
            twf.stdexp_inv.INV_ProductionUsageQuantity,
            twf.stdexp_inv.INV_ProductionReceiptQuantity,
            twf.stdexp_inv.INV_ProductionReceiptValue,
            twf.stdexp_inv.INV_TransferInQuantity,
            twf.stdexp_inv.INV_TransferInValue,
            twf.stdexp_inv.INV_TransferOutQuantity,
            twf.stdexp_inv.INV_VarianceQuantity,
            twf.stdexp_inv.INV_CountedQuantity,
            twf.stdexp_inv.INV_CountedTime
            )
            SET twf.stdexp_inv.ID = NULL;""")
                conexion.commit()
                print("Carga de datos INV exitosa")


        except Error as ex:
            print(f"error durante la conexion INV: {ex}")


        finally:
            if conexion.is_connected():
                conexion.close()    #Se cerro la conexion a la base de datos
                print("la conexion ha finalizado")
        move(na,f"\\Users\\Administrator\\Desktop\\DimensionData\\Destination\\{fecha_carpeta_ayer}\\")


#PO

    elif na[74:76]=="PO":
        archivo=na[61:80]
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
            INTO TABLE twf.stdexp_po
            CHARACTER SET UTF8mb4
            FIELDS TERMINATED BY '|'
            LINES TERMINATED BY '\n'
            (
            twf.stdexp_po.Record_Type,
            twf.stdexp_po.StoreID,
            twf.stdexp_po.Date,
            twf.stdexp_po.PO_EmployeeName,
            twf.stdexp_po.PO_Number,
            twf.stdexp_po.PO_VendorName,
            twf.stdexp_po.PO_VendorNumber,
            twf.stdexp_po.PO_VendorMasterName,
            twf.stdexp_po.PO_VendorMasterNum,
            twf.stdexp_po.PO_VendorAddress1,
            twf.stdexp_po.PO_VendorAddress2,
            twf.stdexp_po.PO_VendorCity,
            twf.stdexp_po.PO_Status,
            twf.stdexp_po.PO_OrderDate,
            twf.stdexp_po.PO_ExpectedDeliveryDate,
            twf.stdexp_po.PO_LastUpdateBusinessDate,
            twf.stdexp_po.PO_DocAndDescription
            )
            SET twf.stdexp_po.ID = NULL;""")
                conexion.commit()
                print("Carga de datos PO exitosa")


        except Error as ex:
            print(f"error durante la conexion PO: {ex}")


        finally:
            if conexion.is_connected():
                conexion.close()    #Se cerro la conexion a la base de datos
                print("la conexion ha finalizado")
        move(na,f"\\Users\\Administrator\\Desktop\\DimensionData\\Destination\\{fecha_carpeta_ayer}\\")


#RCPT

    elif na[74:78]=="RCPT":
        archivo=na[61:82]
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
            INTO TABLE twf.stdexp_rcpt
            CHARACTER SET UTF8mb4
            FIELDS TERMINATED BY '|'
            LINES TERMINATED BY '\n'
            (       
            twf.stdexp_rcpt.Record_Type,
            twf.stdexp_rcpt.StoreID,
            twf.stdexp_rcpt.Date,
            twf.stdexp_rcpt.RCPT_ReceiptNumber,
            twf.stdexp_rcpt.RCPT_VendorName,
            twf.stdexp_rcpt.RCPT_VendorNumber,
            twf.stdexp_rcpt.RCPT_VendorMasterName,
            twf.stdexp_rcpt.RCPT_VendorMasterNumber,
            twf.stdexp_rcpt.RCPT_VendorAddress1,
            twf.stdexp_rcpt.RCPT_VendorAddress2,
            twf.stdexp_rcpt.RCPT_VendorCity,
            twf.stdexp_rcpt.RCPT_ReceiptReceivedBy,
            twf.stdexp_rcpt.RCPT_ReceiptStatus,
            twf.stdexp_rcpt.RCPT_InvoiceDoc,
            twf.stdexp_rcpt.RCPT_PackingDoc,
            twf.stdexp_rcpt.RCPT_PackingDate,
            twf.stdexp_rcpt.RCPT_TotalAdjusted,
            twf.stdexp_rcpt.RCPT_InvoiceDate,
            twf.stdexp_rcpt.RCPT_InvoiceTotal,
            twf.stdexp_rcpt.RCPT_PurchaseOrderCreatedBy,
            twf.stdexp_rcpt.RCPT_PurchaseOrderNum,
            twf.stdexp_rcpt.RCPT_PurchaseOrderStatus,
            twf.stdexp_rcpt.RCPT_PurchaseOrderDate
            )
            SET twf.stdexp_rcpt.ID = NULL;""")
                conexion.commit()
                print("Carga de datos RCPT exitosa")


        except Error as ex:
            print(f"error durante la conexion RCPT: {ex}")


        finally:
            if conexion.is_connected():
                conexion.close()    #Se cerro la conexion a la base de datos
                print("la conexion ha finalizado")
        move(na,f"\\Users\\Administrator\\Desktop\\DimensionData\\Destination\\{fecha_carpeta_ayer}\\")


#XFER

    elif na[74:78]=="XFER":
        archivo=na[61:82]
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
            INTO TABLE twf.stdexp_xfer
            CHARACTER SET UTF8mb4
            FIELDS TERMINATED BY '|'
            LINES TERMINATED BY '\n'
            (           
            twf.stdexp_xfer.Record_Type,
            twf.stdexp_xfer.StoreID,
            twf.stdexp_xfer.Date,
            twf.stdexp_xfer.XFER_TransferNum,
            twf.stdexp_xfer.XFER_TransferRefNum,
            twf.stdexp_xfer.XFER_TransferExtRefNum,
            twf.stdexp_xfer.XFER_CostCenterSourceName,
            twf.stdexp_xfer.XFER_CostCenterSourceNum,
            twf.stdexp_xfer.XFER_CostCenterSourceMasterName,
            twf.stdexp_xfer.XFER_CostCenterSourceMasterNum,
            twf.stdexp_xfer.XFER_CostCenterDestName,
            twf.stdexp_xfer.XFER_CostCenterDestNum,
            twf.stdexp_xfer.XFER_CostCenterDestMasterName,
            twf.stdexp_xfer.XFER_CostCenterDestMasterNum,
            twf.stdexp_xfer.XFER_TransferAmount,
            twf.stdexp_xfer.XFER_TransferStatus,
            twf.stdexp_xfer.XFER_TransferDate
            )
            SET twf.stdexp_xfer.ID = NULL;""")
                conexion.commit()
                print("Carga de datos XFER exitosa")


        except Error as ex:
            print(f"error durante la conexion XFER: {ex}")


        finally:
            if conexion.is_connected():
                conexion.close()    #Se cerro la conexion a la base de datos
                print("la conexion ha finalizado")
        move(na,f"\\Users\\Administrator\\Desktop\\DimensionData\\Destination\\{fecha_carpeta_ayer}\\")


#XFERDTL

    elif na[74:81]=="XFERDTL":
        archivo=na[61:85]
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
            INTO TABLE twf.stdexp_xferdtl
            CHARACTER SET UTF8mb4
            FIELDS TERMINATED BY '|'
            LINES TERMINATED BY '\n'
            (         
            twf.stdexp_xferdtl.Record_Type,
            twf.stdexp_xferdtl.StoreID,
            twf.stdexp_xferdtl.Date,
            twf.stdexp_xferdtl.XFER_TransferDetailNum,
            twf.stdexp_xferdtl.XFER_TransferNum,
            twf.stdexp_xferdtl.XFER_InvItemName1,
            twf.stdexp_xferdtl.XFER_InvItemName2,
            twf.stdexp_xferdtl.XFER_InvItemNum,
            twf.stdexp_xferdtl.XFER_InvItemMasterName1,
            twf.stdexp_xferdtl.XFER_InvItemMasterName2,
            twf.stdexp_xferdtl.XFER_InvItemMasterNum,
            twf.stdexp_xferdtl.XFER_UnitMeasureName,
            twf.stdexp_xferdtl.XFER_UnitMeasureNum,
            twf.stdexp_xferdtl.XFER_UnitMeasureMasterName,
            twf.stdexp_xferdtl.XFER_UnitMeasureMasterNum,
            twf.stdexp_xferdtl.XFER_Quiantity,
            twf.stdexp_xferdtl.XFER_Price,
            twf.stdexp_xferdtl.XFER_PriceChanged
            )
            SET twf.stdexp_xferdtl.ID = NULL;""")
                conexion.commit()
                print("Carga de datos XFERDTL exitosa")


        except Error as ex:
            print(f"error durante la conexion XFERDTL: {ex}")


        finally:
            if conexion.is_connected():
                conexion.close()    #Se cerro la conexion a la base de datos
                print("la conexion ha finalizado")
        move(na,f"\\Users\\Administrator\\Desktop\\DimensionData\\Destination\\{fecha_carpeta_ayer}\\")


#PAY

    elif na[74:77]=="PAY":
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
            INTO TABLE twf.stdexp_pay
            CHARACTER SET UTF8mb4
            FIELDS TERMINATED BY '|'
            LINES TERMINATED BY '\n'
            (
            twf.stdexp_pay.Record_Type,
            twf.stdexp_pay.StoreID,
            twf.stdexp_pay.Date,
            twf.stdexp_pay.PAY_ID,
            twf.stdexp_pay.PAY_BusinessDate,
            twf.stdexp_pay.PAY_JobCodeNumber,
            twf.stdexp_pay.PAY_JobCodeName,
            twf.stdexp_pay.PAY_RegularHour,
            twf.stdexp_pay.PAY_RegularPay,
            twf.stdexp_pay.PAY_OvertimeHour1,
            twf.stdexp_pay.PAY_OvertimePay1,
            twf.stdexp_pay.PAY_OvertimeHourOther,
            twf.stdexp_pay.PAY_OvertimePayOther,
            twf.stdexp_pay.PAY_OtherType,
            twf.stdexp_pay.PAY_OtherHour,
            twf.stdexp_pay.PAY_OtherPay,
            twf.stdexp_pay.PAY_OtherPayRate,
            twf.stdexp_pay.PAY_F_BGrossReceipts,
            twf.stdexp_pay.PAY_TotalTipsPaid,
            twf.stdexp_pay.PAY_TotalChargedReceipts,
            twf.stdexp_pay.PAY_TotalChargedTips,
            twf.stdexp_pay.PAY_Total_IndirectTips,
            twf.stdexp_pay.PAY_TotalDeclareTips,
            twf.stdexp_pay.PAY_HomeStore,
            twf.stdexp_pay.PAY_NonRVC_RegularHour,
            twf.stdexp_pay.PAY_NonRVC_RegularPay,
            twf.stdexp_pay.PAY_NonRVC_OvertimeHour,
            twf.stdexp_pay.PAY_NonRVC_OvertimePay,
            twf.stdexp_pay.PAY_OtherPayDescription,
            twf.stdexp_pay.RVC_name,
            twf.stdexp_pay.RVC_num,
            twf.stdexp_pay.RVC_MasterName,
            twf.stdexp_pay.RVC_MasterNum,
            twf.stdexp_pay.EMP_name,
            twf.stdexp_pay.EMP_Surname,
            twf.stdexp_pay.EMP_number,
            twf.stdexp_pay.PAY_JobCodeMasterName,
            twf.stdexp_pay.PAY_JobCodeMasterNum,
            twf.stdexp_pay.PAY_ServiceTips,
            twf.stdexp_pay.PAY_CashTups,
            twf.stdexp_pay.PAY_TotalTips,
            twf.stdexp_pay.PAY_TotalDaySrvcChrg,
            twf.stdexp_pay.PAY_OvertimeHour2,
            twf.stdexp_pay.PAY_OvertimePay2,
            twf.stdexp_pay.PAY_OvertimeHour3,
            twf.stdexp_pay.PAY_OvertimePay3,
            twf.stdexp_pay.PAY_OvertimeHour4,
            twf.stdexp_pay.PAY_OvertimePay4,
            twf.stdexp_pay.PAY_GrossS_beforediscount,
            twf.stdexp_pay.PAY_GrossVatDiscount,
            twf.stdexp_pay.PAY_GrossSlsAfterDscnt,
            twf.stdexp_pay.PAY_ExternalPayroll_ID
            )
            SET twf.stdexp_pay.ID = NULL;""")
                conexion.commit()
                print("Carga de datos PAY exitosa")


        except Error as ex:
            print(f"error durante la conexion PAY: {ex}")


        finally:
            if conexion.is_connected():
                conexion.close()    #Se cerro la conexion a la base de datos
                print("la conexion ha finalizado")
        move(na,f"\\Users\\Administrator\\Desktop\\DimensionData\\Destination\\{fecha_carpeta_ayer}\\")


#LOC

    elif na[74:77]=="LOC":
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
            INTO TABLE twf.stdexp_loc
            CHARACTER SET UTF8mb4
            FIELDS TERMINATED BY '|'
            LINES TERMINATED BY '\n'
            (
            twf.stdexp_loc.Record_Type,
            twf.stdexp_loc.StoreLvl,
            twf.stdexp_loc.Date,
            twf.stdexp_loc.LOC_Name,
            twf.stdexp_loc.LOC_ID,
            twf.stdexp_loc.Organization_Lvl,
            twf.stdexp_loc.Source,
            twf.stdexp_loc.Open_Date,
            twf.stdexp_loc.Timezone,
            twf.stdexp_loc.Currency,
            twf.stdexp_loc.Date_Current,
            twf.stdexp_loc.Date_Before
            )
            SET twf.stdexp_loc.ID = NULL;""")
                conexion.commit()
                print("Carga de datos LOC exitosa")


        except Error as ex:
            print(f"error durante la conexion LOC: {ex}")


        finally:
            if conexion.is_connected():
                conexion.close()    #Se cerro la conexion a la base de datos
                print("la conexion ha finalizado")
        move(na,f"\\Users\\Administrator\\Desktop\\DimensionData\\Destination\\{fecha_carpeta_ayer}\\")


    else:
        continue


print("well done boy!")