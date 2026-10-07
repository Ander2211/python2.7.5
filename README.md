# Convertidor Nativo de DBF a CSV

Script ligero y portátil en **Python 2.7.5** (y compatible con Python 3.x) para convertir archivos de bases de datos `.dbf` a formato `.csv` sin necesidad de dependencias externas como `pip`, `pandas` o `dbfread`.

---

## 🛠️ Características Principales
* **100% Nativo:** Utiliza únicamente los módulos incluidos por defecto en Python (`struct`, `csv`, `os`, `sys`).
* **Multiplataforma:** Funciona exactamente igual en Windows, Linux y macOS.
* **Manejo de Codificación:** Soporta caracteres especiales (Latin1 / CP1252 / UTF-8) declarando `# -*- coding: utf-8 -*-`.

---

## ⚙️ Configuración Previa (Solo Windows)

Si no tienes Python agregado a tus variables de entorno en PowerShell:

### Opción Permanente (A nivel de Sistema - Administrador)
```powershell
[Environment]::SetEnvironmentVariable("Path", [Environment]::GetEnvironmentVariable("¡Tienes toda la razón! Mil disculpas, fue un lapsus absoluto de mi parte al procesar la respuesta anterior. Al ser texto en Markdown, te lo puedo estructurar y redactar perfectamente.

Aquí tienes la versión completa y profesional del **`README.md`**, consolidando todo lo que hemos trabajado hasta el momento (portabilidad nativa sin `pip`, configuración de entorno, sintaxis universal, corrección de codificación y automatización en Linux):

```markdown
# Convertidor de DBF a CSV (Nativo)

Script en Python ligero y portable diseñado para convertir archivos de bases de datos dBASE (`.dbf`) a formato `.csv` sin depender de librerías externas ni gestores de paquetes como `pip` (`pandas`, `dbfread`, etc.). 

Funciona de forma totalmente nativa en **Python 2.7.5+** (y es compatible con **Python 3.x**) sobre entornos **Windows** y **Linux**.

---

## 🚀 Características
* **0% Dependencias Externas:** Usa únicamente módulos del núcleo estándar de Python (`struct`, `csv`, `os`, `sys`).
* **Multiplataforma:** Funciona nativamente en Windows, Linux y macOS.
* **Manejo de Codificación:** Soporta decodificación `latin1` / `cp1252` con salida limpia en `UTF-8` para evitar corrupción de texto (*mojibake*).
* **Sobrescritura Limpia:** Previene duplicados limpiando automáticamente salidas previas.

---

## ⚙️ Configuración del Entorno (Windows)

Si tu sistema no reconoce el comando `python`, puedes agregar la ruta de Python 2.7 a la variable de entorno `PATH` mediante **PowerShell** (como Administrador):

```powershell
[Environment]::SetEnvironmentVariable("Path", [Environment]::GetEnvironmentVariable("Path", "Machine") + ";C:\Python27;C:\Python27\Scripts", "Machine")
