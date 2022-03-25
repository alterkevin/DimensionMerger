from glob import glob
from zipfile import ZipFile
#-*- coding: utf-8 -*-

#\\Users\\Administrador\\Desktop\\DimensionData\\Datos\\standard.export
#\\Users\\Administrador\\Desktop\\DimensionData\\Destino\\d.standard.merged
#\\Users\\ksanchez\\Desktop\\DataBase\\prueba\*.txt
#\\Users\\ksanchez\\Desktop\\DataBase\\destino2\

Archivoszip=glob("\\Users\\ksanchez\\Desktop\\DataBase\\prueba\*.zip")
for na in Archivoszip:
    archivo=ZipFile(na)
    texto=archivo.extractall("\\Users\\ksanchez\\Desktop\\DataBase\\prueba")

lista=glob("\\Users\\ksanchez\\Desktop\\DataBase\\prueba\*.txt")
for na in lista:

    cadena1=""
    cadena2=""
    cadena3=""
    cadena4=""
    cadena5=""
    cadena6=""
    cadena7=""
    cadena8=""
    cadena9=""
    cadena10=""
    cadena11=""
    cadena12=""
    cadena13=""
    cadena14=""
    cadena15=""
    cadena16=""
    cadena17=""
    cadena18=""
    cadena19=""
    cadena20=""
    
    for reglon in open(na):
        parte=reglon.split("|")

        if parte[0]=="EMPID":
            localEMP=parte[1]
            fechaEMP=parte[3]
        elif parte[0]=="EMP" or parte[0]=="EMPDSC" or parte[0]=="EMPTM" or parte[0]=="EMPOTSLS":
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
        elif (parte[0]=="SUM" or parte[0]=="DSC" or parte[0]=="TND" or parte[0]=="TAX" 
        or parte[0]=="OT" or parte[0]=="MID" or parte[0]=="MNPR" or parte[0]=="CHDR"
        or parte[0]=="NONSLS" or parte[0]=="CMB" or parte[0]=="OTD"):
                parte.insert(1,fechaGL)
                parte.insert(1,localGL)    
        elif parte[0]=="INVID":
            localINV=parte[1]
            fechaINV=parte[3]
