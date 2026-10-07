#!/bin/bash

# ==============================================================================
# SCRIPT DE TAREA AUTOMÁTICA (CRON) PARA DE_DBF_A_CSV
# ==============================================================================

# 1. Definir rutas absolutas (Ajusta estas rutas según tu servidor)
RUTA_PYTHON="/usr/bin/python"
RUTA_SCRIPT="/app-cr/cdrs/de_dbf_a_csv.py"
ARCHIVO_DBF="/app-cr/cdrs/EDR-EXTRACT_2026/ne_50m_admin_0_countries.dbf"
ARCHIVO_LOG="/app-cr/cdrs/conversion.log"

# 2. Registrar fecha y hora de inicio en el Log
echo "==================================================" >> "$ARCHIVO_LOG"
echo "Ejecución iniciada el: $(date '+%Y-%m-%d %H:%M:%S')" >> "$ARCHIVO_LOG"

# 3. Ejecutar el script nativo de Python pasando el archivo
"$RUTA_PYTHON" "$RUTA_SCRIPT" "$ARCHIVO_DBF" >> "$ARCHIVO_LOG" 2>&1

# 4. Registrar código de salida
ESTADO=$?
if [ $ESTADO -eq 0 ]; then
    echo "Estado: FINALIZADO CON ÉXITO" >> "$ARCHIVO_LOG"
else
    echo "Estado: ERROR EN LA EJECUCIÓN (Código: $ESTADO)" >> "$ARCHIVO_LOG"
fi

echo "==================================================" >> "$ARCHIVO_LOG"