import re
from collections import defaultdict
from functools import lru_cache

import matplotlib.pyplot as plt
import requests


class DraCor:
    """
    Base class used to represent Drama Corpus entity.

    DraCor consists of Corpuses.

    Attributes
    ----------
    _base_url : str
        a base API url
    """

    _base_url = 'https://dracor.org/api/'

    @staticmethod
    def make_get_json_request(url):
        """Base method to send GET request and retrieve json from response.

        Parameters
        ----------
        url : str

        Returns
        -------
        dictionary
            json

        Raises
        ------
        Exception
            Client or Server Error can be raised.
        """

        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    @staticmethod
    def make_get_text_request(url):
        """Base method to send GET request and retrieve text from response.

        Parameters
        ----------
        url : str

        Returns
        -------
        string
            text

        Raises
        ------
        Exception
            Client or Server Error can be raised.
        """

        response = requests.get(url)
        response.raise_for_status()
        return response.text

    def __init__(self):
        """Set name, status, existdb and version attributes from dracor_info method
        """

        info = self.dracor_info()
        for key in info:
            setattr(self, self.lowerCamelCase_to_snake_case(key), info[key])

    @staticmethod
    def lowerCamelCase_to_snake_case(name):
        return re.sub('(?!^)([A-Z]+)', r'_\1', name).lower()

    @staticmethod
    def snake_case_to_lowerCamelCase(name):
        return re.sub('_([^_]+)', lambda match: match.group(1).capitalize(), name)

    @lru_cache()
    def dracor_info(self):
        """Get API info.

        Shows version numbers of the dracor-api app and the underlying eXist-db.

        Returns
        -------
        dictionary
            {
              "name" : "DraCor API",
              "status" : "beta",
              "existdb" : "4.7.0",
              "version" : "0.57.1"
            }
        """

        return self.make_get_json_request(f"{self._base_url}/info")

    @lru_cache()
    def corpora(self, include=''):
        """List available corpora.

        Get info about the corpora of Drama Corpus.

        Parameters
        ----------
        include : str, optional
            Whether to return metrics in the output or not (can be only 'metrics' or '')

        Returns
        -------
        list
            [
                {
                    "repository" : "https://github.com/dracor-org/rusdracor",
                    "name" : "rus",
                    "uri" : "https://dracor.org/api/corpora/rus",
                    "title" : "Russian Drama Corpus",
                    "metrics": {
                        "female": 123,
                        "male": 234,
                        ...
                    } -- optional
                },
                ...
            ]

        Raises
        ------
        AssertionError
            If include parameter is not equal either 'metrics' or ''
        """

        assert include in ['', 'metrics'], "Include parameter should be either 'metrics' or ''"
        return self.make_get_json_request(f"{self._base_url}/corpora/?include={include}")

    @lru_cache()
    def corpora_names(self):
        """Get all available corpora names.

        Returns
        -------
        list
            ['rus', ...]
        """

        return [corpus['name'] for corpus in self.corpora()]

    @lru_cache()
    def corpus_name_to_field(self, field):
        """Map corpus name to the field value.

        Returns
        -------
        dictionary
            {
                "rus": field_value,
                ...
            }
        """

        return {corpus['name']: corpus[field] for corpus in self.corpora()}

    @lru_cache()
    def corpus_name_to_repository(self):
        """Map corpus name to the repository url.

        Returns
        -------
        dictionary
            {
                "rus": "https://dracor.org/api/corpora/rus",
                ...
            }
        """

        return self.corpus_name_to_field('repository')

    @lru_cache()
    def corpus_name_to_title(self):
        """Map corpus name to the title (full name).

        Returns
        -------
        dictionary
            {
                "rus": "Russian Drama Corpus",
                ...
            }
        """

        return self.corpus_name_to_field('title')

    @lru_cache()
    def corpus_name_to_uri(self):
        """Map corpus name to the api uri.

        Returns
        -------
        dictionary
            {
                "rus": "https://dracor.org/api/corpora/rus",
                ...
            }
        """

        return self.corpus_name_to_field('uri')

    @lru_cache()
    def field_to_corpus_name(self, field):
        """Map field value to the corpus name.

        Returns
        -------
        dictionary
            {
                field_value: "rus",
                ...
            }
        """

        return {
            play[field]: corpus_name
            for corpus_name in self.corpora_names()
            for play in Corpus(corpus_name).corpus_info()['dramas']
        }

    @lru_cache()
    def play_title_to_corpus_name(self):
        """Map play title to the corpus name.

        Returns
        -------
        dictionary
            {
                "Не убий": "rus",
                ...
            }
        """

        return self.field_to_corpus_name('title')

    @lru_cache()
    def play_name_to_corpus_name(self):
        """Map play name to the corpus name.

        Returns
        -------
        dictionary
            {
                "andreyev-ne-ubiy": "rus",
                ...
            }
        """

        return self.field_to_corpus_name('name')

    @lru_cache()
    def play_id_to_field(self, field):
        """Map play id to the field value.

        Returns
        -------
        dictionary
            {
                'rus000138': field_value,
                ...
            }
        """

        return {
            play['id']: play[field]
            for corpus_name in self.corpora_names()
            for play in Corpus(corpus_name).corpus_info()['dramas']
        }

    @lru_cache()
    def field_to_play_id(self, field):
        """Map field value to the play id.

        Returns
        -------
        dictionary
            {
                field_value: 'rus000138',
                ...
            }
        """

        return {
            play[field]: play['id']
            for corpus_name in self.corpora_names()
            for play in Corpus(corpus_name).corpus_info()['dramas']
        }

    @lru_cache()
    def play_id_to_play_title(self):
        """Map play id to the play title.

        Returns
        -------
        dictionary
            {
                'rus000138': 'Не убий',
                ...
            }
        """

        return self.play_id_to_field('title')

    @lru_cache()
    def play_title_to_play_id(self):
        """Map play title to the play id.

        Returns
        -------
        dictionary
            {
                'Не убий': 'rus000138',
                ...
            }
        """

        return self.field_to_play_id('title')

    @lru_cache()
    def play_id_to_play_name(self):
        """Map play id to the play name.

        Returns
        -------
        dictionary
            {
                'rus000138': 'andreyev-ne-ubiy',
                ...
            }
        """

        return self.play_id_to_field('name')

    @lru_cache()
    def play_name_to_play_id(self):
        """Map play name to the play id.

        Returns
        -------
        dictionary
            {'andreyev-ne-ubiy': 'rus000138', ...}
        """

        return self.field_to_play_id('name')

    @lru_cache()
    def sparql(self, query):
        """Submit SPARQL queries with query parameter

        Parameters
        ----------
        query : str
            A SPARQL query

        Returns
        -------
        string
            result xml
        """

        return self.make_get_text_request(f"{self._base_url}/sparql?query={query}")


