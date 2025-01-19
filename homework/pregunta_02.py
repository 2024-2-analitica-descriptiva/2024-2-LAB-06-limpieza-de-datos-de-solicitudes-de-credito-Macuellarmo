"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""
def pregunta_02():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """

import pandas as pd
from datetime import datetime


def validar_formato_fecha(fecha):
    """
    Valida y transforma las fechas al formato DD/MM/YYYY
    Si el formato no es válido, retorna el valor original.
    """
    try:
        #Intentar convertir al formato DD/MM/YYYY
        fecha_validada = datetime.strptime(fecha, "%d/%m/%Y")
        return fecha_validada.strftime("%d/%m/%Y")
    except ValueError:
        try:
            #Intentar convertir al formato YYYY/MM/DD
            fecha_validada = datetime.strptime(fecha, "%Y/%m/%d")
            return fecha_validada.strftime("%d/%m/%Y")
        except ValueError:
            #Si no coincide con ninguno de los formatos, retornar el valor original
            return fecha
        
def pregunta_01():
    input_file = "files/input/solicitudes_de_credito.csv"
    output_file = "files/output/solicitudes_de_credito.csv"

    """
    Función para limpiar un archivo de csv de solicitudes de crédito
        Convierte los datos en minúsculas
        Elimina duplicados
        Elimina filas con valores vacíos
        Guarda el archivo limpio en la ruta especificada

    Parámetros:
        input_files: Ruta del archivo de entrada
        output_files: Ruta del archivo de salida
    """

    #Leer el archivo csv
    dfi = pd.read_csv(input_file, sep=";")
    df = pd.read_csv(input_file, sep=";")

    #Quitar primera columna del indice
    df = df.drop(df.columns[0], axis = 1)

    #Convertir las columnas a minúsculas
    df.columns = df.columns.str.lower()
    df = df.applymap(lambda x: x.lower() if isinstance(x, str) else x)

    #Reemplazar _ por espacio
    df = df.apply(lambda col: col.str.replace('_', ' ') if col.dtype == 'object' else col)

    #Reemplazar - por espacio
    df = df.apply(lambda col: col.str.replace('-', ' ') if col.dtype == 'object' else col)

    #Quitar espacios al inicio y al final
    df = df.apply(lambda x: x.str.strip() if x.dtype == 'object' else x)

    #Convierte los montos a número entero
    df['monto_del_credito'] = df['monto_del_credito'].replace({'\$': '', ',': '', '\$': ''}, regex=True)
    df['monto_del_credito'] = pd.to_numeric(df['monto_del_credito'], errors='coerce').fillna(0).astype(int)

    #Validar y transformar fechas al formato DD/MM/YYYY
    df['fecha_de_beneficio'] = df['fecha_de_beneficio'].apply(validar_formato_fecha)

    #Eliminar duplicados
    df = df.drop_duplicates()
    
    #Eliminar filas con valores vacíos en cualquier columna
    df = df.dropna()

    #Guarda el archivo limpio
    df.to_csv(output_file, sep=";", index=False)

    dfbarrio = df['barrio'].value_counts().reset_index()

    return df.sexo.value_counts()

if __name__ == '__main__':
    #Ruta de entrada y de salida

    #Llamar a la función
    print(pregunta_01())





