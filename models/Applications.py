import datetime
from services.Database import Database
from services.ScoreCandidate import ScoreCandidate
from models.Jobs import Jobs
from models.People import People
from models.RankingJobs import RankingJobs


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

        self.save_ranking()

        self.id = Database().insert("applications", self.json())
        self.id = str(self.id)

        return self.json()

    def save_ranking(self):
        job = Jobs().getById(self.data['id_vaga'])
        person = People().getById(self.data['id_pessoa'])

        sumN = ScoreCandidate().calc_n(int(job['nivel']), int(person['nivel']))
        sumD = ScoreCandidate().calc_d(person['location'], job['location'])

        score = ScoreCandidate().calc_score(sumN, sumD)

        ranking = RankingJobs({
            'nome': person['name'],
            'profissao': person['ocupation'],
            'localizacao': person['location'],
            'nivel': person['nivel'],
            'score': score,
            'job_id': self.data['id_vaga']
        })

        return ranking.insert()

    def valid_fields(self):
        if ('id_vaga' not in self.data):
            self.error.append(
                "Field 'id_vaga' is required to save application")

        if ('id_pessoa' not in self.data):
            self.error.append(
                "Field 'id_pessoa' is required to save application")

    def json(self):
        return {
            'id': self.id,
            'job_id': self.data['id_vaga'],
            'person_id': self.data['id_pessoa'],
            'created_at': self.created_at
        }