class Corpus(DraCor):
    """
    A class used to represent a Corpus of DraCor

    Corpus (cal/ger/greek/rom/rus/shake/span/swe/...) consists of plays.
    """

    def __init__(self, corpus_name):
        """Set corpusname, title, repository url and number of plays attributes from corpus_info method.

        Parameters
        ----------
        corpus_name : str
            The name of the corpus

        Raises
        ------
        AssertionError
            If there is no such corpus_name
        """

        assert corpus_name in self.corpora_names(), f'No such corpusname "{corpus_name}"'
        super().__init__()
        self.corpus_name = corpus_name
        info = self.corpus_info()
        for key in info:
            setattr(self, self.lowerCamelCase_to_snake_case(key), info[key])
        self.num_of_plays = len(info['dramas'])

    @lru_cache()
    def corpus_info(self):
        """List corpus content.

        Lists all plays available in the corpus including the id, title, author(s) and other meta data.

        Returns
        -------
        dictionary
            {
              "name": "rus",
              "title": "Russian Drama Corpus",
              "repository": "https://github.com/dracor-org/rusdracor",
              "dramas": [
                {
                    ...
                },
                ...
              ]
            }
        """

        return self.make_get_json_request(f"{self._base_url}/corpora/{self.corpus_name}")

    @lru_cache()
    def play_ids(self):
        """Get all corpus' play ids.

        Returns
        -------
        list
            ["rus000138", ...]
        """

        return [play['id'] for play in self.corpus_info()['dramas']]

    @lru_cache()
    def play_names(self):
        """Get all corpus' play names.

        Returns
        -------
        dictionary
            {
                "rus000138": "andreyev-ne-ubiy",
                ...
            }
        """

        return {play['id']: play['name'] for play in self.corpus_info()['dramas']}

    @lru_cache()
    def play_titles(self):
        """Get all corpus' play titles.

        Returns
        -------
        dictionary
            {
                "rus000138": "Не убий",
                ...
            }
        """

        return {play['id']: play['title'] for play in self.corpus_info()['dramas']}

    @lru_cache()
    def written_years(self):
        """Map play id to the written year.

        Returns None if the written year is unknown.

        Returns
        -------
        dictionary
            {
                'rus000138': 1913,
                ...
            }
        """

        return {
            play['id']: (int(play['writtenYear']) if play['writtenYear'] else play['writtenYear'])
            for play in self.corpus_info()['dramas']
        }

    @lru_cache()
    def premiere_years(self):
        """Map play id to the premiere year.

        Returns None if the premiere year is unknown.

        Returns
        -------
        dictionary
            {
                'rus000138': 1913,
                ...
            }
        """

        return {
            play['id']: (int(play['premiereYear']) if play['premiereYear'] else play['premiereYear'])
            for play in self.corpus_info()['dramas']
        }

    @lru_cache()
    def print_years(self):
        """Map play id to the print year.

        Returns None if the print year is unknown.

        Returns
        -------
        dictionary
            {
                'rus000138': 1913,
                ...
            }
        """

        return {
            play['id']: (int(play['printYear']) if play['printYear'] else play['printYear'])
            for play in self.corpus_info()['dramas']
        }

    @lru_cache()
    def metadata(self):
        """List of metadata for all plays in a corpus.

        Returns
        -------
        list
            [
                {
                    "id": "rus000167",
                    "size": 12,
                    "numOfSpeakersMale": 5,
                    ...
                },
                ...
            ]
        """

        return self.make_get_json_request(f"{self._base_url}/corpora/{self.corpus_name}/metadata")

    @lru_cache()
    def filter(self, **kwargs):
        """Filter Plays of a Corpus.

        Parameters
        ----------
        kwargs
            {
                "written_year__eq": 1930,
                "all_in_index__gt": 2,
                ...
            }

        Raises
        ------
        ValueError
            If the input arguments are not correct

        Returns
        -------
        list
            list of play ids that satisfy the conditions
        """

        plays = self.corpus_info()['dramas']
        for kwarg, value in kwargs.items():
            if value is not None:
                value = str(value)
            if '__' not in kwarg:
                raise ValueError(f"Incorrect argument {kwarg} as it should contain '__'")
            field, relation = kwarg.split('__')
            field = self.snake_case_to_lowerCamelCase(field)
            if plays and field not in plays[0]:
                raise ValueError(f"Incorrect argument {kwarg} as it contains nonexistent field {field}")
            correct_plays = []
            for play in plays:
                field_value = play[field]
                was_error = False
                if relation == 'eq':
                    if field_value != value:
                        was_error = True
                elif relation == 'ne':
                    if field_value == value:
                        was_error = True
                elif relation == 'gt':
                    if field_value <= value:
                        was_error = True
                elif relation == 'ge':
                    if field_value < value:
                        was_error = True
                elif relation == 'lt':
                    if field_value >= value:
                        was_error = True
                elif relation == 'le':
                    if field_value > value:
                        was_error = True
                else:
                    raise ValueError(
                        f"Incorrect relation in argument {kwarg}"
                        f"as it should be either of the following: "
                        f"'eq' / 'ne' / 'gt' / 'ge' / 'lt' / 'le'"
                    )
                if not was_error:
                    correct_plays.append(play)
            plays = correct_plays
        # for i, play in enumerate(plays):
        #     for key in dict(play):
        #         play[self.lowerCamelCase_to_snake_case(key)] = play.pop(key)
        # return plays
        return [play['id'] for play in plays]

    @lru_cache()
    def authors_summary(self):
        """Authors' summary for a corpus.

        Returns
        -------
        list
            [
                ("Scheerbart, Paul", 20),
                ("Goethe, Johann Wolfgang", 19),
                ("Hofmannsthal, Hugo von", 17),
                ...
            ]
        """

        authors = defaultdict(int)
        info = self.corpus_info()
        for play in info['dramas']:
            for author in play['authors']:
                authors[author['name']] += 1
        return sorted(authors.items(), key=lambda elem: -elem[1])

    @lru_cache()
    def authors_summary_str(self, num_of_authors=5):
        """String representation of authors_summary method

        Parameters
        ----------
        num_of_authors : int
            The number of the most popular authors to display

        Returns
        -------
        string
            There are N authors in CORPUS_TITLE

            Top authors of the Corpus:
            20 - Scheerbart, Paul
            19 - Goethe, Johann Wolfgang
            17 - Hofmannsthal, Hugo von
            ...
        """
        authors = self.authors_summary()

        result_string = f"There are {len(authors)} authors in {self.title}\n\n" + "Top authors of the Corpus:\n"
        for i in range(min(num_of_authors, len(authors))):
            result_string += f"{authors[i][1]} - {authors[i][0]}\n"
        return result_string

    @lru_cache()
    def summary(self):
        """Summary for a corpus.

        Returns
        -------
        dictionary
            {
                "Corpus title": "German Drama Corpus",
                "Corpus id": "ger",
                "Repository": "https://github.com/dracor-org/gerdracor",
                "Written years": [1730, 1932],
                "Premiere years": [1731, 1963],
                "Years of the first printing": [1732, 1955],
                "Number of plays in the corpus": 474
            }
        """

        written_years = [written_year for written_year in self.written_years().values() if written_year]
        premiere_years = [premiere_year for premiere_year in self.premiere_years().values() if premiere_year]
        print_years = [print_year for print_year in self.print_years().values() if print_year]
        return {
            'Corpus title': self.title,
            'Corpus id': self.corpus_name,
            'Repository': self.repository,
            'Written years': [min(written_years), max(written_years)],
            'Premiere years': [min(premiere_years), max(premiere_years)],
            'Years of the first printing': [min(print_years), max(print_years)],
            'Number of plays in the corpus': self.num_of_plays,
        }

    def __str__(self):
        """Corpus summary in a text

        Returns
        -------
        string
            "Written years: 1730 - 1932
            Premiere years: 1731 - 1963
            Years of the first printing: 1732 - 1955
            474 plays in German Drama Corpus
            Corpus id: ger
            repository: https://github.com/dracor-org/gerdracor"
        """

        info = self.summary()
        return f"Written years: {info['Written years'][0]} - {info['Written years'][1]}\n" \
               f"Premiere years: {info['Premiere years'][0]} - {info['Premiere years'][1]}\n" \
               f"Years of the first printing: {info['Years of the first printing'][0]} - {info['Years of the first printing'][1]}\n" \
               f"{info['Number of plays in the corpus']} plays in {info['Corpus title']}\n" \
               f"Corpus id: {info['Corpus id']}\n" \
               f"repository: {info['Repository']}\n"