#        elif parte[0]=="EMPDSC" or parte[0]=="EMPTM" or parte[0]=="EMPOTSLS":
#                parte.insert(1,fechaINV)
#                parte.insert(1,localINV)
        elif parte[0]=="LOCID":
            localLOC=parte[1]
            fechaLOC=parte[3]
        elif parte[0]=="LOC":
                parte.insert(1,fechaLOC)
                parte.insert(1,localLOC)
        elif parte[0]=="PAYID":
            localPAY=parte[1]
            fechaPAY=parte[3]
        elif parte[0]=="PAY":
                parte.insert(1,fechaPAY)
                parte.insert(1,localPAY)
        else:
            file=open("\\Users\\ksanchez\\Desktop\\DataBase\\destino2\dimension_unknown.txt","a+")
            file.write(f"Se detecto la dimension desconocida {parte[0]} en el archivo {na}\n")
            file.close()

        if parte[0]=="EMPDSC":
            cadena1+=str("|".join(parte))
        elif parte[0]=="EMPTM":
            cadena2+=str("|".join(parte))            
        elif parte[0]=="EMPOTSLS":
            cadena3+=str("|".join(parte))
        elif parte[0]=="FPSUM":
            cadena4+=str("|".join(parte))
        elif parte[0]=="FPOT":
            cadena5+=str("|".join(parte))
        elif parte[0]=="FPMI":
            cadena6+=str("|".join(parte))
        elif parte[0]=="SUM":
            cadena7+=str("|".join(parte))
        elif parte[0]=="DSC":
            cadena8+=str("|".join(parte))
        elif parte[0]=="TND":
            cadena9+=str("|".join(parte))
        elif parte[0]=="TAX":
            cadena10+=str("|".join(parte))
        elif parte[0]=="OT":
            cadena11+=str("|".join(parte))
        elif parte[0]=="MID":
            cadena12+=str("|".join(parte))
        elif parte[0]=="MNPR":
            cadena13+=str("|".join(parte))
        elif parte[0]=="CHDR":
            cadena14+=str("|".join(parte))
        elif parte[0]=="NONSLS":
            cadena15+=str("|".join(parte))
        elif parte[0]=="CMB":
            cadena16+=str("|".join(parte))
        elif parte[0]=="OTD":
            cadena17+=str("|".join(parte))
        elif parte[0]=="LOC":
            cadena18+=str("|".join(parte))
        elif parte[0]=="PAY":
            cadena19+=str("|".join(parte))
        elif parte[0]=="EMP":
            cadena20+=str("|".join(parte))

    file=open("\\Users\\ksanchez\\Desktop\\DataBase\\destino2\d_standard_EMPDSC.csv","a+")
    file.write(cadena1)
    file.close()
    file=open("\\Users\\ksanchez\\Desktop\\DataBase\\destino2\d_standard_EMPTM.csv","a+")
    file.write(cadena2)
    file.close()
    file=open("\\Users\\ksanchez\\Desktop\\DataBase\\destino2\d_standard_EMPOTSLS.csv","a+")
    file.write(cadena3)
    file.close()
    file=open("\\Users\\ksanchez\\Desktop\\DataBase\\destino2\d_standard_FPSUM.csv","a+")
    file.write(cadena4)
    file.close()
    file=open("\\Users\\ksanchez\\Desktop\\DataBase\\destino2\d_standard_PFOT.csv","a+")
    file.write(cadena5)
    file.close()
    file=open("\\Users\\ksanchez\\Desktop\\DataBase\\destino2\d_standard_FPMI.csv","a+")
    file.write(cadena6)
    file.close()
    file=open("\\Users\\ksanchez\\Desktop\\DataBase\\destino2\d_standard_SUM.csv","a+")
    file.write(cadena7)
    file.close()
    file=open("\\Users\\ksanchez\\Desktop\\DataBase\\destino2\d_standard_DSC.csv","a+")
    file.write(cadena8)
    file.close()
    file=open("\\Users\\ksanchez\\Desktop\\DataBase\\destino2\d_standard_TND.csv","a+")
    file.write(cadena9)
    file.close()
    file=open("\\Users\\ksanchez\\Desktop\\DataBase\\destino2\d_standard_TAX.csv","a+")
    file.write(cadena10)
    file.close()
    file=open("\\Users\\ksanchez\\Desktop\\DataBase\\destino2\d_standard_OT.csv","a+")
    file.write(cadena11)
    file.close()
    file=open("\\Users\\ksanchez\\Desktop\\DataBase\\destino2\d_standard_MID.csv","a+")
    file.write(cadena12)
    file.close()
    file=open("\\Users\\ksanchez\\Desktop\\DataBase\\destino2\d_standard_MNPR.csv","a+")
    file.write(cadena13)
    file.close()
    file=open("\\Users\\ksanchez\\Desktop\\DataBase\\destino2\d_standard_CHDR.csv","a+")
    file.write(cadena14)
    file.close()
    file=open("\\Users\\ksanchez\\Desktop\\DataBase\\destino2\d_standard_NONSLS.csv","a+")
    file.write(cadena15)
    file.close()
    file=open("\\Users\\ksanchez\\Desktop\\DataBase\\destino2\d_standard_CMB.csv","a+")
    file.write(cadena16)
    file.close()
    file=open("\\Users\\ksanchez\\Desktop\\DataBase\\destino2\d_standard_OTD.csv","a+")
    file.write(cadena17)
    file.close()
    file=open("\\Users\\ksanchez\\Desktop\\DataBase\\destino2\d_standard_LOC.csv","a+")
    file.write(cadena18)
    file.close()
    file=open("\\Users\\ksanchez\\Desktop\\DataBase\\destino2\d_standard_PAY.csv","a+")
    file.write(cadena19)
    file.close()