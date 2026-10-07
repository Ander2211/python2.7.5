# script nativo
import struct
import csv
import os
import sys

def convert_dbf_to_csv_native(dbf_path):
    if not os.path.exists(dbf_path):
        print "[Error] El archivo no existe: " + str(dbf_path)
        return

    # Determinar nombre del archivo CSV de salida (mismo nombre base)
    nombre_base = os.path.splitext(dbf_path)[0]
    csv_path = nombre_base + ".csv"

    # Sobrescribir archivo previo si existe
    if os.path.exists(csv_path):
        os.remove(csv_path)

    try:
        print "Procesando: " + str(dbf_path) + "..."
        
        with open(dbf_path, 'rb') as f:
            # 1. Leer cabecera principal (32 bytes)
            header = f.read(32)
            if len(header) < 32:
                print "[Error] El archivo no es un DBF valido."
                return

            num_records, header_len, record_len = struct.unpack('<IHH', header[4:12])

            # 2. Leer definiciones de campos / columnas (bloques de 32 bytes)
            num_fields = (header_len - 33) // 32
            fields = []
            for _ in range(num_fields):
                field_bytes = f.read(32)
                name, ftype, flen = struct.unpack('<11s c 4x B', field_bytes[:17])
                field_name = name.split('\x00')[0].strip()
                fields.append((field_name, ftype, flen))

            # Posicionar puntero al inicio de los registros de datos
            f.seek(header_len)

            # 3. Guardar en CSV utilizando el modulo nativo 'csv'
            with open(csv_path, 'wb') as csv_file:
                writer = csv.writer(csv_file)

                # Escribir la cabecera (nombres de columnas)
                headers = [field[0] for field in fields]
                writer.writerow(headers)

                # Escribir cada registro / fila
                for _ in range(num_records):
                    record_bytes = f.read(record_len)
                    if not record_bytes or len(record_bytes) < record_len:
                        break

                    # Verificar si el registro esta marcado como eliminado (asterisco '*')
                    if record_bytes[0] == '*':
                        continue

                    # Extraer el valor de cada campo segun su longitud
                    row = []
                    offset = 1  # Saltar el byte de estado (primer byte)
                    for field in fields:
                        flen = field[2]
                        raw_val = record_bytes[offset:offset + flen]
                        
                        # Decodificar texto con latin1 (estandar dBASE) y limpiar espacios sobrantes
                        val = raw_val.decode('latin1').strip()
                        row.append(val.encode('utf-8'))
                        offset += flen

                    writer.writerow(row)

        print "[✓] Conversion exitosa sin pip ni librerias externas."
        print "  • Archivo CSV generado: " + str(csv_path)

    except Exception as e:
        print "[Error] Fallo la conversion: " + str(e)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        convert_dbf_to_csv_native(sys.argv[1])
    else:
        archivo_ingresado = raw_input("Ingresa la ruta del archivo .dbf: ")
        convert_dbf_to_csv_native(archivo_ingresado.strip('"\''))
