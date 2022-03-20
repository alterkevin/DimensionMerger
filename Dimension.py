import glob
import shutil

#####standard.Employee_LPQ

listaEMP=glob.glob("\\Users\\ksanchez\\Desktop\\DataBase\\prueba\*")

for na in listaEMP:
    cadenaEMP1=""
    cadenaEMP2=""
    cadenaEMP3=""

    for dato in open(na):
        parteEMP=dato.split("|")
    #    print(parteEMP)
    #    print(parteEMP[0])
        if parteEMP[0]=="EMPID":
            v1=parteEMP[1]
            v2=parteEMP[3]
    #        print(v1)
    #        print(v2)
        if parteEMP[0]!="EMPID":
            parteEMP.insert(1,v2)
            parteEMP.insert(1,v1)
    #    print(parteEMP)
        v3=[z1 for z1 in parteEMP if parteEMP[0]=="EMPDSC"]
        v4=[z2 for z2 in parteEMP if parteEMP[0]=="EMPTM"]
        v5=[z3 for z3 in parteEMP if parteEMP[0]=="EMPOTSLS"]
    #    print(V5)
        for x in v3:
            if x == []:
                v3.remove(x)
            d1=", ".join(v3)
            for x1 in d1:
                cadenaEMP1 += str(x1)

        for y in v4:
            if y == []:
                v4.remove(y)
            d2=", ".join(v4)
            for x2 in d2:
                cadenaEMP2 += str(x2)

        for z in v5:
            if z == []:
                v5.remove(z)
            d3=", ".join(v5)
            for x3 in d3:
                cadenaEMP3 += str(x3)
    
    f1=open(f"{na}_EMPDSC.txt","w")
    f1.write(cadenaEMP1)
    f1.close()
    shutil.move(f"{na}_EMPDSC.txt","\\Users\\ksanchez\\Desktop\\DataBase\\Codigo\\destino",copy_function=shutil.copy)

    f2=open(f"{na}_EMPTM.txt","w")
    f2.write(cadenaEMP2)
    f2.close()
    shutil.move(f"{na}_EMPTM.txt","\\Users\\ksanchez\\Desktop\\DataBase\\Codigo\\destino",copy_function=shutil.copy)
    
    f3=open(f"{na}_EMPOTSLS.txt","w")
    f3.write(cadenaEMP3)
    f3.close()
    shutil.move(f"{na}_EMPOTSLS.txt","\\Users\\ksanchez\\Desktop\\DataBase\\Codigo\\destino",copy_function=shutil.copy)

#####standard.FixedPeriod_LPQ

listaFP=glob.glob("\\Users\\ksanchez\\Desktop\\DataBase\\prueba\*")

for na in listaFP:
    cadenaFP1=""
    cadenaFP2=""
    cadenaFP3=""

    for dato in open(na):
        parteFP=dato.split("|")
    #    print(parteFP)
    #    print(parteFP[0])
        if parteFP[0]=="FPID":
            v6=parteFP[1]
            v7=parteFP[3]
    #        print(v6)
    #        print(v7)
        if parteFP[0]!="FPID":
            parteFP.insert(1,v7)
            parteFP.insert(1,v6)
    #    print(parteFP)
        v8=[z1 for z1 in parteFP if parteFP[0]=="FPSUM"]
        v9=[z2 for z2 in parteFP if parteFP[0]=="FPOT"]
        v10=[z3 for z3 in parteFP if parteFP[0]=="FPMI"]
    #    print(v10)
        for x in v8:
            if x == []:
                v8.remove(x)
            d4=", ".join(v8)
            for x4 in d4:
                cadenaFP1 += str(x1)

        for y in v9:
            if y == []:
                v9.remove(y)
            d5=", ".join(v9)
            for x5 in d5:
                cadenaFP2 += str(x5)

        for z in v10:
            if z == []:
                v10.remove(z)
            d6=", ".join(v10)
            for x6 in d6:
                cadenaFP3 += str(x6)
        
    #print(cadenaFP1)
    #'C:\\Users\\ksanchez\\Desktop\\DataBase\\Codigo\\destino\\'  
    
    f4=open(f"{na}_FPSUM.txt","w")
    f4.write(cadenaFP1)
    f4.close()
    shutil.move(f"{na}_FPSUM.txt","\\Users\\ksanchez\\Desktop\\DataBase\\Codigo\\destino",copy_function=shutil.copy)

    f5=open(f"{na}_FPOT.txt","w")
    f5.write(cadenaFP2)
    f5.close()
    shutil.move(f"{na}_FPOT.txt","\\Users\\ksanchez\\Desktop\\DataBase\\Codigo\\destino",copy_function=shutil.copy)
    
    f6=open(f"{na}_FPMI.txt","w")
    f6.write(cadenaFP3)
    f6.close()
    shutil.move(f"{na}_FPMI.txt","\\Users\\ksanchez\\Desktop\\DataBase\\Codigo\\destino",copy_function=shutil.copy)

#####standard.GeneralLedger_LPQ

listaGL=glob.glob("\\Users\\ksanchez\\Desktop\\DataBase\\prueba\*")

