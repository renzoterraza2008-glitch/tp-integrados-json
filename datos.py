import sys
import json
    
archivo_txt = sys.argv[1]
archivo_json = sys.argv[2]
validos = []
invalidos = []


with open(archivo_txt, "r") as datoshorario:
        for i, linea in enumerate(datoshorario):
            if i > 1:
                datos = linea.split()
                if len(datos) < 8:
                    continue
            datos=linea.split()
            fecha=datos[0]
            hora=datos[1]
            temp=datos[2]
            humedad=datos[3]
            PNM=datos[4]
            DD=datos[5]
            FF=datos[6]
            lugar=" ".join(datos[7:])
            # print(hora)

# # La fecha debe existir, tener el formato esperado y representar una fecha posible.
# # La hora debe ser numérica y estar dentro del rango válido.
# # Temperatura, humedad, presión, dirección y velocidad del viento deben poder convertirse a número cuando correspondan.
# def validar_fecha(fecha):
#     try:
#         if len(fecha) == 8:
#             anio = int(fecha[0:2])
#             mes = int(fecha[2:4])
#             dia = int(fecha[4:8])
#             if 1 <= dia <= 31:
#                 if 1 <= mes <= 12:
#                     if anio<2030:
#                         return True
#         return False
#     except ValueError:
#         print("el dato no es un numero")
#         exit(1)
# fecha="20552000"
# print (validar_fecha(fecha))