class Play(Corpus):
    """
    A class used to represent a Play of a Corpus

    Play consists of Characters
    """

    def __init__(self, play_id=None, play_name=None, play_title=None):
        """Set Play characteristics (wikidata_id, title, source, ...)

        If play_id is not None, play_name and play_title are not considered
        If play_id is None AND play_name is not None, play_title is not considered
        If play_id is None AND play_name is None, play_title should not be None,
            otherwise ValueError is raised
        If play_id is None, automatic corpus detection is applied,
            so the errors are possible: there could be several plays with
                the same name or title (depending on what is not None)

        Parameters
        ----------
        play_id
            Id of a play
        play_name
            Name of a play
        play_title
            Title of a play

        Raises
        ------
        AssertionError
            If the input attributes are not correct
        ValueError
            If all of play_id, play_name and play_title are not specified (=None)
        """

        if play_id is not None:
            corpus_name = re.sub('\d+', '', play_id)
            assert corpus_name in self.corpora_names(), f'There is no such corpus {corpus_name}'
            super().__init__(corpus_name)
            assert play_id in self.play_ids(), \
                f"No such play_id in the {corpus_name} corpus aka '{self.corpus_name_to_title()[corpus_name]}'"
            self.id = play_id
            self.name = self.play_id_to_play_name()[self.id]
            self.title = self.play_id_to_play_title()[self.id]
        elif play_name is not None:
            play_names = self.play_name_to_play_id()
            assert play_name in play_names, f"No such play_name {play_name} in the corpora"
            self.name = play_name
            self.id = self.play_name_to_play_id()[self.name]
            self.title = self.play_id_to_play_title()[self.id]
        elif play_title is not None:
            play_titles = self.play_title_to_play_id()
            assert play_title in play_titles, f"No such play_title {play_title} in the corpora"
            self.title = play_title
            self.id = self.play_title_to_play_id()[self.title]
            self.name = self.play_id_to_play_name()[self.id]
        else:
            raise ValueError("No play_id, play_name or play_title specified")

        # super().__init__(self.play_title_to_corpus_name()[self.title])
        info = self.play_info()
        for key in info:
            setattr(self, self.lowerCamelCase_to_snake_case(key), info[key])
        if hasattr(self, 'author'):
            delattr(self, 'author')
        metrics = self.metrics()
        for key in metrics:
            setattr(self, self.lowerCamelCase_to_snake_case(key), metrics[key])

    @lru_cache()
    def play_info(self):
        """Get metadata and network metrics for a single play

        Returns
        -------
        dictionary
            json
        """

        return self.make_get_json_request(f"{self._base_url}/corpora/{self.corpus_name}/play/{self.name}")

    @lru_cache()
    def metrics(self):
        """Get network metrics for a single play

        Returns
        -------
        dictionary
            {
                "size": 23,
                "averageClustering": 0.9121040025468615,
                ...
            }
        """
        return self.make_get_json_request(f"{self._base_url}/corpora/{self.corpus_name}/play/{self.name}/metrics")

    @lru_cache()
    def cast(self):
        """Get a list of characters of a play

        Returns
        -------
        dictionary
            [
                {
                    "numOfSpeechActs": 192,
                    "gender": "MALE",
                    ...
                },
                ...
            ]
        """

        return self.make_get_json_request(f"{self._base_url}/corpora/{self.corpus_name}/play/{self.name}/cast")

    @property
    @lru_cache()
    def num_of_male_characters(self):
        """Get the number of male characters in a play.

        Returns
        -------
        int
            The number of male characters in a play
        """
        return len([character for character in self.cast() if character['gender'] == 'MALE'])

    @property
    @lru_cache()
    def num_of_female_characters(self):
        """Get the number of female characters in a play.

        Returns
        -------
        int
            The number of female characters in a play
        """

        return len([character for character in self.cast() if character['gender'] == 'FEMALE'])

    @property
    @lru_cache()
    def num_of_unknown_characters(self):
        """Get the number of characters of unknown gender in a play.

        Returns
        -------
        int
            The number of characters of unknown gender in a play
        """

        return len([character for character in self.cast() if character['gender'] == 'UNKNOWN'])

    @property
    @lru_cache()
    def tei(self):
        """Get TEI document of a single play.

        Returns
        -------
        string
            TEI document of a single play
        """

        return self.make_get_text_request(f"{self._base_url}/corpora/{self.corpus_name}/play/{self.name}/tei")

    @property
    @lru_cache()
    def rdf(self):
        """Get RDF document for a single play.

        Returns
        -------
        string
            rdf representation of a play
        """

        return self.make_get_text_request(f"{self._base_url}/corpora/{self.corpus_name}/play/{self.name}/rdf")

    @property
    @lru_cache()
    def csv(self):
        """Get network data of a play as CSV

        Returns
        -------
        string
            csv representation of a play
        """

        return self.make_get_text_request(
            f"{self._base_url}/corpora/{self.corpus_name}/play/{self.name}/networkdata/csv")

    @property
    @lru_cache()
    def gexf(self):
        """Get network data of a play as GEXF.

        Returns
        -------
        string
            gexf representation of a play
        """

        return self.make_get_text_request(
            f"{self._base_url}/corpora/{self.corpus_name}/play/{self.name}/networkdata/gexf"
        )

    @lru_cache()
    def spoken_text(self, gender=''):
        """Get spoken text of a play (excluding stage directions).

        Parameters
        ----------
        gender
            should have one of the following values: '' (default) / 'MALE' / 'FEMALE' / 'UNKNOWN'

        Raises
        ------
        AssertionError
            If the input argument 'gender' is incorrect

        Returns
        -------
        string
            '\n'-separated replicas
        """

        assert gender in ['', 'FEMALE', 'MALE', 'UNKNOWN'], \
            "gender parameter should be either 'MALE', 'FEMALE', 'UNKONWN' or ''"
        return self.make_get_text_request(
            f"{self._base_url}/corpora/{self.corpus_name}/play/{self.name}/spoken-text?gender={gender}"
        )

    @lru_cache()
    def spoken_text_by_character(self):
        """Get spoken text for each character of a play.

        Returns
        -------
        list
            [
                {
                    "gender": "MALE",
                    "text": [
                        ...
                    ],
                    "id": "yakov",
                    ...
                }
            ]
        """

        return self.make_get_json_request(
            f"{self._base_url}/corpora/{self.corpus_name}/play/{self.name}/spoken-text-by-character"
        )

    @lru_cache()
    def stage_directions(self):
        """Get all stage directions of a play.

        Returns
        -------
        string
            '\n'-separated stage directions
        """

        return self.make_get_text_request(
            f"{self._base_url}/corpora/{self.corpus_name}/play/{self.name}/stage-directions"
        )

    @lru_cache()
    def stage_directions_with_speakers(self):
        """Get all stage directions of a play including speakers.

        Returns
        -------
        string
            '\n'-separated replicas with speakers
        """

        return self.make_get_text_request(
            f"{self._base_url}/corpora/{self.corpus_name}/play/{self.name}/stage-directions-with-speakers"
        )

    def plot(self):
        # TODO: what should be displayed here?
        plt.plot([1, 2, 3, 1.5])
        plt.show()

    def summary(self):
        """Play summary

        Returns
        -------
        dictionary
            {
                "id": "rus000138",
                ...
            }
        """

        return vars(self)
        # return {
        #     "id": self.id,
        #     "title": self.title,
        #     "subtitle": self.subtitle,
        #     "wikidata_id": self.wikidata_id,
        #     "authors": self.authors,
        #     "genre": self.genre,
        #     "source": self.source,
        #     "year_written": self.year_written,
        #     "year_printed": self.year_printed,
        #     "year_premiered": self.year_premiered
        # }

    def __str__(self):
        """Play summary in a text

        Returns
        -------
        string
            "Author(s): ...
            Title: ...
            Subtitle: ...
            Genre: ...
            Source: ...
            Year (written): ...
            Year (printed): ...
            Year (premiered): ..."
        """

        result_string = f"Author(s): {', '.join([author['name'] + ' (' + author['key'] + ')' for author in self.authors])}\n" \
                        f"Title: {self.title} ({self.id}, {self.wikidata_id})\n" \
                        f"Subtitle: {self.subtitle}\n" \
                        f"Genre: {self.genre}\n" \
                        f"Source: {self.source['name']} ({self.source['url']})\n" \
                        f"Year (written): {self.year_written}\n" \
                        f"Year (printed): {self.year_printed}\n" \
                        f"Year (premiered): {self.year_premiered}\n"
        return result_string


