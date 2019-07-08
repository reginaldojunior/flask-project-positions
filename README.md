# Python Positions Challenge

## Sobre

Esse desafio tem como objetivo resolver o problema de procurar o melhor canditado para determinada vaga de emprego baseado no SCORE da canditadura.

## Variaveis de Ambiente

Existe duas variaveis de ambiente que devem ser utilizadas para funcionar dinamicamente o projeto, elas são:

- MONGODB_STRING
- URL

A `MONGODB_STRING` é utilizada para conexão com o MongoDB e a `URL` é o endereço onde o serviço está funcionando para que os testes integrados rodem.

## Instalando

O projeto está utilizando o docker como container para desenvolvimento e ambiente produtivo. Para iniciar-lo bastar rodar os seguintes comandos.

- `docker-compose build`
- `docker-compose up`

## Testes

Os testes podem ser rodados com o seguinte comando

- `docker-compose exec web pytest -s tests/`

## Endpoints

### [POST] /v1/candidaturas

#### Request

```
{"id_vaga": 1,"id_pessoa": 2}
```

#### Response

 - 201 - Criado

 ```
 {
  "message": "Candidatura adicionada com sucesso",
  "response": {
    "created_at": "Mon, 08 Jul 2019 13:53:18 GMT",
    "id": "5d234ace7cafa122c78b19a2",
    "job_id": "5d20e4c4a62822d106ba2c67",
    "person_id": "5d2216171dac89ce83399c80"
  }
 }
 ```

 - 500 - Erro desconhecido
 ```
 {
  "code": 500,
  "error": "'5d22f171dac89ce83399c80' is not a valid ObjectId, it must be a 12-byte input or a 24-character hex string"
 }
 ```

 - 400 - Mal formação no request
 ```
 {
  "code": 400,
  "error": [
    "Field 'id_pessoa' is required to save application"
  ]
 }
 ```