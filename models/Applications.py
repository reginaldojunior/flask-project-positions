import datetime

from services.Database import Database


class Applications():

    def __init__(self, application):
        self.error = []
        self.id = None
        self.data = application
        self.created_at = datetime.datetime.utcnow()

    def insert(self):
        self.valid_fields()

        if len(self.error) > 0:
            return self.error

        self.id = Database().insert("applications", self.json())
        self.id = str(self.id)

        return self.json()

    def valid_fields(self):
        if ('id_vaga' not in self.data):
            self.error.append(
                "Field 'id_vaga' is required to save application")

        if ('id_pessoa' not in self.data):
            self.error.append(
                "Field 'id_pessoa' is required to save person")

    def json(self):
        return {
            'id': self.id,
            'job_id': self.data['id_vaga'],
            'person_id': self.data['id_pessoa'],
            'created_at': self.created_at
        }
