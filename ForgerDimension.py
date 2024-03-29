from glob import glob
from zipfile import ZipFile
from shutil import move
from os import remove,mkdir
from datetime import datetime,timedelta
from errno import EEXIST
#-*- coding: utf-8 -*-

"""
El codigo se probaba en kevinator y en la base de datos, mejor conocida como base-chan.
Al ser computadoras distintas, el path donde se encuentran las dimensiones es distinto,
para agilizar el proceso de testeo, construccion y deployment se penso en guardar el path en variables,
de esta forma solo se tiene que modificar el path en las variables y no en todas partes.

En otro orden de asuntos, la dimension "WST" esta repetida en los estandar "GL" e "INV" segun la documentacion de oracle,
como este es un codigo sin ningun tipo de fisuras se penso usar el indice de las listas para comprobar el origen de la dimension,
por lo tanto y dependiendo de la compu donde te encuentres debes cambiar el path y los indices de esas dos dimensiones para usar el codigo.

    Path e indices actuales de kevinator!

        kspathstorage=("\\Users\\ksanchez\\Desktop\\DataBase\\storage") #\*.txt or *\.zip
        kspathdestino=("\\Users\\ksanchez\\Desktop\\DataBase\\destino")
        kspathbackup=("\\Users\\ksanchez\\Desktop\\DataBase\\backup")
        GL=[41:43]
        INV=[41:44]

    path e indices actuales de base-chan uwu desune~

        kspathstorage=("\\Users\\Administrator\\Desktop\\DimensionData\\Storage") #\*.txt or *\.zip
        kspathdestino=("\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\Basechan\\Station")
        kspathbackup=("\\Users\\Administrator\\Desktop\\DimensionData\\Backup")
        GL=[51:53]
        INV=[51:54]
"""

kspathstorage=("\\Users\\Administrator\\Desktop\\DimensionData\\Storage") #\*.txt or *\.zip
kspathdestino=("\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\Basechan\\Station")
kspathbackup=("\\Users\\Administrator\\Desktop\\DimensionData\\Backup")


fecha_actual= datetime.now()
diadelta=timedelta(days=1)

fecha_archivo_actual=datetime.strftime(fecha_actual,"%d-%m-%y")
fecha_archivo_ayer=fecha_actual-diadelta
fecha_archivo_ayer=datetime.strftime(fecha_archivo_ayer,"%d-%m-%y")



Archivoszip=glob(f"{kspathstorage}\*.zip")
for na in Archivoszip:
    archivo=ZipFile(na)
    texto=archivo.extractall(kspathstorage)
    archivo.close()
    try:
        move(na,kspathbackup)
    except:
        move(na,"\\Users\\Administrator\\Desktop\\DimensionData\\Backup1")

