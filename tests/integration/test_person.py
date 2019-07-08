import pytest
import requests
import os

URL = os.getenv('URL', 'http://127.0.0.1:5000')


def test_create_person():
    response = requests.post(URL + '/v1/pessoas', json={
        "nome": "João",
        "profissao": "Arquiteto de TI",
        "localizacao": "A",
        "nivel": 2
    })

    body = response.json()
    code = response.status_code

    assert 201 == code
    assert "Pessoa adicionada com sucesso" == body['message']


def test_create_person_with_invalid_fields():
    response = requests.post(URL + '/v1/pessoas', json={
        "profissao": "Arquiteto de TI",
        "localizacao": "A",
        "nivel": 2
    })

    body = response.json()

    code = response.status_code

    assert 400 == code
    assert "Field 'nome' is required to save person" == body['error'][0]
