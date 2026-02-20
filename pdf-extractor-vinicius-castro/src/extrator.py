import argparse
import sys
import os
from pypdf import PdfReader

def parse_pages(pages_str, total_pages):
    """Converte string '1-3,5' em uma lista de índices de páginas [0, 1, 2, 4]."""
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
    """Busca arquivos PDF na pasta raiz e na pasta src."""
    pdfs = [f for f in os.listdir('.') if f.endswith('.pdf')]
    if os.path.exists('src'):
        pdfs += [os.path.join('src', f) for f in os.listdir('src') if f.endswith('.pdf')]
    # Remove duplicatas mantendo a ordem
    return list(dict.fromkeys(pdfs))

def extract_text(pdf_path, pages_option=None, password=None):
    try:
        reader = PdfReader(pdf_path)
        
        # Tratamento de PDF com senha
        if reader.is_encrypted:
            if password:
                reader.decrypt(password)
            else:
                return "Erro: O arquivo está protegido por senha. Use --password."

        total_pages = len(reader.pages)
        indices = []

        if pages_option:
            indices = parse_pages(pages_option, total_pages)
            if indices is None:
                return "Erro: Formato de páginas inválido."
        else:
            indices = range(total_pages)

        text_content = ""
        for i in indices:
            page_text = reader.pages[i].extract_text()
            if page_text:
                text_content += f"--- Página {i+1} ---\n{page_text}\n\n"
        
        return text_content if text_content else "Aviso: Nenhum texto extraível encontrado."

    except FileNotFoundError:
        return "Erro: Arquivo não encontrado."
    except Exception as e:
        return f"Erro inesperado: {str(e)}"

def main():
    parser = argparse.ArgumentParser(description="PDF Extractor - DocuMaster Solutions")
    parser.add_argument("--input", help="Caminho do arquivo PDF")
    parser.add_argument("--pages", help="Páginas (ex: 1-3,5)")
    parser.add_argument("--output", help="Nome do arquivo .txt para salvar")
    parser.add_argument("--password", help="Senha do PDF (se houver)")

    args = parser.parse_args()
    
    caminho_arquivo = args.input

    # MENU INTERATIVO: Se não passar --input, o programa deixa escolher
    if not caminho_arquivo:
        arquivos = listar_pdfs()
        if not arquivos:
            print("Erro: Nenhum arquivo PDF encontrado na pasta atual ou em /src.")
            sys.exit(1)
        
        print("\n=== Seleção de Arquivo (DocuMaster) ===")
        for i, arquivo in enumerate(arquivos):
            print(f"[{i}] {arquivo}")
        
        try:
            escolha = int(input("\nDigite o número do arquivo que deseja extrair: "))
            if 0 <= escolha < len(arquivos):
                caminho_arquivo = arquivos[escolha]
            else:
                print("Erro: Número fora da lista.")
                sys.exit(1)
        except ValueError:
            print("Erro: Por favor, digite um número válido.")
            sys.exit(1)

    # Processamento
    result = extract_text(caminho_arquivo, args.pages, args.password)
    
    if result.startswith("Erro"):
        print(result)
        sys.exit(1)
    
    # Saída
    if args.output:
        try:
            with open(args.output, "w", encoding="utf-8") as f:
                f.write(result)
            print(f"\n✅ Sucesso! Texto de '{caminho_arquivo}' salvo em '{args.output}'")
        except Exception as e:
            print(f"Erro ao salvar arquivo: {e}")
    else:
        print("\n--- CONTEÚDO EXTRAÍDO ---")
        print(result)

if __name__ == "__main__":
    main()