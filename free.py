"""
path=("\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\Basechan\\Station\\txt.txt")
print(path[73:76])
print(path[61:80])
"""
from datetime import datetime,timedelta
from shutil import move

fecha_actual= datetime.now()
diadelta=timedelta(days=90)

fecha_carpeta_actual=datetime.strftime(fecha_actual,"%b_%Y")
fecha_carpeta_ayer=fecha_actual+diadelta
fecha_carpeta_ayer=datetime.strftime(fecha_carpeta_ayer,"%b_%Y")

fecha_archivo_actual=datetime.strftime(fecha_actual,"%d-%m-%y")
fecha_archivo_ayer=fecha_actual-diadelta
fecha_archivo_ayer=datetime.strftime(fecha_archivo_ayer,"%d-%m-%y")

print(fecha_carpeta_actual)
print(fecha_carpeta_ayer)
#print(fecha_archivo_actual)
#print(fecha_archivo_ayer)

#move(path,f"\\Users\\Administrator\\Desktop\\DimensionData\\Destination\\{fecha_carpeta_ayer}\\")