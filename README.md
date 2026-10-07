# Convertidor de DBF a CSV (Nativo)

Script en Python ligero y portable diseñado para convertir archivos de bases de datos dBASE (`.dbf`) a formato `.csv` sin depender de librerías externas ni gestores de paquetes como `pip` (`pandas`, `dbfread`, etc.).

Funciona de forma totalmente nativa en **Python 2.7.5+** (y es compatible con **Python 3.x**) sobre entornos **Windows** y **Linux**.

---

## 🚀 Características

* **0% Dependencias Externas:** Usa únicamente módulos del núcleo estándar de Python (`struct`, `csv`, `os`, `sys`).
* **Multiplataforma:** Funciona exactamente igual en Windows, Linux y macOS.
* **Manejo de Codificación:** Soporta decodificación `latin1` / `cp1252` con salida limpia en `UTF-8` para evitar corrupción de texto (*mojibake*).
* **Sobrescritura Limpia:** Previene duplicados eliminando automáticamente archivos `.csv` previos antes de generar los nuevos.

---

## ⚙️ Configuración del Entorno (Windows)

Si tu sistema no reconoce el comando `python` en PowerShell, puedes agregar la ruta de Python 2.7 a la variable de entorno `PATH`.

### Opción permanente (a nivel de Sistema - Requiere Administrador)

```powershell
[Environment]::SetEnvironmentVariable("Path", [Environment]::GetEnvironmentVariable("Path", "Machine") + ";C:\Python27;C:\Python27\Scripts", "Machine")
```

### Opción permanente (a nivel de Usuario)

```powershell
[Environment]::SetEnvironmentVariable("Path", $env:Path + ";C:\Python27;C:\Python27\Scripts", "User")
```

> **Nota:** Reinicia la ventana de PowerShell tras ejecutar el comando.

---

## 💻 Uso en Windows

Puedes ejecutar el script pasando la ruta como argumento:

```powershell
python convert_dbf_native.py "C:\ruta\a\tu_archivo.dbf"
```

O de manera interactiva:

```powershell
python convert_dbf_native.py
```

---

## 🐧 Uso en Linux

### 1. Dar permisos de ejecución (opcional)

```bash
chmod +x convert_dbf_native.py
```

### 2. Ejecución directa

```bash
python convert_dbf_native.py /app-cr/cdrs/EDR-EXTRACT_2026/tu_archivo.dbf
```

---

## ⏰ Automatización en Linux (Cron)

Para programar la conversión automática en un servidor Linux a una hora específica:

### 1. Script ejecutor (`ejecutar_conversion.sh`)

```bash
#!/bin/bash

RUTA_PYTHON="/usr/bin/python"
RUTA_SCRIPT="/app-cr/cdrs/convert_dbf_native.py"
ARCHIVO_DBF="/app-cr/cdrs/EDR-EXTRACT_2026/tu_archivo.dbf"
ARCHIVO_LOG="/app-cr/cdrs/conversion.log"

echo "==================================================" >> "$ARCHIVO_LOG"
echo "Ejecución iniciada el: $(date '+%Y-%m-%d %H:%M:%S')" >> "$ARCHIVO_LOG"

"$RUTA_PYTHON" "$RUTA_SCRIPT" "$ARCHIVO_DBF" >> "$ARCHIVO_LOG" 2>&1

ESTADO=$?
if [ $ESTADO -eq 0 ]; then
    echo "Estado: FINALIZADO CON ÉXITO" >> "$ARCHIVO_LOG"
else
    echo "Estado: ERROR EN LA EJECUCIÓN (Código: $ESTADO)" >> "$ARCHIVO_LOG"
fi

echo "==================================================" >> "$ARCHIVO_LOG"
```

Otorga permisos de ejecución al script ejecutor:

```bash
chmod +x /app-cr/cdrs/ejecutar_conversion.sh
```

### 2. Programar en `crontab -e`

Para ejecutar todos los días a las 2:00 AM:

```cron
0 2 * * * /app-cr/cdrs/ejecutar_conversion.sh
```
