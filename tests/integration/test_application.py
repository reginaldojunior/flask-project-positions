import pytest
import requests


def test_create_person():
    person_id = create_person_mock()
    job_id = create_job_mock()

    response = requests.post('http://127.0.0.1:5000/v1/candidaturas', json={
        "id_vaga": 1,
        "id_pessoa": 2
    })

    body = response.json()
    code = response.status_code

    assert 201 == code
    assert "Candidatura adicionada com sucesso" == body['message']


def create_job_mock():
    response = requests.post('http://127.0.0.1:5000/v1/vagas', json={
        "empresa": "oi",
        "titulo": "Desnvovledor",
        "descricao": "ksafldjkfl",
        "localizacao": "D",
        "nivel": "1"
    })

    job_id = response.json()['response']['id']

    return job_id


def create_person_mock():
    person = requests.post('http://127.0.0.1:5000/v1/pessoas', json={
        "nome": "João",
        "profissao": "Arquiteto de TI",
        "localizacao": "A",
        "nivel": 2
    })

    person_id = person.json()['response']['id']

    return person_id


def test_create_person_with_invalid_fields():
    response = requests.post('http://127.0.0.1:5000/v1/pessoas', json={
        "profissao": "Arquiteto de TI",
        "localizacao": "A",
        "nivel": 2
    })

    body = response.json()

    code = response.status_code

    assert 400 == code
    assert "Field 'nome' is required to save person" == body['error'][0]