for na in listaGL:
    cadenaGL1=""
    cadenaGL2=""
    cadenaGL3=""
    cadenaGL4=""
    cadenaGL5=""
    cadenaGL6=""
    cadenaGL7=""
    cadenaGL8=""
    cadenaGL9=""
    cadenaGL10=""
    cadenaGL11=""

    for dato in open(na):
        parteGL=dato.split("|")
    #    print(parteGL)
    #    print(parteGL[0])
        if parteGL[0]=="GLID":
            v11=parteGL[1]
            v12=parteGL[3]
    #        print(11)
    #        print(12)
        if parteGL[0]!="GLID":
            parteGL.insert(1,v12)
            parteGL.insert(1,v11)
    #    print(parteGL)
        v13=[z1 for z1 in parteGL if parteGL[0]=="SUM"]
        v14=[z2 for z2 in parteGL if parteGL[0]=="DSC"]
        v15=[z3 for z3 in parteGL if parteGL[0]=="TND"]
        v16=[z1 for z1 in parteGL if parteGL[0]=="TAX"]
        v17=[z2 for z2 in parteGL if parteGL[0]=="OT"]
        v18=[z3 for z3 in parteGL if parteGL[0]=="MID"]
        v19=[z1 for z1 in parteGL if parteGL[0]=="MNPR"]
        v20=[z2 for z2 in parteGL if parteGL[0]=="CHDR"]
        v21=[z3 for z3 in parteGL if parteGL[0]=="NONSLS"]
        v22=[z1 for z1 in parteGL if parteGL[0]=="CMB"]
        v23=[z2 for z2 in parteGL if parteGL[0]=="OTD"]

        for p in v13:
            if p == []:
                v13.remove(p)
            d7=", ".join(v13)
            for x7 in d7:
                cadenaGL1 += str(x7)

        for q in v14:
            if q == []:
                v14.remove(q)
            d8=", ".join(v14)
            for x8 in d8:
                cadenaGL2 += str(x8)

        for r in v15:
            if r == []:
                v15.remove(r)
            d9=", ".join(v15)
            for x9 in d9:
                cadenaGL3 += str(x9)
                
        for s in v16:
            if s == []:
                v16.remove(s)
            d10=", ".join(v16)
            for x10 in d10:
                cadenaGL4 += str(x10)
                
        for t in v17:
            if t == []:
                v17.remove(t)
            d11=", ".join(v17)
            for x11 in d11:
                cadenaGL5 += str(x11)
                
        for u in v18:
            if u == []:
                v18.remove(u)
            d12=", ".join(v18)
            for x12 in d12:
                cadenaGL6 += str(x12)
                
        for v in v19:
            if v == []:
                v19.remove(v)
            d13=", ".join(v19)
            for x13 in d13:
                cadenaGL7 += str(x13)
                
        for w in v20:
            if w == []:
                v20.remove(w)
            d14=", ".join(v20)
            for x14 in d14:
                cadenaGL8 += str(x14)
                
        for x in v21:
            if x == []:
                v21.remove(x)
            d15=", ".join(v21)
            for x15 in d15:
                cadenaGL9 += str(x15)
                
        for y in v22:
            if y == []:
                v22.remove(y)
            d16=", ".join(v22)
            for x16 in d16:
                cadenaGL10 += str(x16)
                
        for z in v23:
            if z == []:
                v23.remove(z)
            d17=", ".join(v23)
            for x17 in d17:
                cadenaGL11 += str(x17)
    
    f7=open(f"{na}_SUM.txt","w")
    f7.write(cadenaGL1)
    f7.close()
    shutil.move(f"{na}_SUM.txt","\\Users\\ksanchez\\Desktop\\DataBase\\Codigo\\destino",copy_function=shutil.copy)

    f8=open(f"{na}_DSC.txt","w")
    f8.write(cadenaGL2)
    f8.close()
    shutil.move(f"{na}_DSC.txt","\\Users\\ksanchez\\Desktop\\DataBase\\Codigo\\destino",copy_function=shutil.copy)

    f9=open(f"{na}_TND.txt","w")
    f9.write(cadenaGL3)
    f9.close()
    shutil.move(f"{na}_TND.txt","\\Users\\ksanchez\\Desktop\\DataBase\\Codigo\\destino",copy_function=shutil.copy)
    
    f10=open(f"{na}_TAX.txt","w")
    f10.write(cadenaGL4)
    f10.close()
    shutil.move(f"{na}_TAX.txt","\\Users\\ksanchez\\Desktop\\DataBase\\Codigo\\destino",copy_function=shutil.copy)

    f11=open(f"{na}_OT.txt","w")
    f11.write(cadenaGL5)
    f11.close()
    shutil.move(f"{na}_OT.txt","\\Users\\ksanchez\\Desktop\\DataBase\\Codigo\\destino",copy_function=shutil.copy)

    f12=open(f"{na}_MID.txt","w")
    f12.write(cadenaGL6)
    f12.close()
    shutil.move(f"{na}_MID.txt","\\Users\\ksanchez\\Desktop\\DataBase\\Codigo\\destino",copy_function=shutil.copy)
        
    f13=open(f"{na}_MNPR.txt","w")
    f13.write(cadenaGL7)
    f13.close()
    shutil.move(f"{na}_MNPR.txt","\\Users\\ksanchez\\Desktop\\DataBase\\Codigo\\destino",copy_function=shutil.copy)

    f14=open(f"{na}_CHDR.txt","w")
    f14.write(cadenaGL8)
    f14.close()
    shutil.move(f"{na}_CHDR.txt","\\Users\\ksanchez\\Desktop\\DataBase\\Codigo\\destino",copy_function=shutil.copy)

    f15=open(f"{na}_NONSLS.txt","w")
    f15.write(cadenaGL9)
    f15.close()
    shutil.move(f"{na}_NONSLS.txt","\\Users\\ksanchez\\Desktop\\DataBase\\Codigo\\destino",copy_function=shutil.copy)
        
    f16=open(f"{na}_CMB.txt","w")
    f16.write(cadenaGL10)
    f16.close()
    shutil.move(f"{na}_CMB.txt","\\Users\\ksanchez\\Desktop\\DataBase\\Codigo\\destino",copy_function=shutil.copy)

    f17=open(f"{na}_OTD.txt","w")
    f17.write(cadenaGL11)
    f17.close()
    shutil.move(f"{na}_OTD.txt","\\Users\\ksanchez\\Desktop\\DataBase\\Codigo\\destino",copy_function=shutil.copy)

