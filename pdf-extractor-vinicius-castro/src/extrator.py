import argparse
import sys
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
    parser.add_argument("--input", required=True, help="Caminho do arquivo PDF")
    parser.add_argument("--pages", help="Páginas (ex: 1-3,5)")
    parser.add_argument("--output", help="Nome do arquivo .txt para salvar")
    parser.add_argument("--password", help="Senha do PDF (se houver)")

    args = parser.parse_args()
    
    result = extract_text(args.input, args.pages, args.password)
    
    if result.startswith("Erro"):
        print(result)
        sys.exit(1)
    
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(result)
        print(f"Sucesso! Texto salvo em {args.output}")
    else:
        print(result)

if __name__ == "__main__":
    main()