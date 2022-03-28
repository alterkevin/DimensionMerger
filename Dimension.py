from glob import glob
from zipfile import ZipFile
from shutil import move
from os import remove
#-*- coding: utf-8 -*-

#\\Users\\Administrador\\Desktop\\DimensionData\\Datos\\standard.export
#\\Users\\Administrador\\Desktop\\DimensionData\\Destino\\d.standard.merged
#\\Users\\ksanchez\\Desktop\\DataBase\\prueba\*.txt
#\\Users\\ksanchez\\Desktop\\DataBase\\destino2\

Archivoszip=glob("\\Users\\ksanchez\\Desktop\\DataBase\\prueba\*.zip")
for na in Archivoszip:
    archivo=ZipFile(na)
    texto=archivo.extractall("\\Users\\ksanchez\\Desktop\\DataBase\\prueba")
    archivo.close()
    move(na,"\\Users\\ksanchez\\Desktop\\DataBase\\backup")


lista=glob("\\Users\\ksanchez\\Desktop\\DataBase\\prueba\*.txt")
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
    cadenaWST=""
    #Inventory
    cadenaINV=""
    cadenaWST=""
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
        or parte[0]=="CMB" or parte[0]=="KDS" or parte[0]=="OTD" or parte[0]=="WST"):
            parte.insert(1,fechaGL)
            parte.insert(1,localGL)    

        elif parte[0]=="INVID":
            localINV=parte[1]
            fechaINV=parte[3]
        elif (parte[0]=="INV" or parte[0]=="WST" or parte[0]=="PO" or parte[0]=="PODTL"
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
            file=open("\\Users\\ksanchez\\Desktop\\DataBase\\destino2\dimension_unknown.txt","a+")
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
        elif parte[0]=="WST":
            cadenaWST+=str("|".join(parte))  

        elif parte[0]=="INV":
            cadenaINV+=str("|".join(parte)) 
        elif parte[0]=="WST":
            cadenaWST+=str("|".join(parte))
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


    file=open("\\Users\\ksanchez\\Desktop\\DataBase\\destino2\Employee_standard_EMP.csv","a+")
    file.write(cadenaEMP)
    file.close()
    file=open("\\Users\\ksanchez\\Desktop\\DataBase\\destino2\Employee_standard_EMPSHFT.csv","a+")
    file.write(cadenaEMPSHFT)
    file.close()
    file=open("\\Users\\ksanchez\\Desktop\\DataBase\\destino2\Employee_standard_EMPSVC.csv","a+")
    file.write(cadenaEMPSVC)
    file.close()
    file=open("\\Users\\ksanchez\\Desktop\\DataBase\\destino2\Employee_standard_EMPDSC.csv","a+")
    file.write(cadenaEMPDSC)
    file.close()
    file=open("\\Users\\ksanchez\\Desktop\\DataBase\\destino2\Employee_standard_EMPTM.csv","a+")
    file.write(cadenaEMPTM)
    file.close()
    file=open("\\Users\\ksanchez\\Desktop\\DataBase\\destino2\Employee_standard_EMPSLS.csv","a+")
    file.write(cadenaEMPSLS)
    file.close()
    file=open("\\Users\\ksanchez\\Desktop\\DataBase\\destino2\Employee_standard_EMPOTSLS.csv","a+")
    file.write(cadenaEMPOTSLS)
    file.close()

    file=open("\\Users\\ksanchez\\Desktop\\DataBase\\destino2\FixedPeriod_standard_FPSUM.csv","a+")
    file.write(cadenaFPSUM)
    file.close()
    file=open("\\Users\\ksanchez\\Desktop\\DataBase\\destino2\FixedPeriod_standard_PFOT.csv","a+")
    file.write(cadenaFPOT)
    file.close()
    file=open("\\Users\\ksanchez\\Desktop\\DataBase\\destino2\FixedPeriod_standard_FPMI.csv","a+")
    file.write(cadenaFPMI)
    file.close()

    file=open("\\Users\\ksanchez\\Desktop\\DataBase\\destino2\GeneralLedger_standard_SUM.csv","a+")
    file.write(cadenaSUM)
    file.close()
    file=open("\\Users\\ksanchez\\Desktop\\DataBase\\destino2\GeneralLedger_standard_DSC.csv","a+")
    file.write(cadenaDSC)
    file.close()
    file=open("\\Users\\ksanchez\\Desktop\\DataBase\\destino2\GeneralLedger_standard_SVC.csv","a+")
    file.write(cadenaSVC)
    file.close()
    file=open("\\Users\\ksanchez\\Desktop\\DataBase\\destino2\GeneralLedger_standard_TND.csv","a+")
    file.write(cadenaTND)
    file.close()
    file=open("\\Users\\ksanchez\\Desktop\\DataBase\\destino2\GeneralLedger_standard_TAX.csv","a+")
    file.write(cadenaTAX)
    file.close()
    file=open("\\Users\\ksanchez\\Desktop\\DataBase\\destino2\GeneralLedger_standard_OT.csv","a+")
    file.write(cadenaOT)
    file.close()
    file=open("\\Users\\ksanchez\\Desktop\\DataBase\\destino2\GeneralLedger_standard_GLC.csv","a+")
    file.write(cadenaGLC)
    file.close()
    file=open("\\Users\\ksanchez\\Desktop\\DataBase\\destino2\GeneralLedger_standard_PIO.csv","a+")
    file.write(cadenaPIO)
    file.close()
    file=open("\\Users\\ksanchez\\Desktop\\DataBase\\destino2\GeneralLedger_standard_MID.csv","a+")
    file.write(cadenaMID)
    file.close()
    file=open("\\Users\\ksanchez\\Desktop\\DataBase\\destino2\GeneralLedger_standard_MNPR.csv","a+")
    file.write(cadenaMNPR)
    file.close()
    file=open("\\Users\\ksanchez\\Desktop\\DataBase\\destino2\GeneralLedger_standard_CHDR.csv","a+")
    file.write(cadenaCHDR)
    file.close()
    file=open("\\Users\\ksanchez\\Desktop\\DataBase\\destino2\GeneralLedger_standard_CDTL.csv","a+")
    file.write(cadenaCDTL)
    file.close()
    file=open("\\Users\\ksanchez\\Desktop\\DataBase\\destino2\GeneralLedger_standard_CMI.csv","a+")
    file.write(cadenaCMI)
    file.close()
    file=open("\\Users\\ksanchez\\Desktop\\DataBase\\destino2\GeneralLedger_standard_CSVC.csv","a+")
    file.write(cadenaCSVC)
    file.close()
    file=open("\\Users\\ksanchez\\Desktop\\DataBase\\destino2\GeneralLedger_standard_CTND.csv","a+")
    file.write(cadenaCTND)
    file.close()
    file=open("\\Users\\ksanchez\\Desktop\\DataBase\\destino2\GeneralLedger_standard_CDSC.csv","a+")
    file.write(cadenaCDSC)
    file.close()
    file=open("\\Users\\ksanchez\\Desktop\\DataBase\\destino2\GeneralLedger_standard_COTD.csv","a+")
    file.write(cadenaCOTD)
    file.close()
    file=open("\\Users\\ksanchez\\Desktop\\DataBase\\destino2\GeneralLedger_standard_CTAX.csv","a+")
    file.write(cadenaCTAX)
    file.close()
    file=open("\\Users\\ksanchez\\Desktop\\DataBase\\destino2\GeneralLedger_standard_CVAT.csv","a+")
    file.write(cadenaCVAT)
    file.close()
    file=open("\\Users\\ksanchez\\Desktop\\DataBase\\destino2\GeneralLedger_standard_FFD.csv","a+")
    file.write(cadenaFFD)
    file.close()
    file=open("\\Users\\ksanchez\\Desktop\\DataBase\\destino2\GeneralLedger_standard_FFL.csv","a+")
    file.write(cadenaFFL)
    file.close()
    file=open("\\Users\\ksanchez\\Desktop\\DataBase\\destino2\GeneralLedger_standard_CASH.csv","a+")
    file.write(cadenaCASH)
    file.close()
    file=open("\\Users\\ksanchez\\Desktop\\DataBase\\destino2\GeneralLedger_standard_NONSLS.csv","a+")
    file.write(cadenaNONSLS)
    file.close()
    file=open("\\Users\\ksanchez\\Desktop\\DataBase\\destino2\GeneralLedger_standard_CHSRSHFT.csv","a+")
    file.write(cadenaCSHRSHFT)
    file.close()
    file=open("\\Users\\ksanchez\\Desktop\\DataBase\\destino2\GeneralLedger_standard_CMB.csv","a+")
    file.write(cadenaCMB)
    file.close()
    file=open("\\Users\\ksanchez\\Desktop\\DataBase\\destino2\GeneralLedger_standard_KDS.csv","a+")
    file.write(cadenaKDS)
    file.close()
    file=open("\\Users\\ksanchez\\Desktop\\DataBase\\destino2\GeneralLedger_standard_OTD.csv","a+")
    file.write(cadenaOTD)
    file.close()
    file=open("\\Users\\ksanchez\\Desktop\\DataBase\\destino2\GeneralLedger_standard_WST.csv","a+")
    file.write(cadenaWST)
    file.close()

    file=open("\\Users\\ksanchez\\Desktop\\DataBase\\destino2\Inventory_standard_INV.csv","a+")
    file.write(cadenaINV)
    file.close()
    file=open("\\Users\\ksanchez\\Desktop\\DataBase\\destino2\Inventory_standard_WST.csv","a+")
    file.write(cadenaWST)
    file.close()
    file=open("\\Users\\ksanchez\\Desktop\\DataBase\\destino2\Inventory_standard_PO.csv","a+")
    file.write(cadenaPO)
    file.close()
    file=open("\\Users\\ksanchez\\Desktop\\DataBase\\destino2\Inventory_standard_PODTL.csv","a+")
    file.write(cadenaPODTL)
    file.close()
    file=open("\\Users\\ksanchez\\Desktop\\DataBase\\destino2\Inventory_standard_RCPT.csv","a+")
    file.write(cadenaRCPT)
    file.close()
    file=open("\\Users\\ksanchez\\Desktop\\DataBase\\destino2\Inventory_standard_RCPTDTL.csv","a+")
    file.write(cadenaRCPTDTL)
    file.close()
    file=open("\\Users\\ksanchez\\Desktop\\DataBase\\destino2\Inventory_standard_XFER.csv","a+")
    file.write(cadenaXFER)
    file.close()
    file=open("\\Users\\ksanchez\\Desktop\\DataBase\\destino2\Inventory_standard_XFERDTL.csv","a+")
    file.write(cadenaXFERDTL)
    file.close()
    file=open("\\Users\\ksanchez\\Desktop\\DataBase\\destino2\Inventory_standard_INVWST.csv","a+")
    file.write(cadenaINVWST)
    file.close()

    file=open("\\Users\\ksanchez\\Desktop\\DataBase\\destino2\CustomerActivity_standard_CUSACT.csv","a+")
    file.write(cadenaCUSACT)
    file.close()

    file=open("\\Users\\ksanchez\\Desktop\\DataBase\\destino2\Location_standard_LOC.csv","a+")
    file.write(cadenaLOC)
    file.close()

    file=open("\\Users\\ksanchez\\Desktop\\DataBase\\destino2\Payroll_standard_PAY.csv","a+")
    file.write(cadenaPAY)
    file.close()
    file=open("\\Users\\ksanchez\\Desktop\\DataBase\\destino2\Payroll_standard_TC.csv","a+")
    file.write(cadenaTC)
    file.close()
    file=open("\\Users\\ksanchez\\Desktop\\DataBase\\destino2\Payroll_standard_TCADJ.csv","a+")
    file.write(cadenaTCADJ)
    file.close()


    texto.close()
    remove(na)