#####standard.Inventory_LPQ
'''
listaINV=glob.glob("\\Users\\ksanchez\\Desktop\\DataBase\\prueba\*")

for na in listaINV:
#    cadenaINV1=""

    for dato in open(na):
        parteINV=dato.split("|")
    #    print(parteINV)
    #    print(parteINV[0])
        if parteINV[0]=="INVID":
            v24=parteINV[1]
            v25=parteINV[3]
    #        print(v24)
    #        print(v25)
        if parteINV[0]!="INVID":
            parteINV.insert(1,v25)
            parteINV.insert(1,v24)

        v8=[z1 for z1 in parteFP if parteFP[0]=="FPSUM"]
        v9=[z2 for z2 in parteFP if parteFP[0]=="FPOT"]
        v10=[z3 for z3 in parteFP if parteFP[0]=="FPMI"]
    #    print(v10)
        for x in v8:
            if x == []:
                v8.remove(x)
            d4=", ".join(v8)
            for x4 in d4:
                cadenaFP1 += str(x1) 
    
    f4=open(f"{na}_FPSUM.txt","w")
    f4.write(cadenaFP1)
    f4.close()
    shutil.move(f"{na}_FPSUM.txt","\\Users\\ksanchez\\Desktop\\DataBase\\Codigo\\destino",copy_function=shutil.copy)
'''
######standard.Location_THF

listaLOC=glob.glob("\\Users\\ksanchez\\Desktop\\DataBase\\prueba\*")

for na in listaLOC:
    cadenaLOC1=""
    
    for dato in open(na):
        parteLOC=dato.split("|")
    #    print(parteLOC)
    #    print(parteLOC[0])
        if parteLOC[0]=="LOCID":
            v26=parteLOC[1]
            v27=parteLOC[3]
    #        print(v26)
    #        print(v27)
        if parteLOC[0]!="LOCID":
            parteLOC.insert(1,v27)
            parteLOC.insert(1,v26)
    #    print(parteLOC)
        v28=[z1 for z1 in parteLOC if parteLOC[0]=="LOC"]

        for x in v28:
            if x == []:
                v28.remove(x)
            d18=", ".join(v28)
            for x18 in d18:
                cadenaLOC1 += str(x18)
    
    f18=open(f"{na}_LOC.txt","w")
    f18.write(cadenaLOC1)
    f18.close()
    shutil.move(f"{na}_LOC.txt","\\Users\\ksanchez\\Desktop\\DataBase\\Codigo\\destino",copy_function=shutil.copy)

#####standard.Payroll_LPQ

listaPAY=glob.glob("\\Users\\ksanchez\\Desktop\\DataBase\\prueba\*")

for na in listaPAY:
    cadenaPAY1=""

    for dato in open(na):
        partePAY=dato.split("|")
    #    print(partePAY)
    #    print(partePAY[0])
        if partePAY[0]=="PAYID":
            v29=partePAY[1]
            v30=partePAY[3]
    #        print(v29)
    #        print(v30)
        if partePAY[0]!="PAYID":
            partePAY.insert(1,v30)
            partePAY.insert(1,v29)
    #    print(partePAY)
        v31=[z1 for z1 in partePAY if partePAY[0]=="PAY"]

        for x in v31:
            if x == []:
                v31.remove(x)
            d19=", ".join(v31)
            for x19 in d19:
                cadenaPAY1 += str(x19)
    
    f19=open(f"{na}_PAY.txt","w")
    f19.write(cadenaPAY1)
    f19.close()
    shutil.move(f"{na}_PAY.txt","\\Users\\ksanchez\\Desktop\\DataBase\\Codigo\\destino",copy_function=shutil.copy)