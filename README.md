
# Terms Generator

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=EPS-DataMed_terms&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=EPS-DataMed_terms)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=EPS-DataMed_terms&metric=coverage)](https://sonarcloud.io/summary/new_code?id=EPS-DataMed_terms)
[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=EPS-DataMed_terms&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=EPS-DataMed_terms)

## Descrição do Projeto

Este projeto é uma API construída com FastAPI para gerar arquivos PDF contendo termos de uso personalizados. A API permite que você forneça o nome do projeto e o email de contato, e então gera um PDF com termos de uso pré-definidos.

## Configuração do ambiente de desenvolvimento local

### Pré-requisitos

- Python 3.11 ou superior
- `venv` para gerenciamento de ambientes virtuais
- Dependências listadas em `requirements.txt`

Siga os passos abaixo para configurar o ambiente de desenvolvimento local:

1. **Clone o repositório**

   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd terms
   ```

2. **Crie e ative um ambiente virtual**

   ```bash
   python -m venv venv
   source venv/bin/activate   # No Windows, use `venv\Scripts\activate`
   ```

3. **Instale as dependências**

   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt 
   ```

4. **Execute a aplicação**

   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8005 --reload
   ```

   A aplicação estará disponível em `http://127.0.0.1:8005`.

### Testes

1. Para executar os testes, utilize o comando abaixo:

    ```bash
    pytest
    ```

## Configuração do ambiente de desenvolvimento com Docker

### Pré-requisitos

- Docker
- Docker Compose

1. **Construir a imagem Docker**
    ```bash
    docker-compose build
    ```

2. **Executar o container**
    ```bash
    docker-compose up
    ```

A aplicação estará disponível em `http://127.0.0.1:8005`.

## Endpoints

### POST /generate-terms/

Gera um arquivo PDF contendo os termos de uso.

#### Parâmetros

- `project_name` (str): Nome do projeto.
- `contact_email` (str): Email de contato.

#### Resposta

- `application/pdf`: Arquivo PDF gerado.

## Licença

Este projeto está licenciado sob a [MIT License](./LICENSE).