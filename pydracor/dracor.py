import re
import warnings
from collections import defaultdict
from functools import lru_cache

import requests


class DraCor:
    """
    Base class used to represent Drama Corpus entity.

    DraCor consists of Corpora.

    Attributes
    ----------
    _base_url : str
        a base API url
    _sparql_url : str
        a URL to post SPARQL queries to
    """

    _base_url = 'https://dracor.org/api/'
    _sparql_url = 'https://dracor.org/fuseki/sparql'

    def __init__(self):
        """Set name, status, existdb and version attributes from dracor_info method
        """

        #TODO: set each attribute with check? 
        info = self.dracor_info()
        for key in info:
            setattr(self, key, info[key])

    def make_get_json_request(self, url):
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
        result = self.transform_dict(response.json())
        return result

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

    @staticmethod
    def lowerCamelCase_to_snake_case(name):
        """Convert lowerCamelCase to snake_case"""
        return re.sub('(?!^)([A-Z]+)', r'_\1', name).lower()

    def transform_dict_support(self, new_dict):
        for key, value in new_dict.items():
            if isinstance(value, dict):
                new_dict[key] = self.transform_dict(value)
            elif isinstance(value, list):
                for index, item in enumerate(value):
                    if isinstance(item, dict):
                        new_dict[key][index] = self.transform_dict(item)
        return new_dict

    def transform_dict(self, multilevel_dict, f=0):
        """Apply f (0: lowerCamelCase_to_snake_case; another_value: snake_case_to_lowerCamelCase)
        to every key name in a multilevel_dict or multilevel_list"""
        if f == 0:
            f = self.lowerCamelCase_to_snake_case
        else:
            f = self.snake_case_to_lowerCamelCase
        new_dict = multilevel_dict
        if isinstance(new_dict, dict):
            new_dict = dict(
                map(lambda key_value: (f(key_value[0]), key_value[1]), new_dict.items())
            )
            new_dict = self.transform_dict_support(new_dict)
        elif isinstance(new_dict, list):
            for i, inner_new_dict in enumerate(new_dict):
                new_dict[i] = self.transform_dict(inner_new_dict)
        return new_dict

    @staticmethod
    def snake_case_to_lowerCamelCase(name):
        """Convert snake_case to lowerCamelCase"""
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
            ['cal', ...]
        """

        return [corpus['name'] for corpus in self.corpora()]

    @lru_cache()
    def corpora_titles(self):
        """Get all available corpora titles.

        Returns
        -------
        list
            ['Calderón Drama Corpus', ...]
        """

        return [corpus['title'] for corpus in self.corpora()]

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
        response = requests.post(self._sparql_url, data={'query':query}, headers={"accept": "application/sparql-results+xml"})
        response.raise_for_status()
        result = response.text
        return result
    
    @lru_cache()
    def plays_by_character_wikidata_id(self, wikidata_id):
        """List plays having a character identified by Wikidata ID
           
        
        Parameters
        ----------
        wikidata_id : str
            The wikidata id of a character

        Returns
        -------
        list
            [
              {
                "id": "ger000311",
                "title": "Maria Stuart",
                ...
              },
              ...
            ]
        """
        return self.make_get_json_request(f"{self._base_url}/character/{wikidata_id}")


    @lru_cache()
    def summary(self):
        """DraCor summary

        Returns
        -------
        dictionary
            {
                "name": "DraCor API",
                "status": "beta",
                "existdb": "4.7.0",
                "version": "0.57.1",
                "corpora_full_names": ["Calderón Drama Corpus", "German Drama Corpus", "Greek Drama Corpus", "Roman Drama Corpus", "Russian Drama Corpus", "Shakespeare Drama Corpus", "Spanish Drama Corpus", "Swedish Drama Corpus"],
                "corpora_abbreviations": ["cal", "ger", "greek", "rom", "rus", "shake", "span", "swe"],
                "number_of_corpora": 8,
            }
        """

        info = self.dracor_info()
        corpora_names = self.corpora_names()
        info.update({
            "corpora_full_names": self.corpora_titles(),
            "corpora_abbreviations": corpora_names,
            "number_of_corpora": len(corpora_names)
        })
        return info

    @lru_cache()
    def __str__(self):
        """DraCor summary in a text

        Returns
        -------
        string
            "Name: DraCor API
            Status: beta
            Existdb: 4.7.0
            Version: 0.57.1
            Corpora (full names): Calderón Drama Corpus, German Drama Corpus, Greek Drama Corpus, Roman Drama Corpus, Russian Drama Corpus, Shakespeare Drama Corpus, Spanish Drama Corpus, Swedish Drama Corpus
            Corpora (abbreviations): cal, ger, greek, rom, rus, shake, span, swe
            Number of corpora: 8"
        """

        info = self.summary()
        return f"Name: {info['name']}\n" \
               f"Status: {info['status']}\n" \
               f"Existdb: {info['existdb']}\n" \
               f"Version: {info['version']}\n" \
               f"Corpora (full names): {', '.join(info['corpora_full_names'])}\n" \
               f"Corpora (abbreviations): {', '.join(info['corpora_abbreviations'])}\n" \
               f"Number of corpora: {info['number_of_corpora']}\n"


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
            setattr(self, key, info[key])
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
                'rus000138': '1913',
                'rus000192': '1936/1939'
                ...
            }
        """

        return {
            play['id']: play['written_year']
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
                'ger000002': '1762/1763',
                ...
            }
        """

        return {
            play['id']: play['premiere_year']
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
                'fre000034': '1547/1557',
                ...
            }
        """

        return {
            play['id']: play['print_year']
            for play in self.corpus_info()['dramas']
        }

    @lru_cache()
    def normalized_years(self):
        """Map play id to the normalized year.

        Returns None if the print normalized is unknown.

        Returns
        -------
        dictionary
            {
                'fre000034': 1512,
                ...
            }
        """

        return {
            play['id']: (int(play['year_normalized']) if play['year_normalized'] else play['year_normalized'])
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
                    "num_of_speakers_male": 5,
                    ...
                },
                ...
            ]
        """

        return self.make_get_json_request(f"{self._base_url}/corpora/{self.corpus_name}/metadata")
    
    @lru_cache()
    def metadata_csv(self):
        """Get metadata for all plays in corpus as CSV

        Returns
        -------
        string
            csv representation of a play
        """

        return self.make_get_text_request(
            f"{self._base_url}/corpora/{self.corpus_name}/metadata/csv")
    
    #TODO: Filtering works on strings right now - make more predictable 
    @lru_cache()
    def filter(self, **kwargs):
        """Filter Plays of a Corpus.

        Parameters
        ----------
        kwargs
            {
                "written_year__eq": 1913,
                "network_size__lt": 20,
                "title__icontains": "в",
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
        fields = set([field_name for play_entry in plays for field_name in play_entry.keys()])
        for kwarg, value in kwargs.items():
            if value is not None:
                value = str(value)
            if '__' not in kwarg:
                raise ValueError(f"Incorrect argument {kwarg} as it should contain '__'")
            field, relation = kwarg.rsplit('__', maxsplit=1)
            full_field = field
            field = full_field.split('__')[0]
            if plays and field not in fields:
                raise ValueError(f"Incorrect argument {kwarg} as it contains nonexistent field {field}")
            correct_plays = []
            for play in plays:
                if field not in play:
                    continue
                field_value = play[field]
                if full_field != field:
                    if field == 'authors':
                        field_value = ' && '.join([elem[full_field.split('__')[1].lower()] for elem in field_value])
                    else:
                        field_value = field_value[full_field.split('__')[1].lower()]
                if field_value is None:
                    continue
                field_value = str(field_value)
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
                elif relation == 'contains':
                    if value not in field_value:
                        was_error = True
                elif relation == 'icontains':
                    if value.lower() not in field_value.lower():
                        was_error = True
                elif relation == 'exact':
                    if field_value != value:
                        was_error = True
                elif relation == 'iexact':
                    if field_value.lower() != value.lower():
                        was_error = True
                elif relation == 'in':
                    if field_value not in value:
                        was_error = True
                else:
                    raise ValueError(
                        f"Incorrect relation in argument {kwarg}"
                        f"as it should be either of the following: "
                        f"'eq' / 'ne' / 'gt' / 'ge' / 'lt' / 'le' / 'contains' / 'icontains' / 'exact' / 'iexact' / 'in'"
                    )
                if not was_error:
                    correct_plays.append(play)
            plays = correct_plays
        # for i, play in enumerate(plays):
        #     for key in dict(play):
        #         play[self.lowerCamelCase_to_snake_case(key)] = play.pop(key)
        # return plays
        # print(plays)
        return [play['id'] for play in plays]

    @lru_cache()
    def authors_summary(self, num_of_authors=None):
        """Authors' summary for a corpus.

        Parameters
        ----------
        num_of_authors
            Number of authors to return
            If n is negative, then slice [::n] is taken

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
        sorted_authors = sorted(authors.items(), key=lambda elem: -elem[1])
        if num_of_authors is not None:
            return sorted_authors[:num_of_authors]
        return sorted_authors

    @lru_cache()
    def authors_summary_str(self, num_of_authors=None):
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
        result_string = f"There are {len(authors)} authors in {self.title}\n\n" + f"Top {num_of_authors or len(authors)} authors of the Corpus:\n"
        for i in range(min(num_of_authors or len(authors), len(authors))):
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
                "Written years": ["1730", "1932"],
                "Premiere years": ["1731", "1963"],
                "Years of the first printing": ["1732", "1955"],
                "Number of plays in the corpus": 474
            }
        """

        written_years = sorted([written_year for written_year in self.written_years().values() if written_year])
        premiere_years = sorted([premiere_year for premiere_year in self.premiere_years().values() if premiere_year])
        print_years = sorted([print_year for print_year in self.print_years().values() if print_year])
        normalized_years = [normalized_year for normalized_year in self.normalized_years().values() if normalized_year]
        return {
            'Corpus title': self.title,
            'Corpus id': self.corpus_name,
            'Repository': self.repository,
            'Written years': [written_years[0], written_years[-1]],
            'Premiere years': [premiere_years[0], premiere_years[-1]],
            'Years of the first printing': [print_years[0], print_years[-1]],
            'Normalized years': [min(normalized_years), max(normalized_years)],
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
               f"Normalized years: {info['Normalized years'][0]} - {info['Normalized years'][1]}\n" \
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
            play_names = list(self.play_id_to_play_name().values())
            assert play_name in play_names, f"No such play_name {play_name} in the corpora"
            if play_names.count(play_name) > 1:
                warnings.warn(
                    f'There are several plays with the play_name {play_name} in the corpora.'
                    f' Better use a play_id. Otherwise, a random play is selected.'
                )
            super().__init__(self.play_name_to_corpus_name()[play_name])
            self.name = play_name
            self.id = self.play_name_to_play_id()[self.name]
            self.title = self.play_id_to_play_title()[self.id]
        elif play_title is not None:
            play_titles = list(self.play_id_to_play_title().values())
            assert play_title in play_titles, f"No such play_title {play_title} in the corpora"
            if play_titles.count(play_title) > 1:
                warnings.warn(
                    f'There are several plays with the play_title {play_title} in the corpora.'
                    f' Better use a play_id. Otherwise, a random play is selected.'
                )
            self.id = self.play_title_to_play_id()[play_title]
            super().__init__(self.play_title_to_corpus_name()[play_title])
            self.title = play_title
            self.name = self.play_id_to_play_name()[self.id]
        else:
            raise ValueError("No play_id, play_name or play_title specified")

        info = self.play_info()
        for key in info:
            setattr(self, key, info[key])
        if hasattr(self, 'author'):
            delattr(self, 'author')
        metrics = self.metrics()
        for key in metrics:
            setattr(self, key, metrics[key])

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
                "average_clustering": 0.9121040025468615,
                ...
            }
        """
        return self.make_get_json_request(f"{self._base_url}/corpora/{self.corpus_name}/play/{self.name}/metrics")

    @lru_cache()
    def get_cast(self):
        """Get a list of characters of a play

        Returns
        -------
        dictionary
            [
                {
                    "num_of_speech_acts": 192,
                    "gender": "MALE",
                    ...
                },
                ...
            ]
        """

        return self.make_get_json_request(f"{self._base_url}/corpora/{self.corpus_name}/play/{self.name}/cast")

    @lru_cache()
    def cast_csv(self):
        """Get a list of characters of a play (CSV).

        Returns
        -------
        string
            csv representation of the list of characters for a single play
        """

        return self.make_get_text_request(
            f"{self._base_url}/corpora/{self.corpus_name}/play/{self.name}/cast/csv"
        )

    @property
    @lru_cache()
    def num_of_male_characters(self):
        """Get the number of male characters in a play.

        Returns
        -------
        int
            The number of male characters in a play
        """
        return len([character for character in self.get_cast() if character['gender'] == 'MALE'])

    @property
    @lru_cache()
    def num_of_female_characters(self):
        """Get the number of female characters in a play.

        Returns
        -------
        int
            The number of female characters in a play
        """

        return len([character for character in self.get_cast() if character['gender'] == 'FEMALE'])

    @property
    @lru_cache()
    def num_of_unknown_characters(self):
        """Get the number of characters of unknown gender in a play.

        Returns
        -------
        int
            The number of characters of unknown gender in a play
        """

        return len([character for character in self.get_cast() if character['gender'] == 'UNKNOWN'])

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
    def relations_csv(self):
        """Get relation data of a play as CSV.

        Returns
        -------
        string
            csv representation of a play
        """

        return self.make_get_text_request(
            f"{self._base_url}/corpora/{self.corpus_name}/play/{self.name}/relations/csv"
        )

    @lru_cache()
    def relations_gexf(self):
        """Get relation data of a play as GEXF.

        Returns
        -------
        string
            gexf representation of a play
        """

        return self.make_get_text_request(
            f"{self._base_url}/corpora/{self.corpus_name}/play/{self.name}/relations/gexf"
        )

    @lru_cache()
    def relations_graphml(self):
        """Get relation data of a play as GRAPHML.

        Returns
        -------
        string
            graphml representation of a play
        """

        return self.make_get_text_request(
            f"{self._base_url}/corpora/{self.corpus_name}/play/{self.name}/relations/graphml"
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

        return {
            "id": self.id,
            "title": self.title,
            "subtitle": self.subtitle,
            "wikidata_id": self.wikidata_id,
            "authors": self.authors,
            "genre": self.genre,
            "libretto": self.libretto,
            "source": self.source,
            "original_source": self.original_source,
            "year_written": self.year_written,
            "year_printed": self.year_printed,
            "year_premiered": self.year_premiered,
            "year_normalized": self.year_normalized
        }

    def __str__(self):
        """Play summary in a text

        Returns
        -------
        string
            "Author(s): ...
            Title: ...
            Subtitle: ...
            Genre: ...
            Libretto: ...
            Source: ...
            Original Source: ... 
            Year (written): ...
            Year (printed): ...
            Year (premiered): ...
            Year (normalized): ..."
        """

        result_string = f"Author(s): {', '.join([author['name'] + ' (' + author['fullname'] + ')' for author in self.authors])}\n" \
                        f"Title: {self.title} ({self.id}, {self.wikidata_id})\n" \
                        f"Subtitle: {self.subtitle}\n" \
                        f"Genre: {self.genre}\n" \
                        f"Libretto: {self.libretto}\n" \
                        f"Source: {self.source['name']} ({self.source['url']})\n" \
                        f"Original Source: {self.original_source}\n" \
                        f"Year (written): {self.year_written}\n" \
                        f"Year (printed): {self.year_printed}\n" \
                        f"Year (premiered): {self.year_premiered}\n" \
                        f"Year (normalized): {self.year_normalized}\n"
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
        play_cast = self.get_cast()
        was_character = False
        for i, character in enumerate(play_cast):
            if character['id'] == character_id:
                was_character = True
                break
        assert was_character, f'There is no character "{character_id}" in the play with' \
                              f'play_id "{play_id}" / play_name "{play_name}" / play_title "{play_title}"'
        self.id = character_id
        for key in play_cast[i]:
            setattr(self, key, play_cast[i][key])
        dct = [elem for elem in self.cast if elem['id'] == self.id][0]
        dct = self.transform_dict(dct)
        for key, value in dct.items():
            setattr(self, key, value)

    def summary(self):
        """Character summary

        Returns
        -------
        dictionary
            {
                "id": "yakov",
                "sex": "MALE",
                ...
            }
        """
        return {
            'id': self.id,
            'name': self.name,
            'sex': self.sex,
            'gender': self.gender,
            'is_group': self.is_group,
            'num_of_speech_acts': self.num_of_speech_acts,
            'num_of_scenes': self.num_of_scenes,
            'num_of_words': self.num_of_words
        }

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


if __name__ == "__main__":
    dracor = DraCor()
    print(f'DraCor info:\n{str(dracor)}')

    corpus = Corpus('rus')
    print(f'RUS corpus info:\n{str(corpus)}')

    play = Play('rus000160')
    print(f'Play rus000160 info:\n{str(play)}')

    character = Character('yakov', 'rus000138')
    print(f'Character yakov (rus000138) info:\n{str(character)}')
