# CLI Test Project

Este é um projeto de demonstração para uma CLI (Interface de Linha de Comando) usando Typer em Python. A CLI inclui funcionalidades básicas como saudação com nome e sobrenome, opção de exibir a versão e subcomandos para aprimoramentos futuros.

## Sumário

- [Material de Apoio](#material-de-apoio)
- [Estrutura do projeto](#estrutura-do-projeto)
- [Como instalar](#como-instalar)

## Material de Apoio

A seguir estará disponibilizado algumas das fontes que eu utilizei para criar este repositório:

**Documentação Oficial do Typer**
-[Typer Documentação](https://typer.tiangolo.com/)

**Lives do Eduardo Mendes**
- [Criando aplicações de linha de comando (CLIs) com Typer | Live de Python #233](https://www.youtube.com/watch?v=m1_48lmAX-Y)

**Repositório Eduardo Mendes**
-[Live 233](https://github.com/dunossauro/live-de-python/tree/main/codigo/Live233)

## Estrutura do Projeto

- [cli-test.py](cli-test.py): Arquivo principal que contém a implementação da CLI.
- [cli-app.py](cli-app.py): Arquivo com a estrutura para subcomandos adicionais (atualmente não implementados).
- [notes/](notes/notes.md): Diretório contendo anotações e informações relevantes para o projeto.

## Como instalar

1. **Clone o Repositório:** No terminal, use o comando `git clone` seguido do URL do repositório do GitHub:
   ```bash
   git clone https://github.com/Jojojmo/CLI-Test-Project.git
   ```


3. **Crie e Ative um Ambiente Virtual:**
   ```bash
   python -m venv .env
   ```
   Em seguida, ative o ambiente virtual:
   - No Windows:
     ```bash
     .env\Scripts\activate
     ```
   - No macOS/Linux:
     ```bash
     source .env/bin/activate
     ```

4. **Instale as Dependências:** Use o `pip` para instalar as dependências listadas no arquivo `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

Após seguir esses passos, o repositório estará instalado e suas dependências Python estarão configuradas no ambiente virtual, se você optou por utilizá-lo.