class Character(Play):
    """
    A class used to represent a Character of a Play.
    """

    def __init__(self, character_id, play_id=None, play_name=None, play_title=None):
        """Set Character characteristics (sex and gender, name, is_group, ...)

        Parameters
        ----------
        character_id
            Id of a character
        play_id
            Id of the play to which the character with character_id belongs
        play_name
            Name of the play to which the character with character_id belongs
        play_title
            Title of the play to which the character with character_id belongs

        Raises
        ------
        AssertionError
            If the input arguments are not correct
        """

        super().__init__(play_id=play_id, play_name=play_name, play_title=play_title)
        play_cast = self.cast()
        was_character = False
        for i, character in enumerate(play_cast):
            if character['id'] == character_id:
                was_character = True
                break
        assert was_character, f'There is no character "{character_id}" in the play with' \
                              f'play_id "{play_id}" / play_name "{play_name}" / play_title "{play_title}"'
        self.id = character_id
        for key in play_cast[i]:
            setattr(self, self.lowerCamelCase_to_snake_case(key), play_cast[key])
        for key in self.cast:
            setattr(self, self.lowerCamelCase_to_snake_case(key), self.cast[key])

    def summary(self):
        """Character summary

        Returns
        -------
        dictionary
            {
                "id": "yakov",
                ...
            }
        """

        return vars(self)

    def __str__(self):
        """Character summary in a text

        Returns
        -------
        string
            "Id: ...
            Name: ...
            Sex: ...
            Gender: ...
            Is group: ..."

        """

        result_string = f"Id: {self.id}\n" \
                        f"Name: {self.name}\n" \
                        f"Sex: {self.sex}\n" \
                        f"Gender: {self.gender}\n" \
                        f"Is group: {self.is_group}\n"
        return result_string
