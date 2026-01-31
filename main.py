import qrcode
import os

def crear_qr(url, nombre_archivo):
    """
    Genera un código QR a partir de una URL y lo guarda como imagen.
    """
    try:
        # Configuración del QR
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )

        # Añadir los datos
        qr.add_data(url)
        qr.make(fit=True)

        # Crear la imagen
        img = qr.make_image(fill_color="black", back_color="white")

        # Asegurar extensión .png
        if not nombre_archivo.endswith('.png'):
            nombre_archivo += '.png'

        # Guardar imagen
        img.save(nombre_archivo)
        print(f"Archivo generado: {nombre_archivo}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    print("Generador de QR")
    url_input = input("URL: ")
    nombre_input = input("Nombre del archivo: ")

    if url_input:
        crear_qr(url_input, nombre_input)
    else:
        print("Error: No se introdujo URL.")