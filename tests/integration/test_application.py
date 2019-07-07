import pytest
import requests


def test_create_apply():
    result = create_apply_mock()

    assert 201 == result['code']
    assert "Candidatura adicionada com sucesso" == result['body']['message']


def test_get_applys_ranking():
    result = create_apply_mock()

    response = requests.get('http://127.0.0.1:5000/v1/vagas/' +
                            str(result['job_id']) + '/candidaturas/ranking')

    assert 200 == response.status_code
    assert 75 == response.json()[0]['score']


def create_apply_mock():
    person_id = create_person_mock()
    job_id = create_job_mock()

    response = requests.post('http://127.0.0.1:5000/v1/candidaturas', json={
        "id_vaga": job_id,
        "id_pessoa": person_id
    })

    body = response.json()
    code = response.status_code

    return {"body": body, "code": code,
            "job_id": job_id, "person_id": person_id}


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
