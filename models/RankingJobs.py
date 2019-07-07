import datetime
from bson.objectid import ObjectId
from services.Database import Database
from services.ScoreCandidate import ScoreCandidate


class RankingJobs():

    def __init__(self, ranking={}):
        self.error = []
        self.id = None
        self.data = ranking
        self.created_at = datetime.datetime.utcnow()

    def insert(self):
        self.valid_fields()

        if len(self.error) > 0:
            return self.error

        self.id = Database().insert("ranking", self.json())
        self.id = str(self.id)

        return self.json()

    def valid_fields(self):
        if ('nome' not in self.data):
            self.error.append(
                "Field 'nome' is required to save ranking")

        if ('profissao' not in self.data):
            self.error.append(
                "Field 'profissao' is required to save ranking")

        if ('localizacao' not in self.data):
            self.error.append(
                "Field 'localizacao' is required to save ranking")

        if ('nivel' not in self.data):
            self.error.append(
                "Field 'nivel' is required to save ranking")

        if ('score' not in self.data):
            self.error.append(
                "Field 'score' is required to save ranking")

    def json(self):
        return {
            'id': self.id,
            'nome': self.data['nome'],
            'profissao': self.data['profissao'],
            'localizacao': self.data['localizacao'],
            'nivel': self.data['nivel'],
            'score': self.data['score'],
            'job_id': ObjectId(self.data['job_id']),
            'created_at': self.created_at
        }

    def getByJobId(self, job_id):
        applys = Database().find("ranking", {"job_id": ObjectId(job_id)}, {
            "field": "score", "order": -1})

        result = []
        for apply in list(applys):
            result.append({
                "nome": apply['nome'],
                "profissao": apply['profissao'],
                "localizacao": apply['localizacao'],
                "nivel": apply['nivel'],
                "score": apply['score']
            })

        return result
