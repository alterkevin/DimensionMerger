# DimensionMerger
Primera version del fusionador de dimensiones de simphony, su proposito es ser un código feliz, util y estable.

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
        GL=[39:41]
        INV=[39:42]

    path e indices actuales de base-chan uwu desune~

        kspathstorage=("\\Users\\Administrador\\Desktop\\DimensionData\\Storage\\standard_zip") #\*.txt or *\.zip
        kspathdestino=("\\Users\\Administrador\\Desktop\\DimensionData\\Destino\\d.standard.merged")
        kspathbackup=("\\Users\\Administrador\\Desktop\\DimensionData\\Backup")
        GL=[61:63]
        INV=[61:64]