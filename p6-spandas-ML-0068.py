import pandas as pd
import numpy as np

# Christian Garcia Jimenez Nc = 0068
print("Christian Garcia Jimenez Nc = 0068")
# fecha = jueves/29/octubre/10/2026

serie_amigos = ["pedro", "morgan", "sammy", "scarlet", "ambar", "karol", "alan"]
print("-------------- serie lista de amigos Nc = 0068 -----------")
amigos = pd.Series(serie_amigos)
print(amigos)

serie_billetes = [20, 50, 100, 200, 500, 1000]
print("-------------- serie lista valor del billetes mx Nc = 0068 -----------")
billetes = pd.Series(serie_billetes)  # Corregido: antes decia 'amigos'
print(billetes)

serie_bletras = ["veinte", "cincuenta", "cien", "docientos", "quinientos", "mil"]
print("-------------- serie lista nombre y valor del billetes mx Nc = 0068 -----------")
tablabilletes = pd.Series(serie_billetes, index=serie_bletras)
print(tablabilletes)

# diccionario dataframe
# diccionario de valor moneda y nombre
print("------ datos de diccionario a dataframe Nc = 0068 ---------")
dicc_monedas = {
    "serie_billetes": [20, 50, 100, 200, 500, 1000],
    "serie_bletras": ["veinte", "cincuenta", "cien", "docientos", "quinientos", "mil"]
}
tablacris = pd.DataFrame(dicc_monedas, index=["A", "B", "C", "D", "E", "F"])
print(tablacris)  

print("Casa de cambio de Christian Garcia Jimenez Nc = 0058")