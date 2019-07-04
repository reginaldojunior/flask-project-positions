import datetime

from services.Database import Database


class People():

    def __init__(self, person):
        self.error = []
        self.id = None
        self.data = person
        self.created_at = datetime.datetime.utcnow()

    def insert(self):
        self.valid_fields()

        if len(self.error) > 0:
            return self.error

        self.id = Database().insert("people", self.json())
        self.id = str(self.id)

        return self.json()

    def valid_fields(self):
        if ('nome' not in self.data):
            self.error.append("Field 'nome' is required to save person")

        if ('profissao' not in self.data):
            self.error.append("Field 'profissao' is required to save person")

        if ('localizacao' not in self.data):
            self.error.append("Field 'localizacao' is required to save person")

        if ('nivel' not in self.data):
            self.error.append("Field 'nivel' is required to save person")

    def json(self):
        return {
            'id': self.id,
            'name': self.data['nome'],
            'ocupation': self.data['profissao'],
            'location': self.data['localizacao'],
            'nivel': self.data['nivel'],
            'created_at': self.created_at
        }
