# QRCodeGenerator
A simple Qr Code Generator Program by a URL with Python

## Requisitos
- Python 3.x
- Librerías en requirements.txt

## Instalación

1. **Clonar el repositorio:**
   git clone https://github.com/raultejada24/QRCodeGenerator.git

2. **Crear y activar entorno virtual:**
   python3 -m venv venv
   source venv/bin/activate

3. **Instalar librerías:**
   pip install -r requirements.txt

## Uso

1. **Activar entorno:**
   source venv/bin/activate

2. **Ejecutar el script:**
   python main.py

El sistema solicitará:
- **URL**: El enlace o texto a convertir.
- **Nombre**: El nombre del archivo de salida (se añade .png automáticamente).

## Estructura del Proyecto
- `main.py`: Script principal de generación.
- `requirements.txt`: Lista de dependencias.
- `.gitignore`: Archivos excluidos de Git (como el entorno virtual y las imágenes de prueba).
