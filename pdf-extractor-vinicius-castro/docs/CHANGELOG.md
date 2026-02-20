# Changelog - PDF Extractor

Todas as mudanças notáveis neste projeto serão documentadas neste arquivo.

## [1.0.0] - 2024-05-20
### Adicionado
- Funcionalidade de leitura básica de PDFs.
- Filtro para extração de páginas específicas (ex: 1-3, 5).
- Suporte para decodificação de PDFs protegidos por senha.
- Opção de exportação para arquivo `.txt` em UTF-8.
- Tratamento de erros para arquivos inexistentes e páginas fora do intervalo.

### Corrigido
- Erro ao tentar ler PDFs sem camada de texto (adicionado aviso).
- Bug no intervalo de páginas onde a contagem começava em 0 em vez de 1.