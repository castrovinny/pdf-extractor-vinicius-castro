import argparse
from pypdf import PdfReader


def extrair_texto_pdf(caminho_pdf, paginas=None):
    """
    Extrai texto de um arquivo PDF.
    Se 'paginas' for None, extrai todas as páginas.
    """
    reader = PdfReader(caminho_pdf)
    texto = ""

    total_paginas = len(reader.pages)

    if paginas is None:
        paginas = range(total_paginas)

    for i in paginas:
        if i < 0 or i >= total_paginas:
            raise ValueError(f"Página fora do intervalo: {i + 1}")
        texto += reader.pages[i].extract_text() or ""

    if not texto.strip():
        raise ValueError("PDF não contém texto extraível.")

    return texto


def salvar_texto_em_txt(texto, nome_arquivo):
    """
    Salva o texto extraído em um arquivo .txt com codificação UTF-8
    """
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(texto)


def interpretar_paginas(paginas_str):
    """
    Converte uma string como '1-3,5,10' em índices de páginas (base 0)
    """
    paginas = set()

    for parte in paginas_str.split(","):
        if "-" in parte:
            inicio, fim = parte.split("-")
            for p in range(int(inicio), int(fim) + 1):
                paginas.add(p - 1)
        else:
            paginas.add(int(parte) - 1)

    return sorted(paginas)


def criar_parser():
    parser = argparse.ArgumentParser(
        description="Extrator de texto de arquivos PDF"
    )

    parser.add_argument(
        "--input",
        required=True,
        help="Caminho do arquivo PDF"
    )

    parser.add_argument(
        "--pages",
        help="Páginas para extração (ex: 1-3,5,10)"
    )

    return parser


def main():
    parser = criar_parser()
    args = parser.parse_args()

    try:
        paginas = None
        if args.pages:
            paginas = interpretar_paginas(args.pages)

        texto = extrair_texto_pdf(args.input, paginas)

        nome_txt = args.input.replace(".pdf", ".txt")
        salvar_texto_em_txt(texto, nome_txt)

        print("\n✅ Texto extraído com sucesso!")
        print(f"📄 Arquivo salvo em: {nome_txt}")

    except FileNotFoundError:
        print("❌ Erro: Arquivo PDF não encontrado.")
    except ValueError as erro:
        print(f"❌ Erro: {erro}")
    except Exception as erro:
        print(f"❌ Erro inesperado: {erro}")


if __name__ == "__main__":
    main()
