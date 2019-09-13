import matplotlib.pyplot as plt
import requests
from collections import defaultdict, OrderedDict


class DraCor:
    _base_url = 'https://dracor.org/api/'

    @staticmethod
    def make_request(url):
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    def __init__(self):
        info = self.dracor_info()
        self.name = info['name']
        self.status = info['status']
        self.existdb = info['existdb']
        self.version = info['version']

    def dracor_info(self):
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
        info = self.corpus_info()
        self.title = info['title']
        self.repository = info['repository']
        self.num_of_plays = len(info['dramas'])

    def corpus_info(self):
        return self.make_request(f"{self._base_url}/corpora/{self.corpusname}")

    def plays_names(self):
        return [play['name'] for play in self.corpus_info()['dramas']]

    def plays_ids(self):
        return [play['id'] for play in self.corpus_info()['dramas']]

    def written_years(self):
        return [play['writtenYear'] for play in self.corpus_info()['dramas'] if play['writtenYear']]

    def premiere_years(self):
        return [play['premiereYear'] for play in self.corpus_info()['dramas'] if play['premiereYear']]

    def print_years(self):
        return [play['printYear'] for play in self.corpus_info()['dramas'] if play['printYear']]

    def metadata(self):
        return self.make_request(f"{self._base_url}/corpora/{self.corpusname}")

    def summary(self):
        written_years = self.written_years()
        premiere_years = self.premiere_years()
        print_years = self.print_years()
        return {
            'Corpus title': self.title,
            'Corpus id': self.corpusname,
            'Repository': self.repository,
            'Written years': [min(written_years), max(written_years)],
            'Premiere years': [min(premiere_years), max(premiere_years)],
            'Years of the first printing': [min(print_years), max(print_years)],
            'Number of plays in the corpus': self.num_of_plays,
        }

    def authors_summary(self):
        authors = defaultdict(int)
        info = self.corpus_info()
        for play in info['dramas']:
            for author in play['authors']:
                authors[author['name']] += 1
        return OrderedDict(sorted(authors.items(), key=lambda elem: -elem[1]))

    def authors_summary_str(self):
        authors = list(self.authors_summary().items())

        return f"There are {len(authors)} authors in {self.title}\n\n" \
               f"Top authors of the Corpus:" \
               f"{authors[0][1]} - {authors[0][0]}\n" \
               f"{authors[1][1]} - {authors[1][0]}\n" \
               f"{authors[2][1]} - {authors[2][0]}\n" \
               f"{authors[3][1]} - {authors[3][0]}\n" \
               f"{authors[4][1]} - {authors[4][0]}\n"

    def __str__(self):
        info = self.summary()
        return f"Written years: {info['Written years'][0]} - {info['Written years'][1]}\n" \
               f"Premiere years: {info['Premiere years'][0]} - {info['Premiere years'][1]}\n" \
               f"Years of the first printing: {info['Years of the first printing'][0]} - {info['Years of the first printing'][1]}\n" \
               f"{info['Number of plays in the corpus']} plays in {info['Corpus title']}\n" \
               f"Corpus id: {info['Corpus id']}, repository: {info['Repository']}"


class Play(Corpus):
    def __init__(self, corpusname, playname=None, play_id=None):
        super().__init__(corpusname)
        if play_id is not None:
            assert play_id in self.plays_ids(), "no such id"
            self.playname = self.plays_names()[self.plays_ids().index(play_id)]
        elif playname is not None:
            assert playname in self.plays_names(), "no such playname"
            self.playname = playname
        else:
            raise Exception("no playname or play_id specified")
        info = self.play_info()
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

    def play_info(self):
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

    def plot(self):
        # TODO: what should be displayed here?
        plt.plot([1, 2, 3, 1.5])
        plt.show()


class Character(Play):
    def __init__(self, corpusname, playname, id=None):
        self.id = id
        super().__init__(corpusname, playname, id)

    def id(self):
        return self.make_request(f"{self._base_url}/id/{self.id}")
