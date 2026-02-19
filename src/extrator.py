from pypdf import PdfReader


def extrair_texto_pdf(caminho_pdf):
    """
    Extrai todo o texto de um arquivo PDF.
    """
    reader = PdfReader(caminho_pdf)
    texto = ""

    for pagina in reader.pages:
        texto += pagina.extract_text() or ""

    return texto


if __name__ == "__main__":
    caminho = input("Digite o caminho do PDF: ")
    texto = extrair_texto_pdf(caminho)

    print("\n--- TEXTO EXTRAÍDO ---\n")
    print(texto)
