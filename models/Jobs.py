import datetime

from services.Database import Database


class Jobs():

    def __init__(self, job):
        self.error = []
        self.id = None
        self.data = job
        self.created_at = datetime.datetime.utcnow()

    def insert(self):
        self.valid_fields()

        if len(self.error) == 0:
            self.id = Database().insert("jobs", self.json())
            self.id = str(self.id)

            return self.json()

        return self.error

    def valid_fields(self):
        if ('empresa' not in self.data):
            self.error.append("Field 'empresa' is required to save person")

        if ('titulo' not in self.data):
            self.error.append("Field 'titulo' is required to save person")

        if ('descricao' not in self.data):
            self.error.append("Field 'descricao' is required to save person")

        if ('localizacao' not in self.data):
            self.error.append("Field 'localizacao' is required to save person")

        if ('nivel' not in self.data):
            self.error.append("Field 'nivel' is required to save person")

    def json(self):
        return {
            'id': self.id,
            'organization': self.data['empresa'],
            'title': self.data['titulo'],
            'description': self.data['descricao'],
            'location': self.data['localizacao'],
            'nivel': self.data['nivel'],
            'created_at': self.created_at
        }
