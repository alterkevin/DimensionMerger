from datetime import datetime,timedelta

fecha_actual= datetime.now()
diadelta=timedelta(days=1)

fecha_carpeta_actual=datetime.strftime(fecha_actual,"%B_%Y")
fecha_carpeta_ayer=fecha_actual-diadelta
fecha_carpeta_ayer=datetime.strftime(fecha_carpeta_ayer,"%B_%Y")

fecha_archivo_actual=datetime.strftime(fecha_actual,"%d-%m-%y")
fecha_archivo_ayer=fecha_actual-diadelta
fecha_archivo_ayer=datetime.strftime(fecha_archivo_ayer,"%d-%m-%y")

print(fecha_carpeta_actual)
print(fecha_carpeta_ayer)
print(fecha_archivo_actual)
print(fecha_archivo_ayer)