# 📄 PDF Extractor – Extração de Texto de PDFs com Python

## 📌 Descrição
O **PDF Extractor** é uma solução robusta em Python para extração de texto. Ele foi desenvolvido para simular um cenário real na *DocuMaster Solutions*, onde a automação do processamento de documentos (como contratos e relatórios) é vital para a eficiência operacional.

---

## 🚀 Funcionalidades
* **Extração Total**: Lê todo o conteúdo do documento de uma vez.
* **Extração Seletiva**: Permite escolher páginas específicas ou intervalos (ex: 1-3, 5).
* **Exportação Automática**: Gera um arquivo `.txt` com o mesmo nome do PDF original.
* **Menu Interativo**: Se você não passar argumentos, o programa pergunta o que fazer.

---

## 🛠️ Tecnologias e Dependências
* **Linguagem**: Python 3.x
* **Biblioteca Principal**: `pypdf` (instalação necessária)
* **Versionamento**: Git & GitHub

---

## 📁 Estrutura do Projeto
```text
pdf-extractor/
├── docs/               # Prints de evidência da execução
├── src/
│   └── extrator.py     # Código-fonte principal
├── requirements.txt    # Lista de dependências
├── README.md           # Documentação do projeto
└── CHANGELOG.md        # Histórico de versões
