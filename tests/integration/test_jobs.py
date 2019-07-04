import pytest
import requests


def test_create_person():
    response = requests.post('http://127.0.0.1:5000/v1/vagas', json={
        "empresa": "oi",
        "titulo": "Desnvovledor",
        "descricao": "ksafldjkfl",
        "localizacao": "D",
        "nivel": "1"
    })

    body = response.json()
    code = response.status_code

    assert 201 == code
    assert "Vaga adicionada com sucesso" == body['message']


def test_create_person_with_invalid_fields():
    response = requests.post('http://127.0.0.1:5000/v1/vagas', json={
        "titulo": "Desnvovledor",
        "descricao": "ksafldjkfl",
        "localizacao": "D",
        "nivel": "1"
    })

    body = response.json()

    code = response.status_code

    assert 400 == code
    assert "Field 'empresa' is required to save person" == body['error'][0]
