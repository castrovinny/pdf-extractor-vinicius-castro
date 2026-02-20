# PDF Extractor – DocuMaster Solutions 🎯

O **PDF Extractor** é uma solução em Python desenvolvida para automatizar a extração de texto de documentos PDF. O projeto foca em usabilidade, permitindo que o usuário escolha arquivos de forma interativa ou via linha de comando.

## 🛠️ Funcionalidades
- **Menu Interativo:** Lista PDFs automaticamente para seleção numerada (iniciando em 1).
- **Extração Seletiva:** Permite extrair apenas páginas específicas (ex: 1-3, 5).
- **Suporte a Senha:** Desbloqueia arquivos protegidos via parâmetro `--password`.
- **Exportação Flexível:** Opção de visualizar no terminal ou salvar em arquivo `.txt` com codificação UTF-8.
- **Tratamento de Erros:** Mensagens amigáveis para arquivos não encontrados ou páginas inválidas.

## 📦 Pré-requisitos
- Python 3.10 ou superior.
- Biblioteca `pypdf`.

## 🚀 Instalação e Uso
1. Clone este repositório.
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt