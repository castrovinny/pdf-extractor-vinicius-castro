# Changelog

Todas as mudanças relevantes deste projeto serão documentadas neste arquivo.

## [1.0.0] - 2026-02-19

### Added
- Leitura básica de arquivos PDF
- Extração de texto de todas as páginas
- Extração de páginas específicas via linha de comando (CLI)
- Salvamento automático do texto extraído em arquivo `.txt`
- Uso da biblioteca `pypdf`

### Fixed
- Tratamento de erro para arquivo inexistente
- Tratamento de erro para PDF criptografado
- Tratamento de erro para PDF sem texto extraível
- Validação de páginas fora do intervalo informado

### Chore
- Estrutura inicial do projeto
- Configuração do repositório Git
- Criação do README.md
- Organização das pastas do projeto
