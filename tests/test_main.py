import pytest
from fastapi.testclient import TestClient
import json
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.main import app

client = TestClient(app)

@pytest.fixture(scope="module")
def test_app():
    yield client

def test_generate_terms(test_app):
    response = test_app.post("/term/generate", data={
        "project_name": "Projeto Teste",
        "contact_email": "contato@teste.com",
        "extra_topics": json.dumps([
            {"title": "Topico 1", "body": "Detalhes do tópico 1"},
            {"title": "Topico 2", "body": "Detalhes do tópico 2"}
        ])
    })

    assert response.status_code == 200
    assert response.headers["content-type"] == "application/pdf"
    
    # Salva o arquivo retornado para verificação manual (opcional)
    with open("test_output.pdf", "wb") as f:
        f.write(response.content)

def test_invalid_extra_topics(test_app):
    response = test_app.post("/term/generate", data={
        "project_name": "Projeto Teste",
        "contact_email": "contato@teste.com",
        "extra_topics": "string_invalida"
    })

    assert response.status_code == 200
    assert response.json() == {'error': 'Expecting value: line 1 column 1 (char 0)'}

def test_missing_project_name(test_app):
    response = test_app.post("/term/generate", data={
        "contact_email": "contato@teste.com",
        "extra_topics": json.dumps([
            {"title": "Topico 1", "body": "Detalhes do tópico 1"}
        ])
    })

    assert response.status_code == 422

def test_missing_contact_email(test_app):
    response = test_app.post("/term/generate", data={
        "project_name": "Projeto Teste",
        "extra_topics": json.dumps([
            {"title": "Topico 1", "body": "Detalhes do tópico 1"}
        ])
    })

    assert response.status_code == 422

@pytest.fixture(scope="module", autouse=True)
def cleanup():
    # Executa antes dos testes
    yield
    # Executa após os testes
    if os.path.exists("test_output.pdf"):
        os.remove("test_output.pdf")