lista=glob(f"{kspathstorage}\*.txt")
for na in lista:
    texto=open(na)

    #Employee
    cadenaEMP=""
    cadenaEMPSHFT=""
    cadenaEMPSVC=""
    cadenaEMPDSC=""
    cadenaEMPTM=""
    cadenaEMPSLS=""
    cadenaEMPOTSLS=""
    #Fixed period
    cadenaFPSUM=""
    cadenaFPOT=""
    cadenaFPMI=""
    #General ledger
    cadenaSUM=""
    cadenaDSC=""
    cadenaSVC=""
    cadenaTND=""
    cadenaTAX=""
    cadenaOT=""
    cadenaGLC=""
    cadenaPIO=""
    cadenaMID=""
    cadenaMNPR=""
    cadenaCHDR=""
    cadenaCDTL=""
    cadenaCMI=""
    cadenaCSVC=""
    cadenaCTND=""
    cadenaCDSC=""
    cadenaCOTD=""
    cadenaCTAX=""
    cadenaCVAT=""
    cadenaFFD=""
    cadenaFFL=""
    cadenaCASH=""
    cadenaNONSLS=""
    cadenaCSHRSHFT=""
    cadenaCMB=""
    cadenaKDS=""
    cadenaOTD=""
    cadenaWST_GL=""
    #Inventory
    cadenaINV=""
    cadenaWST_I=""
    cadenaPO=""
    cadenaPODTL=""
    cadenaRCPT=""
    cadenaRCPTDTL=""
    cadenaXFER=""
    cadenaXFERDTL=""
    cadenaINVWST=""
    #Customer activity
    cadenaCUSACT=""
    #Location
    cadenaLOC=""
    #Payroll
    cadenaPAY=""
    cadenaTC=""
    cadenaTCADJ=""



    for reglon in texto:
        parte=reglon.split("|")

        if parte[0]=="EMPID":
            localEMP=parte[1]
            fechaEMP=parte[3]
        elif(parte[0]=="EMP" or parte[0]=="EMPSHFT" or parte[0]=="EMPSVC" or parte[0]=="EMPDSC"
        or parte[0]=="EMPTM" or parte[0]=="EMPOTSLS" or parte[0]=="EMPOTSLS"):
            parte.insert(1,fechaEMP)
            parte.insert(1,localEMP)

        elif parte[0]=="FPID":
            localFP=parte[1]
            fechaFP=parte[3]
        elif parte[0]=="FPSUM" or parte[0]=="FPOT" or parte[0]=="FPMI":
            parte.insert(1,fechaFP)
            parte.insert(1,localFP)

        elif parte[0]=="GLID":
            localGL=parte[1]
            fechaGL=parte[3]
        elif (parte[0]=="SUM" or parte[0]=="DSC" or parte[0]=="SVC" or parte[0]=="TND" 
        or parte[0]=="TAX" or parte[0]=="OT" or parte[0]=="GLC" or parte[0]=="PIO" 
        or parte[0]=="MID" or parte[0]=="MNPR" or parte[0]=="CHDR" or parte[0]=="CDTL" 
        or parte[0]=="CMI" or parte[0]=="CSVC" or parte[0]=="CTND" or parte[0]=="CDSC"
        or parte[0]=="COTD" or parte[0]=="CTAX" or parte[0]=="CVAT" or parte[0]=="FFD"
        or parte[0]=="FFL" or parte[0]=="CASH" or parte[0]=="NONSLS" or parte[0]=="CSHRSHFT"
        or parte[0]=="CMB" or parte[0]=="KDS" or parte[0]=="OTD" or parte[0]=="WST" and na[51:53]=="GL"):       #indiceGL
            parte.insert(1,fechaGL)
            parte.insert(1,localGL)    

        elif parte[0]=="INVID":
            localINV=parte[1]
            fechaINV=parte[3]
        elif (parte[0]=="INV" or parte[0]=="WST" and na[51:54]=="INV" or parte[0]=="PO" or parte[0]=="PODTL"     #indiceINV
        or parte[0]=="RCPT" or parte[0]=="RCPTDTL" or parte[0]=="XFER" or parte[0]=="XFERDTL"
        or parte[0]=="INVWST"):
            parte.insert(1,fechaINV)
            parte.insert(1,localINV)

        elif parte[0]=="CUSTID":
            localCUST=parte[1]
            fechaCUST=parte[3]
        elif parte[0]=="CUSACT":
            parte.insert(1,fechaCUST)
            parte.insert(1,localCUST)

        elif parte[0]=="LOCID":
            localLOC=parte[1]
            fechaLOC=parte[3]
        elif parte[0]=="LOC":
            parte.insert(1,fechaLOC)
            parte.insert(1,localLOC)

        elif parte[0]=="PAYID":
            localPAY=parte[1]
            fechaPAY=parte[3]
        elif parte[0]=="PAY" or parte[0]=="TC" or parte[0]=="TCADJ":
            parte.insert(1,fechaPAY)
            parte.insert(1,localPAY)

        else:
            file=open(f"{kspathdestino}\dimension_unknown.txt","a+")
            file.write(f"Se detecto la dimension desconocida {parte[0]} en el archivo {na}\n")
            file.close()



        if parte[0]=="EMP":
            cadenaEMP+=str("|".join(parte))
        elif parte[0]=="EMPSHFT":
            cadenaEMPSHFT+=str("|".join(parte)) 
        elif parte[0]=="EMPSVC":
            cadenaEMPSVC+=str("|".join(parte))
        elif parte[0]=="EMPDSC":
            cadenaEMPDSC+=str("|".join(parte))  
        elif parte[0]=="EMPTM":
            cadenaEMPTM+=str("|".join(parte))
        elif parte[0]=="EMPSLS":
            cadenaEMPSLS+=str("|".join(parte))             
        elif parte[0]=="EMPOTSLS":
            cadenaEMPOTSLS+=str("|".join(parte))

        elif parte[0]=="FPSUM":
            cadenaFPSUM+=str("|".join(parte))
        elif parte[0]=="FPOT":
            cadenaFPOT+=str("|".join(parte))
        elif parte[0]=="FPMI":
            cadenaFPMI+=str("|".join(parte))

        elif parte[0]=="SUM":
            cadenaSUM+=str("|".join(parte))
        elif parte[0]=="DSC":
            cadenaDSC+=str("|".join(parte))
        elif parte[0]=="SVC":
            cadenaSVC+=str("|".join(parte)) 
        elif parte[0]=="TND":
            cadenaTND+=str("|".join(parte))
        elif parte[0]=="TAX":
            cadenaTAX+=str("|".join(parte))
        elif parte[0]=="OT":
            cadenaOT+=str("|".join(parte))
        elif parte[0]=="GLC":
            cadenaGLC+=str("|".join(parte))
        elif parte[0]=="PIO":
            cadenaPIO+=str("|".join(parte))  
        elif parte[0]=="MID":
            cadenaMID+=str("|".join(parte))
        elif parte[0]=="MNPR":
            cadenaMNPR+=str("|".join(parte))
        elif parte[0]=="CHDR":
            cadenaCHDR+=str("|".join(parte))
        elif parte[0]=="CDTL":
            cadenaCDTL+=str("|".join(parte))
        elif parte[0]=="CMI":
            cadenaCMI+=str("|".join(parte))
        elif parte[0]=="CSVC":
            cadenaCSVC+=str("|".join(parte))
        elif parte[0]=="CTND":
            cadenaCTND+=str("|".join(parte)) 
        elif parte[0]=="CDSC":
            cadenaCDSC+=str("|".join(parte)) 
        elif parte[0]=="COTD":
            cadenaCOTD+=str("|".join(parte)) 
        elif parte[0]=="CTAX":
            cadenaCTAX+=str("|".join(parte)) 
        elif parte[0]=="CVAT":
            cadenaCVAT+=str("|".join(parte)) 
        elif parte[0]=="FFD":
            cadenaFFD+=str("|".join(parte)) 
        elif parte[0]=="FFL":
            cadenaFFL+=str("|".join(parte))
        elif parte[0]=="CASH":
            cadenaCASH+=str("|".join(parte)) 
        elif parte[0]=="NONSLS":
            cadenaNONSLS+=str("|".join(parte)) 
        elif parte[0]=="CSHRSHFT":
            cadenaCSHRSHFT+=str("|".join(parte)) 
        elif parte[0]=="CMB":
            cadenaCMB+=str("|".join(parte)) 
        elif parte[0]=="KDS":
            cadenaKDS+=str("|".join(parte)) 
        elif parte[0]=="OTD":
            cadenaOTD+=str("|".join(parte)) 
        elif parte[0]=="WST" and na[51:53]=="GL":      #indiceGL
            cadenaWST_GL+=str("|".join(parte))  

        elif parte[0]=="INV":
            cadenaINV+=str("|".join(parte)) 
        elif parte[0]=="WST" and na[51:54]=="INV":      #indiceINV
            cadenaWST_I+=str("|".join(parte))
        elif parte[0]=="PO":
            cadenaPO+=str("|".join(parte)) 
        elif parte[0]=="PODTL":
            cadenaPODTL+=str("|".join(parte)) 
        elif parte[0]=="RCPT":
            cadenaRCPT+=str("|".join(parte)) 
        elif parte[0]=="RCPTDTL":
            cadenaRCPTDTL+=str("|".join(parte)) 
        elif parte[0]=="XFER":
            cadenaXFER+=str("|".join(parte)) 
        elif parte[0]=="XFERDTL":
            cadenaXFERDTL+=str("|".join(parte)) 
        elif parte[0]=="INVWST":
            cadenaINVWST+=str("|".join(parte)) 

        elif parte[0]=="CUSACT":
            cadenaCUSACT+=str("|".join(parte)) 

        elif parte[0]=="LOC":
            cadenaLOC+=str("|".join(parte))

        elif parte[0]=="PAY":
            cadenaPAY+=str("|".join(parte))
        elif parte[0]=="TC":
            cadenaTC+=str("|".join(parte)) 
        elif parte[0]=="TCADJ":
            cadenaTCADJ+=str("|".join(parte)) 



    if cadenaEMP != "":
        file=open(str(f"{kspathdestino}\\EMP_{fecha_archivo_ayer}_EMP.csv"),"a+")
        file.write(cadenaEMP)
        file.close()
    if cadenaEMPSHFT != "":
        file=open(str(f"{kspathdestino}\\EMP_{fecha_archivo_ayer}_EMPSHFT.csv"),"a+")
        file.write(cadenaEMPSHFT)
        file.close()
    if cadenaEMPSVC != "":
        file=open(str(f"{kspathdestino}\\EMP_{fecha_archivo_ayer}_EMPSVC.csv"),"a+")
        file.write(cadenaEMPSVC)
        file.close()
    if cadenaEMPDSC != "":
        file=open(str(f"{kspathdestino}\\EMP_{fecha_archivo_ayer}_EMPDSC.csv"),"a+")
        file.write(cadenaEMPDSC)
        file.close()
    if cadenaEMPTM != "":
        file=open(str(f"{kspathdestino}\\EMP_{fecha_archivo_ayer}_EMPTM.csv"),"a+")
        file.write(cadenaEMPTM)
        file.close()
    if cadenaEMPSLS != "":
        file=open(str(f"{kspathdestino}\\EMP_{fecha_archivo_ayer}_EMPSLS.csv"),"a+")
        file.write(cadenaEMPSLS)
        file.close()
    if cadenaEMPOTSLS != "":
        file=open(str(f"{kspathdestino}\\EMP_{fecha_archivo_ayer}_EMPOTSLS.csv"),"a+")
        file.write(cadenaEMPOTSLS)
        file.close()

    if cadenaFPSUM != "":
        file=open(f"{kspathdestino}\\FP_{fecha_archivo_ayer}_FPSUM.csv","a+")
        file.write(cadenaFPSUM)
        file.close()
    if cadenaFPOT != "":
        file=open(f"{kspathdestino}\\FP_{fecha_archivo_ayer}_FPOT.csv","a+")
        file.write(cadenaFPOT)
        file.close()
    if cadenaFPMI != "":
        file=open(f"{kspathdestino}\\FP_{fecha_archivo_ayer}_FPMI.csv","a+")
        file.write(cadenaFPMI)
        file.close()

    if cadenaSUM != "":
        file=open(f"{kspathdestino}\\GL_{fecha_archivo_ayer}_SUM.csv","a+")
        file.write(cadenaSUM)
        file.close()
    if cadenaDSC != "":
        file=open(f"{kspathdestino}\\GL_{fecha_archivo_ayer}_DSC.csv","a+")
        file.write(cadenaDSC)
        file.close()
    if cadenaSVC != "":
        file=open(f"{kspathdestino}\\GL_{fecha_archivo_ayer}_SVC.csv","a+")
        file.write(cadenaSVC)
        file.close()
    if cadenaTND != "":
        file=open(f"{kspathdestino}\\GL_{fecha_archivo_ayer}_TND.csv","a+")
        file.write(cadenaTND)
        file.close()
    if cadenaTAX != "":
        file=open(f"{kspathdestino}\\GL_{fecha_archivo_ayer}_TAX.csv","a+")
        file.write(cadenaTAX)
        file.close()
    if cadenaOT != "":
        file=open(f"{kspathdestino}\\GL_{fecha_archivo_ayer}_OT.csv","a+")
        file.write(cadenaOT)
        file.close()
    if cadenaGLC != "":
        file=open(f"{kspathdestino}\\GL_{fecha_archivo_ayer}_GLC.csv","a+")
        file.write(cadenaGLC)
        file.close()
    if cadenaPIO != "":
        file=open(f"{kspathdestino}\\GL_{fecha_archivo_ayer}_PIO.csv","a+")
        file.write(cadenaPIO)
        file.close()
    if cadenaMID != "":
        file=open(f"{kspathdestino}\\GL_{fecha_archivo_ayer}_MID.csv","a+")
        file.write(cadenaMID)
        file.close()
    if cadenaMNPR != "":
        file=open(f"{kspathdestino}\\GL_{fecha_archivo_ayer}_MNPR.csv","a+")
        file.write(cadenaMNPR)
        file.close()
    if cadenaCHDR != "":
        file=open(f"{kspathdestino}\\GL_{fecha_archivo_ayer}_CHDR.csv","a+")
        file.write(cadenaCHDR)
        file.close()
    if cadenaCDTL != "":
        file=open(f"{kspathdestino}\\GL_{fecha_archivo_ayer}_CDTL.csv","a+")
        file.write(cadenaCDTL)
        file.close()
    if cadenaCMI != "":
        file=open(f"{kspathdestino}\\GL_{fecha_archivo_ayer}_CMI.csv","a+")
        file.write(cadenaCMI)
        file.close()
    if cadenaCSVC != "":
        file=open(f"{kspathdestino}\\GL_{fecha_archivo_ayer}_CSVC.csv","a+")
        file.write(cadenaCSVC)
        file.close()
    if cadenaCTND != "":
        file=open(f"{kspathdestino}\\GL_{fecha_archivo_ayer}_CTND.csv","a+")
        file.write(cadenaCTND)
        file.close()
    if cadenaCDSC != "":
        file=open(f"{kspathdestino}\\GL_{fecha_archivo_ayer}_CDSC.csv","a+")
        file.write(cadenaCDSC)
        file.close()
    if cadenaCOTD != "":
        file=open(f"{kspathdestino}\\GL_{fecha_archivo_ayer}_COTD.csv","a+")
        file.write(cadenaCOTD)
        file.close()
    if cadenaCTAX != "":
        file=open(f"{kspathdestino}\\GL_{fecha_archivo_ayer}_CTAX.csv","a+")
        file.write(cadenaCTAX)
        file.close()
    if cadenaCVAT != "":
        file=open(f"{kspathdestino}\\GL_{fecha_archivo_ayer}_CVAT.csv","a+")
        file.write(cadenaCVAT)
        file.close()
    if cadenaFFD != "":
        file=open(f"{kspathdestino}\\GL_{fecha_archivo_ayer}_FFD.csv","a+")
        file.write(cadenaFFD)
        file.close()
    if cadenaFFL != "":
        file=open(f"{kspathdestino}\\GL_{fecha_archivo_ayer}_FFL.csv","a+")
        file.write(cadenaFFL)
        file.close()
    if cadenaCASH != "":
        file=open(f"{kspathdestino}\\GL_{fecha_archivo_ayer}_CASH.csv","a+")
        file.write(cadenaCASH)
        file.close()
    if cadenaNONSLS != "":
        file=open(f"{kspathdestino}\\GL_{fecha_archivo_ayer}_NONSLS.csv","a+")
        file.write(cadenaNONSLS)
        file.close()
    if cadenaCSHRSHFT != "":
        file=open(f"{kspathdestino}\\GL_{fecha_archivo_ayer}_CSHRSHFT.csv","a+")
        file.write(cadenaCSHRSHFT)
        file.close()
    if cadenaCMB != "":
        file=open(f"{kspathdestino}\\GL_{fecha_archivo_ayer}_CMB.csv","a+")
        file.write(cadenaCMB)
        file.close()
    if cadenaKDS != "":
        file=open(f"{kspathdestino}\\GL_{fecha_archivo_ayer}_KDS.csv","a+")
        file.write(cadenaKDS)
        file.close()
    if cadenaOTD != "":
        file=open(f"{kspathdestino}\\GL_{fecha_archivo_ayer}_OTD.csv","a+")
        file.write(cadenaOTD)
        file.close()
    if cadenaWST_GL != "":
        file=open(f"{kspathdestino}\\GL_{fecha_archivo_ayer}_WST.csv","a+")
        file.write(cadenaWST_GL)
        file.close()

    if cadenaINV != "":
        file=open(f"{kspathdestino}\\INV_{fecha_archivo_ayer}_INV.csv","a+")
        file.write(cadenaINV)
        file.close()
    if cadenaWST_I != "":
        file=open(f"{kspathdestino}\\INV_{fecha_archivo_ayer}_WST.csv","a+")
        file.write(cadenaWST_I)
        file.close()
    if cadenaPO != "":
        file=open(f"{kspathdestino}\\INV_{fecha_archivo_ayer}_PO.csv","a+")
        file.write(cadenaPO)
        file.close()
    if cadenaPODTL != "":
        file=open(f"{kspathdestino}\\INV_{fecha_archivo_ayer}_PODTL.csv","a+")
        file.write(cadenaPODTL)
        file.close()
    if cadenaRCPT != "":
        file=open(f"{kspathdestino}\\INV_{fecha_archivo_ayer}_RCPT.csv","a+")
        file.write(cadenaRCPT)
        file.close()
    if cadenaRCPTDTL != "":
        file=open(f"{kspathdestino}\\INV_{fecha_archivo_ayer}_RCPTDTL.csv","a+")
        file.write(cadenaRCPTDTL)
        file.close()
    if cadenaXFER != "":
        file=open(f"{kspathdestino}\\INV_{fecha_archivo_ayer}_XFER.csv","a+")
        file.write(cadenaXFER)
        file.close()
    if cadenaXFERDTL != "":
        file=open(f"{kspathdestino}\\INV_{fecha_archivo_ayer}_XFERDTL.csv","a+")
        file.write(cadenaXFERDTL)
        file.close()
    if cadenaINVWST != "":
        file=open(f"{kspathdestino}\\INV_{fecha_archivo_ayer}_INVWST.csv","a+")
        file.write(cadenaINVWST)
        file.close()

    if cadenaCUSACT != "":
        file=open(f"{kspathdestino}\\CUSACT_{fecha_archivo_ayer}_CUSACT.csv","a+")
        file.write(cadenaCUSACT)
        file.close()

    if cadenaLOC != "":
        file=open(f"{kspathdestino}\\LOC_{fecha_archivo_actual}_LOC.csv","a+")
        file.write(cadenaLOC)
        file.close()

    if cadenaPAY != "":
        file=open(f"{kspathdestino}\\PAY_{fecha_archivo_ayer}_PAY.csv","a+")
        file.write(cadenaPAY)
        file.close()
    if cadenaTC != "":
        file=open(f"{kspathdestino}\\PAY_{fecha_archivo_ayer}_TC.csv","a+")
        file.write(cadenaTC)
        file.close()
    if cadenaTCADJ != "":
        file=open(f"{kspathdestino}\\PAY_{fecha_archivo_ayer}_TCADJ.csv","a+")
        file.write(cadenaTCADJ)
        file.close()


    texto.close()
    remove(na)
