import argparse
from pypdf import PdfReader

# --- Suas funções originais (MANTIDAS) ---
def extrair_texto_pdf(caminho_pdf, paginas=None):
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
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(texto)

def interpretar_paginas(paginas_str):
    if not paginas_str: return None
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
    parser = argparse.ArgumentParser(description="Extrator de texto de arquivos PDF")
    # Removi o 'required=True' para ele não dar erro se você não digitar nada
    parser.add_argument("--input", help="Caminho do arquivo PDF")
    parser.add_argument("--pages", help="Páginas para extração (ex: 1-3,5,10)")
    return parser

# --- NOVA FUNÇÃO MAIN (AJUSTADA PARA MENU) ---
def main():
    parser = criar_parser()
    args = parser.parse_args()

    # 1. Lógica do Caminho do PDF
    caminho_input = args.input
    if not caminho_input:
        print("--- 📂 MENU DE SELEÇÃO ---")
        caminho_input = input("👉 Digite o nome do arquivo PDF (ex: Teste.pdf): ")

    # 2. Lógica das Páginas
    entrada_paginas = args.pages
    if not entrada_paginas and args.input is None: # Só pergunta se não veio via comando
        print("--- 📄 SELEÇÃO DE PÁGINAS ---")
        print("Opções: Deixe vazio para TUDO ou digite o intervalo (ex: 1-3)")
        entrada_paginas = input("👉 Escolha as páginas: ")

    try:
        # Processamento das páginas
        paginas = None
        if entrada_paginas:
            paginas = interpretar_paginas(entrada_paginas)

        # Execução principal
        texto = extrair_texto_pdf(caminho_input, paginas)
        nome_txt = caminho_input.replace(".pdf", ".txt")
        salvar_texto_em_txt(texto, nome_txt)

        print("\n✅ Sucesso! O arquivo foi gerado com as suas escolhas.")
        print(f"📄 Arquivo: {nome_txt}")

    except FileNotFoundError:
        print("❌ Erro: Arquivo PDF não encontrado. Verifique o nome digitado.")
    except Exception as erro:
        print(f"❌ Ocorreu um erro: {erro}")

if __name__ == "__main__":
    main()