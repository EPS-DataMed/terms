
# Terms Generator

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=EPS-DataMed_terms&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=EPS-DataMed_terms) [![Coverage](https://sonarcloud.io/api/project_badges/measure?project=EPS-DataMed_terms&metric=coverage)](https://sonarcloud.io/summary/new_code?id=EPS-DataMed_terms) [![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=EPS-DataMed_terms&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=EPS-DataMed_terms)

Este projeto é uma API construída com FastAPI para gerar arquivos PDF contendo termos de uso personalizados. A API permite que você forneça o nome do projeto e o email de contato, e então gera um PDF com termos de uso pré-definidos.

## Estrutura do Projeto

- `.gitignore`: Arquivo para ignorar arquivos e pastas que não devem ser versionados.
- `main.py`: Script principal que contém a implementação da API.
- `README.md`: Este arquivo que você está lendo, que fornece uma visão geral do projeto.
- `requirements.txt`: Arquivo que lista as dependências do projeto.

## Como Executar

### Pré-requisitos

- Python 3.7 ou superior
- pip3 (gerenciador de pacotes do Python)

### Instalação

1. Clone o repositório para sua máquina local:

   ```bash
   git clone https://github.com/seu_usuario/seu_repositorio.git
   ```

2. Navegue até o diretório do projeto:

   ```bash
   cd seu_repositorio
   ```

3. Crie um ambiente virtual e ative-o:

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows use `venv\Scripts\activate`
   ```

4. Instale as dependências:

   ```bash
   pip3 install -r requirements.txt
   ```

### Executando a API

1. Inicie o servidor FastAPI usando Uvicorn:

   ```bash
   uvicorn main:app --reload
   ```

2. Acesse a documentação interativa da API em [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Endpoints

### POST /generate-terms/

Gera um arquivo PDF contendo os termos de uso.

#### Parâmetros

- `project_name` (str): Nome do projeto.
- `contact_email` (str): Email de contato.

#### Resposta

- `application/pdf`: Arquivo PDF gerado.

## Licença

Este projeto está licenciado sob os termos da licença MIT.
