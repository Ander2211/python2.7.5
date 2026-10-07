import os
import sys
import pandas as pd
from dbfread import DBF

def convertir_dbf_a_csv(ruta_dbf):
    if not os.path.exists(ruta_dbf):
        print "[Error] El archivo no existe: " + str(ruta_dbf)
        return

    if not ruta_dbf.lower().endswith('.dbf'):
        print "[Aviso] El archivo no tiene extension .dbf."
        return

    # Mismo nombre base para el CSV de salida
    nombre_base = os.path.splitext(ruta_dbf)[0]
    ruta_csv = nombre_base + ".csv"

    # Sobrescribir archivo previo si existe
    if os.path.exists(ruta_csv):
        os.remove(ruta_csv)
        print "• Se elimino la version previa de: " + str(ruta_csv)

    try:
        print "Procesando: " + str(ruta_dbf) + "..."
        
        # Cargar registros desde la tabla DBF con codificacion latin1 / cp1252
        table = DBF(ruta_dbf, encoding='latin1', ignore_missing_memofile=True)
        df = pd.DataFrame(list(table))

        # Exportar a CSV sobrescribiendo
        df.to_csv(ruta_csv, index=False, encoding='utf-8-sig', mode='w')

        print "\n[✓] Conversion exitosa:"
        print "  • Filas procesadas    : " + str(len(df))
        print "  • Columnas procesadas : " + str(len(df.columns))
        print "  • Archivo CSV generado: " + str(ruta_csv)

    except Exception as e:
        print "[Error] Fallo la conversion: " + str(e)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        # Permite ejecutar: python convert_dbf_to_csv.py tu_archivo.dbf
        convertir_dbf_a_csv(sys.argv[1])
    else:
        # Si no se le pasa argumento, pide la ruta interactivamente
        archivo_ingresado = raw_input("Ingresa la ruta del archivo .dbf: ")
        convertir_dbf_a_csv(archivo_ingresado.strip('"\''))