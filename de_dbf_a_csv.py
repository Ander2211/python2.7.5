# -*- coding: utf-8 -*-
import struct
import csv
import os
import sys


try:
    obtener_input = raw_input
except NameError:
    obtener_input = input

def convert_dbf_to_csv_native(dbf_path):
    if not os.path.exists(dbf_path):
        print("[Error] El archivo no existe: " + str(dbf_path))
        return

    nombre_base = os.path.splitext(dbf_path)[0]
    csv_path = nombre_base + ".csv"

    if os.path.exists(csv_path):
        os.remove(csv_path)

    try:
        print("Procesando: " + str(dbf_path) + "...")
        
        with open(dbf_path, 'rb') as f:
            header = f.read(32)
            if len(header) < 32:
                print("[Error] El archivo no es un DBF valido.")
                return

            num_records, header_len, record_len = struct.unpack('<IHH', header[4:12])

            num_fields = (header_len - 33) // 32
            fields = []
            for _ in range(num_fields):
                field_bytes = f.read(32)
                name, ftype, flen = struct.unpack('<11s c 4x B', field_bytes[:17])
                
                # Manejo de bytes/strings compatible con Python 2 y 3
                if isinstance(name, bytes):
                    field_name = name.split(b'\x00')[0].strip().decode('latin1')
                else:
                    field_name = name.split('\x00')[0].strip()
                    
                fields.append((field_name, ftype, flen))

            f.seek(header_len)

            # En Python 3 el archivo de texto para CSV no requiere 'b'
            modo_escritura = 'wb' if sys.version_info[0] < 3 else 'w'
            kwargs = {} if sys.version_info[0] < 3 else {'newline': '', 'encoding': 'utf-8'}

            with open(csv_path, modo_escritura, **kwargs) as csv_file:
                writer = csv.writer(csv_file)

                headers = [field[0] for field in fields]
                writer.writerow(headers)

                for _ in range(num_records):
                    record_bytes = f.read(record_len)
                    if not record_bytes or len(record_bytes) < record_len:
                        break

                    # Byte de borrado
                    if record_bytes[0:1] == b'*' or record_bytes[0] == '*':
                        continue

                    row = []
                    offset = 1
                    for field in fields:
                        flen = field[2]
                        raw_val = record_bytes[offset:offset + flen]
                        
                        val = raw_val.decode('latin1').strip()
                        if sys.version_info[0] < 3:
                            val = val.encode('utf-8')
                            
                        row.append(val)
                        offset += flen

                    writer.writerow(row)

        print("[OK] Conversion exitosa.")
        print(" -> Archivo CSV generado: " + str(csv_path))

    except Exception as e:
        print("[Error] Fallo la conversion: " + str(e))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        convert_dbf_to_csv_native(sys.argv[1])
    else:
        archivo_ingresado = obtener_input("Ingresa la ruta del archivo .dbf: ")
        convert_dbf_to_csv_native(archivo_ingresado.strip('"\''))
