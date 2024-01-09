"""
Results for tests dating 2023-01-30
"""

import unittest
from pathlib import Path

from pydracor import DraCor

CORPORA = sorted(['als', 'bash', 'cal', 'fre', 'ger', 'gersh', 'greek', 'hun', 'ita', 'rom', 'rus', 'shake', 'span', 'swe', 'tat', 'u'])
ARTIFACTS_DIR = Path(__file__).parent/"test_artifacts"

class TestDraCorClass(unittest.TestCase):
    maxDiff = None
    dracor = DraCor()

    def test_init(self):
        self.assertEqual(self.dracor.name, "DraCor API v1")
        self.assertEqual(self.dracor.status, "beta")
        self.assertEqual(self.dracor.existdb, "6.2.0")
        self.assertEqual(self.dracor.version, "1.0.0")

    def test_transform_dict(self):
        self.assertEqual(
            self.dracor.transform_dict({'playsRus': [{'aB': 3, 'cD': 4, 'eF': [{'gH': 5}]}]}),
            {'plays_rus': [{'a_b': 3, 'c_d': 4, 'e_f': [{'g_h': 5}]}]}
        )
        self.assertEqual(
            self.dracor.transform_dict({'abcDfg': {'tmPr': 1, 'egFr': 2}}),
            {'abc_dfg': {'tm_pr': 1, 'eg_fr': 2}}
        )
        self.assertEqual(
            self.dracor.transform_dict([{
                'numOfSpeechActs': 192, 'gender': 'MALE', 'weightedDegree': 30, 'numOfScenes': 5,
                'name': 'Яков', 'numOfWords': 2713, 'degree': 21, 'closeness': 0.9565217391304348,
                'eigenvector': 0.2638364418039411, 'isGroup': False, 'id': 'yakov',
                'betweenness': 0.1356421356421356
            }]),
            [{
                'num_of_speech_acts': 192, 'gender': 'MALE', 'weighted_degree': 30,
                'num_of_scenes': 5, 'name': 'Яков', 'num_of_words': 2713, 'degree': 21,
                'closeness': 0.9565217391304348, 'eigenvector': 0.2638364418039411,
                'is_group': False, 'id': 'yakov', 'betweenness': 0.1356421356421356
            }]
        )

    def test_lowerCamelCase_to_snake_case(self):
        f = self.dracor.lowerCamelCase_to_snake_case
        self.assertEqual(f('abCdEfghiJkl'), 'ab_cd_efghi_jkl')

    def test_snake_case_to_lowerCamelCase(self):
        f = self.dracor.snake_case_to_lowerCamelCase
        self.assertEqual(f('ab_cd_efghi_jkl'), 'abCdEfghiJkl')

    def test_dracor_info(self):
        self.assertEqual(self.dracor.dracor_info(),{
            'name': 'DraCor API v1',
            'version': '1.0.0',
            'status': 'beta',
            'existdb': '6.2.0',
            'base': 'https://dracor.org/api/v1'})

    def test_corpora(self):
        corpora = self.dracor.corpora()
        self.assertEqual(type(corpora), list)
        self.assertEqual(len(corpora), len(CORPORA))
        self.assertEqual(type(corpora[0]), dict)
        self.assertEqual(
            {corpus['name'] for corpus in corpora},
            set(CORPORA)
        )

        self.assertRaises(AssertionError, self.dracor.corpora, 'nonexistent_include')

        corpora = self.dracor.corpora(include='metrics')
        self.assertEqual(type(corpora), list)
        self.assertEqual(len(corpora), len(CORPORA))
        self.assertEqual(type(corpora[0]), dict)
        self.assertTrue('metrics' in corpora[0])

    def test_corpora_names(self):
        self.assertEqual(
            set(self.dracor.corpora_names()),
            set(CORPORA)
        )

    def test_corpus_name_to_repository(self):
        base_url = 'https://github.com/dracor-org'

        self.assertEqual(
            self.dracor.corpus_name_to_repository(),
            {
                corpus: f'{base_url}/{corpus}dracor'
                for corpus in CORPORA
            }
        )

    def test_corpus_name_to_title(self):
        self.assertEqual(
            self.dracor.corpus_name_to_field('title'),
            {
                corpus: f'{lang} Drama Corpus'
                for corpus, lang in
                zip(
                    CORPORA,
                    [
                        'Alsatian', 'Bashkir', 'Calderón', 'French', 'German',
                        'German Shakespeare', 'Greek', 'Hungarian', 'Italian',
                        'Roman', 'Russian', 'Shakespeare', 'Spanish', 'Swedish',
                        'Tatar', 'Ukrainian'

                    ]
                )
            }
        )

    def test_play_title_to_corpus_name(self):
        play_titles = self.dracor.play_title_to_corpus_name()
        self.assertEqual(type(play_titles), dict)
        self.assertEqual(set(play_titles.values()), set(CORPORA))

    def test_play_name_to_corpus_name(self):
        play_names = self.dracor.play_name_to_corpus_name()
        self.assertEqual(type(play_names), dict)
        self.assertEqual(set(play_names.values()), set(CORPORA))

    def test_play_id_to_play_title(self):
        dct = self.dracor.play_id_to_play_title()
        self.assertEqual(type(dct), dict)
        self.assertEqual(dct['rus000138'], 'Не убий')

    def test_play_title_to_play_id(self):
        dct = self.dracor.play_title_to_play_id()
        self.assertEqual(type(dct), dict)
        self.assertEqual(dct['Не убий'], 'rus000138')

    def test_play_id_to_play_name(self):
        dct = self.dracor.play_id_to_play_name()
        self.assertEqual(type(dct), dict)
        self.assertEqual(dct['rus000138'], 'andreyev-ne-ubiy')

    def test_play_name_to_play_id(self):
        dct = self.dracor.play_name_to_play_id()
        self.assertEqual(type(dct), dict)
        self.assertEqual(dct['andreyev-ne-ubiy'], 'rus000138')

    def test_sparql(self):
        self.assertEqual(
            self.dracor.sparql("PREFIX urn: <http://fliqz.com/> SELECT *  FROM <urn:x-arq:UnionGraph> WHERE {?sub ?pred ?obj .} LIMIT 1"),"""<?xml version="1.0"?>
<sparql xmlns="http://www.w3.org/2005/sparql-results#">
  <head>
    <variable name="sub"/>
    <variable name="pred"/>
    <variable name="obj"/>
  </head>
  <results>
    <result>
      <binding name="sub">
        <uri>https://dracor.org/entity/als000001</uri>
      </binding>
      <binding name="pred">
        <uri>http://www.w3.org/1999/02/22-rdf-syntax-ns#type</uri>
      </binding>
      <binding name="obj">
        <uri>http://www.cidoc-crm.org/cidoc-crm/E33_Linguistic_Object</uri>
      </binding>
    </result>
  </results>
</sparql>\n""")

    def test_plays_by_character_wikidata_id(self):
        self.assertEqual(
                self.dracor.plays_by_character_wikidata_id("Q131412"),[
                    {
                        'id': 'ger000311',
                        'uri': 'https://dracor.org/id/ger000311',
                        'title': 'Maria Stuart',
                        'authors': ['Friedrich Schiller'],
                        'character_name': 'Maria'
                        },
                    {
                        'id': 'ita000009',
                        'uri': 'https://dracor.org/id/ita000009',
                        'title': 'Maria Stuarda',
                        'authors': ['Vittorio Alfieri'],
                        'character_name': 'Maria'
                        }
                    ])

    def test_play_info_by_id(self):
        html_text_response = (ARTIFACTS_DIR / "play_info_by_id.html").read_text().strip()
        self.assertEqual(
                self.dracor.play_info_by_id("ger000023"),
                html_text_response)


    def test_summary(self):
        dracor_summary = self.dracor.summary()
        self.assertIsInstance(dracor_summary, dict)
        self.assertEqual(
            dracor_summary, {
                "name": "DraCor API v1",
                "status": "beta",
                "existdb": "6.2.0",
                "version": "1.0.0",
                "corpora_full_names": [
                    'Alsatian Drama Corpus', 'Bashkir Drama Corpus', 'Calderón Drama Corpus', 'French Drama Corpus',
                    'German Drama Corpus', 'German Shakespeare Drama Corpus', 'Greek Drama Corpus',
                    'Hungarian Drama Corpus', 'Italian Drama Corpus', 'Roman Drama Corpus', 'Russian Drama Corpus',
                    'Shakespeare Drama Corpus', 'Spanish Drama Corpus', 'Swedish Drama Corpus', 'Tatar Drama Corpus',
                    'Ukrainian Drama Corpus'
                ],
                "base": "https://dracor.org/api/v1",
                "corpora_abbreviations": CORPORA,
                "number_of_corpora": len(CORPORA),
            }
        )

    def test_str(self):
        self.assertEqual(
            str(self.dracor),
            f"Name: DraCor API v1\n"
            f"Status: beta\n"
            f"Existdb: 6.2.0\n"
            f"Version: 1.0.0\n"
            f"Corpora (full names): Alsatian Drama Corpus, Bashkir Drama Corpus, Calderón Drama Corpus, French Drama Corpus, German Drama Corpus, German Shakespeare Drama Corpus, Greek Drama Corpus, Hungarian Drama Corpus, Italian Drama Corpus, Roman Drama Corpus, Russian Drama Corpus, Shakespeare Drama Corpus, Spanish Drama Corpus, Swedish Drama Corpus, Tatar Drama Corpus, Ukrainian Drama Corpus\n"
            f"Corpora (abbreviations): als, bash, cal, fre, ger, gersh, greek, hun, ita, rom, rus, shake, span, swe, tat, u\n"
            f"Number of corpora: 16\n"
        )

