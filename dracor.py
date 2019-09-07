import requests


class DraCor:
    _base_url = 'https://dracor.org/api/'

    @staticmethod
    def make_request(url):
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    def __init__(self):
        info = self.info()
        self.name = info['name']
        self.status = info['status']
        self.existdb = info['existdb']
        self.version = info['version']

    def info(self):
        return self.make_request(f"{self._base_url}/info")

    def corpora(self, include=''):
        assert include in ['', 'metrics'], "include parameter should be either 'metrics' or ''"
        return self.make_request(f"{self._base_url}/corpora/?include={include}")

    def corpora_names(self):
        return [corpus['name'] for corpus in self.corpora()]

    def sparql(self, query):
        return self.make_request(f"{self._base_url}/sparql?query={query}")


class Corpus(DraCor):
    def __init__(self, corpusname):
        assert corpusname in self.corpora_names(), "no such corpusname"
        super().__init__()
        self.corpusname = corpusname
        info = self.info()
        self.title = info['title']
        self.repository = info['repository']
        self.title = info['title']

    def info(self):
        return self.make_request(f"{self._base_url}/corpora/{self.corpusname}")

    def plays_names(self):
        return [play['name'] for play in self.info()['dramas']]

    def plays_ids(self):
        return [play['id'] for play in self.info()['dramas']]

    def metadata(self):
        return self.make_request(f"{self._base_url}/corpora/{self.corpusname}")


class Play(Corpus):
    def __init__(self, corpusname, playname=None, play_id=None):
        super().__init__(corpusname)
        if play_id is not None:
            assert play_id in self.plays_ids(), "no such id"
            self.playname = playname
        elif playname is not None:
            assert playname in self.plays_names(), "no such playname"
            self.play_id = play_id
        else:
            raise Exception("no playname of play_id specified")
        info = self.info()
        self.genre = info['genre']
        self.authors = info['authors']
        self.year_premiered = info['yearPremiered']
        self.year_printed = info['yearPrinted']
        self.year_normalized = info['yearNormalized']
        self.wikidata_id = info['wikidataId']
        self.subtitle = info['subtitle']
        self.title = info['title']
        self.year_written = info['yearWritten']
        self.play_id = info['id']
        self.source = info['source']

    def info(self):
        return self.make_request(f"{self._base_url}/corpora/{self.corpusname}/play/{self.playname}")

    def metrics(self):
        return self.make_request(f"{self._base_url}/corpora/{self.corpusname}/play/{self.playname}/metrics")

    def tei(self):
        return self.make_request(f"{self._base_url}/corpora/{self.corpusname}/play/{self.playname}/tei")

    def rdf(self):
        return self.make_request(f"{self._base_url}/corpora/{self.corpusname}/play/{self.playname}/rdf")

    def cast(self):
        return self.make_request(f"{self._base_url}/corpora/{self.corpusname}/play/{self.playname}/cast")

    def csv(self):
        return self.make_request(f"{self._base_url}/corpora/{self.corpusname}/play/{self.playname}/networkdata/csv")

    def gexf(self):
        return self.make_request(f"{self._base_url}/corpora/{self.corpusname}/play/{self.playname}/networkdata/gexf")

    def spoken_text(self, gender=''):
        assert gender in ['', 'FEMALE', 'MALE',
                          'UNKNOWN'], "gender parameter should be either 'MALE', 'FEMALE', 'UNKONWN' or ''"
        return self.make_request(
            f"{self._base_url}/corpora/{self.corpusname}/play/{self.playname}/spoken-text?gender={gender}")

    def spoken_text_by_character(self):
        return self.make_request(
            f"{self._base_url}/corpora/{self.corpusname}/play/{self.playname}/spoken-text-by-character")

    def stage_directions(self):
        return self.make_request(f"{self._base_url}/corpora/{self.corpusname}/play/{self.playname}/stage-directions")

    def stage_directions_with_speakers(self):
        return self.make_request(
            f"{self._base_url}/corpora/{self.corpusname}/play/{self.playname}/stage-directions-with-speakers")


class Character(Play):
    def __init__(self, corpusname, playname, id=None):
        self.id = id
        super().__init__(corpusname, playname, id)

    def id(self):
        return self.make_request(f"{self._base_url}/id/{self.id}")
