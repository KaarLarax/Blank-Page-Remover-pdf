from PyPDF2 import PdfReader, PdfWriter

def eliminar_paginas_en_blanco(input_pdf, output_pdf):
    lector = PdfReader(input_pdf)
    escritor = PdfWriter()

    for pagina in lector.pages:
        contenido = pagina.extract_text().strip()
        if contenido:  # Agregar páginas con contenido
            escritor.add_page(pagina)

    with open(output_pdf, "wb") as archivo_salida:
        escritor.write(archivo_salida)

# Usar la función
eliminar_paginas_en_blanco("archivo_entrada.pdf", "archivo_salida.pdf")
