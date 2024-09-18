#!/bin/bash

# Directorio del entorno virtual
VENV_DIR="venv"

# Archivo de dependencias
REQUIREMENTS_FILE="requirements.txt"

# Archivo de la aplicación CLI
CLI_FILE="main.py"

# Ciudad para el comando de la aplicación CLI
CIUDAD="Madrid"

# Formato de salida para el comando de la aplicación CLI
OUTPUT="json"

# Activar el entorno virtual
echo "Activando el entorno virtual..."
source $VENV_DIR/bin/activate

# Instalar dependencias
echo "Instalando dependencias..."
pip install -r $REQUIREMENTS_FILE

# Ejecutar la aplicación CLI
echo "Ejecutando la aplicación CLI..."
python3 main.py Luque --output json

# Mensaje final
echo "Ejecución completada con éxito."

# Desactivar el entorno virtual
deactivate
