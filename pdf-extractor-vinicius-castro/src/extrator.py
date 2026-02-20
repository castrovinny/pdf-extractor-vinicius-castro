import argparse
import sys
import os
from pypdf import PdfReader

def parse_pages(pages_str, total_pages):
    pages = set()
    try:
        parts = pages_str.split(',')
        for part in parts:
            if '-' in part:
                start, end = map(int, part.split('-'))
                for p in range(start, end + 1):
                    if 1 <= p <= total_pages:
                        pages.add(p - 1)
            else:
                p = int(part)
                if 1 <= p <= total_pages:
                    pages.add(p - 1)
        return sorted(list(pages))
    except ValueError:
        return None

def listar_pdfs():
    pdfs = [f for f in os.listdir('.') if f.endswith('.pdf')]
    if os.path.exists('src'):
        pdfs += [os.path.join('src', f) for f in os.listdir('src') if f.endswith('.pdf')]
    return list(dict.fromkeys(pdfs))

def extract_text(pdf_path, pages_option=None, password=None):
    try:
        reader = PdfReader(pdf_path)
        if reader.is_encrypted:
            if password:
                reader.decrypt(password)
            else:
                return "Erro: O arquivo está protegido por senha. Use --password."

        total_pages = len(reader.pages)
        indices = range(total_pages)
        if pages_option:
            indices = parse_pages(pages_option, total_pages)

        text_content = ""
        for i in indices:
            page_text = reader.pages[i].extract_text()
            if page_text:
                text_content += f"--- Página {i+1} ---\n{page_text}\n\n"
        return text_content if text_content else "Aviso: Nenhum texto extraível encontrado."
    except Exception as e:
        return f"Erro: {str(e)}"

def main():
    parser = argparse.ArgumentParser(description="PDF Extractor - DocuMaster Solutions")
    parser.add_argument("--input", help="Caminho do arquivo PDF")
    parser.add_argument("--pages", help="Páginas (ex: 1-3,5)")
    parser.add_argument("--output", help="Nome do arquivo .txt")
    parser.add_argument("--password", help="Senha do PDF")

    args = parser.parse_args()
    caminho_arquivo = args.input
    nome_saida = args.output

    # 1. MENU DE SELEÇÃO (Iniciando em 1)
    if not caminho_arquivo:
        arquivos = listar_pdfs()
        if not arquivos:
            print("Erro: Nenhum PDF encontrado.")
            sys.exit(1)
        
        print("\n=== Seleção de Arquivo (DocuMaster) ===")
        for i, arquivo in enumerate(arquivos, start=1):
            print(f"[{i}] {arquivo}")
        
        try:
            escolha = int(input("\nDigite o número do arquivo desejado: "))
            caminho_arquivo = arquivos[escolha - 1] # Ajusta para o índice do Python
        except (ValueError, IndexError):
            print("Erro: Seleção inválida.")
            sys.exit(1)

    # 2. PERGUNTA SOBRE O ARQUIVO TXT (Se não foi passado via comando)
    if not nome_saida:
        salvar = input("\nDeseja salvar o resultado em um arquivo .txt? (s/n): ").lower()
        if salvar == 's':
            nome_saida = input("Digite o nome para o arquivo de saída (ex: resultado.txt): ")
            if not nome_saida.endswith('.txt'):
                nome_saida += '.txt'

    # 3. EXECUÇÃO
    result = extract_text(caminho_arquivo, args.pages, args.password)
    
    if result.startswith("Erro"):
        print(result)
    else:
        if nome_saida:
            with open(nome_saida, "w", encoding="utf-8") as f:
                f.write(result)
            print(f"\n✅ SUCESSO! O arquivo '{nome_saida}' foi criado com o texto de '{caminho_arquivo}'.")
        else:
            print("\n--- CONTEÚDO EXTRAÍDO ---")
            print(result)

if __name__ == "__main__":
    main()