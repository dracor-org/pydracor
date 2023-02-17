#!/usr/bin/env/python

"""
Results for tests dating 2023-01-30
"""

import unittest
import warnings

from pydracor import DraCor, Corpus, Play, Character

CORPORA = sorted(['als', 'bash', 'cal', 'fre', 'ger', 'gersh', 'greek', 'hun', 'ita', 'rom', 'rus', 'shake', 'span', 'swe', 'tat'])


class TestDraCorClass(unittest.TestCase):
    maxDiff = None
    dracor = DraCor()

    def test_init(self):
        self.assertEqual(self.dracor.name, "DraCor API")
        self.assertEqual(self.dracor.status, "beta")
        self.assertEqual(self.dracor.existdb, "6.0.1")
        self.assertEqual(self.dracor.version, "0.87.1")

    def test_transform_dict(self):
        self.assertEqual(
            self.dracor.transform_dict({'dramasRus': [{'aB': 3, 'cD': 4, 'eF': [{'gH': 5}]}]}),
            {'dramas_rus': [{'a_b': 3, 'c_d': 4, 'e_f': [{'g_h': 5}]}]}
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
            'name': 'DraCor API',
            'version': '0.87.1',
            'status': 'beta',
            'existdb': '6.0.1'})

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
                        'Tatar'

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

    def test_summary(self):
        dracor_summary = self.dracor.summary()
        self.assertIsInstance(dracor_summary, dict)
        self.assertEqual(
            dracor_summary, {
                "name": "DraCor API",
                "status": "beta",
                "existdb": "6.0.1",
                "version": "0.87.1",
                "corpora_full_names": [
                    'Alsatian Drama Corpus', 'Bashkir Drama Corpus', 'Calderón Drama Corpus', 'French Drama Corpus', 
                    'German Drama Corpus', 'German Shakespeare Drama Corpus', 'Greek Drama Corpus', 
                    'Hungarian Drama Corpus', 'Italian Drama Corpus', 'Roman Drama Corpus', 'Russian Drama Corpus', 
                    'Shakespeare Drama Corpus', 'Spanish Drama Corpus', 'Swedish Drama Corpus', 'Tatar Drama Corpus'
                ],
                "corpora_abbreviations": CORPORA,
                "number_of_corpora": len(CORPORA),
            }
        )

    def test_str(self):
        self.assertEqual(
            str(self.dracor),
            f"Name: DraCor API\n"
            f"Status: beta\n"
            f"Existdb: 6.0.1\n"
            f"Version: 0.87.1\n"
            f"Corpora (full names): Alsatian Drama Corpus, Bashkir Drama Corpus, Calderón Drama Corpus, French Drama Corpus, German Drama Corpus, German Shakespeare Drama Corpus, Greek Drama Corpus, Hungarian Drama Corpus, Italian Drama Corpus, Roman Drama Corpus, Russian Drama Corpus, Shakespeare Drama Corpus, Spanish Drama Corpus, Swedish Drama Corpus, Tatar Drama Corpus\n"
            f"Corpora (abbreviations): als, bash, cal, fre, ger, gersh, greek, hun, ita, rom, rus, shake, span, swe, tat\n"
            f"Number of corpora: 15\n"
        )


class TestCorpusClass(unittest.TestCase):
    maxDiff = None
    corpus = Corpus('rus')
    num_of_plays = 212

    def test_init(self):
        self.assertRaises(AssertionError, Corpus, 'nonexistent_corpusname')
        self.assertEqual(self.corpus.corpus_name, 'rus')
        self.assertEqual(self.corpus.name, 'rus')
        self.assertEqual(self.corpus.title, 'Russian Drama Corpus')
        self.assertEqual(self.corpus.repository, 'https://github.com/dracor-org/rusdracor')
        self.assertEqual(len(self.corpus.dramas), self.num_of_plays)
        self.assertEqual(self.corpus.num_of_plays, self.num_of_plays)

    def test_corpus_info(self):
        dct = self.corpus.corpus_info()
        self.assertEqual(dct['name'], 'rus')
        self.assertEqual(dct['title'], 'Russian Drama Corpus')
        self.assertEqual(dct['repository'], 'https://github.com/dracor-org/rusdracor')
        self.assertEqual(len(dct['dramas']), self.num_of_plays)

    def test_play_ids(self):
        play_ids = self.corpus.play_ids()
        self.assertEqual(len(play_ids), self.num_of_plays)
        self.assertTrue(all([play_id.startswith('rus000') for play_id in play_ids]))

    def test_play_names(self):
        dct = self.corpus.play_names()
        self.assertEqual(set(dct), set(self.corpus.play_ids()))
        self.assertEqual(dct['rus000138'], 'andreyev-ne-ubiy')

    def test_play_titles(self):
        dct = self.corpus.play_titles()
        self.assertEqual(set(dct), set(self.corpus.play_ids()))
        self.assertEqual(dct['rus000138'], 'Не убий')

    def test_written_years(self):
        dct = self.corpus.written_years()
        self.assertEqual(set(dct), set(self.corpus.play_ids()))
        self.assertEqual(dct['rus000138'], '1913')

    def test_premiere_years(self):
        dct = self.corpus.premiere_years()
        self.assertEqual(set(dct), set(self.corpus.play_ids()))
        self.assertEqual(dct['rus000138'], '1913')

    def test_print_years(self):
        dct = self.corpus.print_years()
        self.assertEqual(set(dct), set(self.corpus.play_ids()))
        self.assertEqual(dct['rus000138'], '1913')

    def test_normalized_years(self):
        dct = self.corpus.normalized_years()
        self.assertEqual(set(dct), set(self.corpus.play_ids()))
        self.assertEqual(dct['rus000138'], 1913)

    def test_metadata(self):
        lst = self.corpus.metadata()
        self.assertIsInstance(lst, list)
        self.assertEqual(len(lst), self.num_of_plays)
        self.assertIsInstance(lst[0], dict)
        self.assertEqual(set([elem['id'] for elem in lst]), set(self.corpus.play_ids()))
        lst = sorted(lst, key=lambda elem: elem['id'])
        self.assertEqual(lst[166]['id'], 'rus000167')
        self.assertEqual(lst[166]['size'], 12)
        self.assertEqual(lst[166]['num_of_speakers_male'], 5)

    def test_metadata_csv(self):
        metadata_csv = self.corpus.metadata_csv()
        self.assertIsInstance(metadata_csv, str)
        metadata_csv_entries = metadata_csv.splitlines()
        self.assertEqual(len(metadata_csv_entries), self.num_of_plays + 1)
        self.assertEqual(metadata_csv_entries[0], ("name,id,firstAuthor,numOfCoAuthors,title,"
                                              "subtitle,normalizedGenre,digitalSource,originalSourcePublisher,"
                                              "originalSourcePubPlace,originalSourceYear,originalSourceNumberOfPages,"
                                              "yearNormalized,size,libretto,averageClustering,density,averagePathLength,"
                                              "maxDegreeIds,averageDegree,diameter,yearPremiered,yearPrinted,maxDegree,"
                                              "numOfSpeakers,numOfSpeakersFemale,numOfSpeakersMale,numOfSpeakersUnknown,"
                                              "numPersonGroups,numConnectedComponents,numEdges,yearWritten,numOfSegments,"
                                              "wikipediaLinkCount,numOfActs,wordCountText,wordCountSp,wordCountStage,"
                                              "numOfP,numOfL"))
        self.assertEqual(metadata_csv_entries[1].split(",")[0], '"afinogenov-mashenka"')



    def test_filter(self):
        self.assertRaises(
            ValueError, self.corpus.filter, wikidata_id__iecaxt='Q1989636'
        )
        self.assertRaises(
            ValueError, self.corpus.filter, wikitada_id__iexact='Q1989636'
        )
        self.assertRaises(
            ValueError, self.corpus.filter, wikidata_id_iexact='Q1989636'
        )
        lst = self.corpus.filter(written_year__eq=1913, network_size__lt=20)
        self.assertEqual(set(lst), {'rus000137', 'rus000046'})

        lst = self.corpus.filter(
            print_year__lt=1850, source__icontains='lib.ru', premiere_year__gt=1845,
        )
        self.assertEqual(set(lst), {'rus000007', 'rus000189'})
        lst = self.corpus.filter(
            id__in=frozenset(f"rus000{num:03d}" for num in range(0, 250, 2)),
            subtitle__icontains='комедия',
            author__name__contains='Крылов'
        )
        self.assertEqual(set(lst), {'rus000102', 'rus000038', 'rus000132'})

        lst = self.corpus.filter(
            name__contains='mysl'
        )
        self.assertEqual(set(lst), {'rus000137'})

        lst = self.corpus.filter(
            title__exact='Мысль'
        )
        self.assertEqual(set(lst), {'rus000137'})

        lst = self.corpus.filter(
            year_normalized__in=frozenset(['1935', '1936']),
            source_url__contains='lib'
        )
        self.assertEqual(set(lst), {'rus000090', 'rus000083'})

        lst = self.corpus.filter(
            wikidata_id__iexact='Q1989636'
        )
        self.assertEqual(set(lst), {'rus000083'})

        lst = self.corpus.filter(
            networkdata_csv_url__icontains='/andreyev-ne-ubiy/'
        )
        self.assertEqual(set(lst), {'rus000138'})

        lst = self.corpus.filter(
            authors__name__icontains='Бабель'
        )
        self.assertEqual(set(lst), {'rus000119', 'rus000118'})


    def test_authors_summary(self):
        summary = self.corpus.authors_summary(num_of_authors=10)
        self.assertEqual(len(summary), 10)
        self.assertEqual(summary[0][0], 'Островский, Александр Николаевич')
        self.assertEqual(summary, [
            ('Островский, Александр Николаевич', 38),
            ('Сумароков, Александр Петрович', 14),
            ('Чехов, Антон Павлович', 14),
            ('Булгаков, Михаил Афанасьевич', 10),
            ('Тургенев, Иван Сергеевич', 9),
            ('Гоголь, Николай Васильевич', 8),
            ('Княжнин, Яков Борисович', 8),
            ('Крылов, Иван Андреевич', 8),
            ('Пушкин, Александр Сергеевич', 7),
            ('Прутков, Козьма', 6)
        ])

    def test_authors_summary_str(self):
        num_of_authors = 5
        self.assertEqual(
            self.corpus.authors_summary_str(num_of_authors=num_of_authors),
            f"There are 57 authors in Russian Drama Corpus\n\n"
            f"Top {num_of_authors} authors of the Corpus:\n"
            f"38 - Островский, Александр Николаевич\n"
            f"14 - Сумароков, Александр Петрович\n"
            f"14 - Чехов, Антон Павлович\n"
            f"10 - Булгаков, Михаил Афанасьевич\n"
            f"9 - Тургенев, Иван Сергеевич\n"
        )

    def test_summary(self):
        self.assertEqual(
            self.corpus.summary(),
            {
                'Corpus title': 'Russian Drama Corpus',
                'Corpus id': 'rus',
                'Repository': 'https://github.com/dracor-org/rusdracor',
                'Written years': ['1747', '1940'],
                'Premiere years': ['1750', '1992'],
                'Years of the first printing': ['1747', '1986'],
                'Normalized years' : [1747, 1947],
                'Number of plays in the corpus': 212
            }
        )

    def test_str(self):
        self.assertEqual(
            str(self.corpus),
            f'Written years: 1747 - 1940\n'
            f'Premiere years: 1750 - 1992\n'
            f'Years of the first printing: 1747 - 1986\n'
            f'Normalized years: 1747 - 1947\n'
            f'212 plays in Russian Drama Corpus\n'
            f'Corpus id: rus\n'
            f'repository: https://github.com/dracor-org/rusdracor\n'
        )


class TestPlayClass(unittest.TestCase):
    maxDiff = None
    play = Play('rus000160')

    def play_test(self, play: Play):
        self.assertEqual(play.id, 'rus000160')
        self.assertEqual(play.corpus_name, 'rus')
        self.assertEqual(play.name, 'ostrovsky-dohodnoe-mesto')
        self.assertEqual(play.title, 'Доходное место')
        self.assertTrue(hasattr(play, 'segments'))
        self.assertEqual(len(play.segments), 38)
        self.assertEqual(play.genre, 'Comedy')
        self.assertEqual(play.authors, [{
            'name': 'Островский, Александр Николаевич',
            'fullname': 'Александр Николаевич Островский',
            'shortname': 'Островский',
            'refs': [{'ref': 'Q171976', 'type': 'wikidata'}],
            'fullname_en': 'Alexander Ostrovsky',
            'name_en': 'Ostrovsky, Alexander',
            'shortname_en': 'Ostrovsky',
            'also_known_as': ['Alexander Ostrovsky']}])
        self.assertEqual(play.year_printed, '1856')
        self.assertTrue(hasattr(play, 'cast'))
        self.assertTrue(hasattr(play, 'authors'))
        self.assertFalse(hasattr(play, 'author'))
        self.assertTrue(hasattr(play, 'source'))
        self.assertTrue(hasattr(play, 'year_printed'))
        self.assertTrue(hasattr(play, 'original_source'))
        self.assertTrue(hasattr(play, 'year_normalized'))

    def test_init_play_id(self):
        self.assertRaises(ValueError, Play)
        self.assertRaises(AssertionError, Play, 'en000001')
        self.assertRaises(AssertionError, Play, 'rus000999')

        play_id = 'rus000160'
        play = Play(play_id)
        self.play_test(play)

    def test_init_play_name(self):
        self.assertRaises(AssertionError, Play, play_name='nonexistent_play_name')
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            play_name = 'avenarius-faust'
            Play(play_name=play_name)
            self.assertEqual(len(w), 0)
        play_name = 'ostrovsky-dohodnoe-mesto'
        play = Play(play_name=play_name)
        self.play_test(play)

    def test_init_play_title(self):
        self.assertRaises(AssertionError, Play, play_title='nonexistent_play_title')
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            play_title = 'Faust'
            Play(play_title=play_title)
            self.assertEqual(len(w), 1)
            w = w[-1]
            assert issubclass(w.category, UserWarning)
            self.assertEqual(
                str(w.message),
                f'There are several plays with the play_title {play_title} in the corpora.'
                f' Better use a play_id. Otherwise, a random play is selected.'
            )
        play_title = 'Доходное место'
        play = Play(play_title=play_title)
        self.play_test(play)

    def test_play_info(self):
        play_info = self.play.play_info()
        for key in play_info:
            setattr(self, key, play_info[key])
        self.assertEqual(play_info['id'], 'rus000160')
        self.assertEqual(play_info['corpus'], 'rus')
        self.assertEqual(play_info['name'], 'ostrovsky-dohodnoe-mesto')
        self.assertEqual(play_info['title'], 'Доходное место')
        self.assertTrue('segments' in play_info)
        self.assertEqual(len(play_info['segments']), 38)
        self.assertEqual(play_info['genre'], 'Comedy')
        self.assertEqual(play_info['authors'], [{'name': 'Островский, Александр Николаевич',
  'fullname': 'Александр Николаевич Островский',
  'shortname': 'Островский',
  'refs': [{'ref': 'Q171976', 'type': 'wikidata'}],
  'fullname_en': 'Alexander Ostrovsky',
  'name_en': 'Ostrovsky, Alexander',
  'shortname_en': 'Ostrovsky',
  'also_known_as': ['Alexander Ostrovsky']}])
        self.assertEqual(play_info['year_printed'], '1856')
        self.assertTrue('cast' in play_info)
        self.assertTrue('authors' in play_info)
        self.assertTrue('author' in play_info)
        self.assertTrue('source' in play_info)
        self.assertTrue('year_printed' in play_info)
        self.assertTrue('original_source' in play_info)

    def test_metrics(self):
        metrics = self.play.metrics()
        self.assertIsInstance(metrics, dict)
        self.assertTrue('nodes' in metrics)
        self.assertEqual(len(metrics['nodes']), 16)

    def test_get_cast(self):
        play_cast = self.play.get_cast()
        self.assertIsInstance(play_cast, list)
        self.assertEqual(len(play_cast), 16)

    def test_cast_csv(self):
        play_cast_csv = self.play.cast_csv()
        self.assertIsInstance(play_cast_csv, str)
        play_cast_csv_entries = play_cast_csv.splitlines()
        self.assertEqual(len(play_cast_csv_entries), 17)
        self.assertEqual(play_cast_csv_entries[0], ("id,name,gender,isGroup,numOfScenes,"
                                                    "numOfSpeechActs,numOfWords,wikidataId,degree,"
                                                    "weightedDegree,betweenness,closeness,eigenvector"))

    def test_num_of_male_characters(self):
        self.assertEqual(self.play.num_of_male_characters, 11)

    def test_num_of_female_characters(self):
        self.assertEqual(self.play.num_of_female_characters, 5)

    def test_num_of_unknown_characters(self):
        self.assertEqual(self.play.num_of_unknown_characters, 0)

    def test_tei(self):
        self.assertIsInstance(self.play.tei, str)

    def test_rdf(self):
        self.assertIsInstance(self.play.rdf, str)
        self.assertEqual(self.play.rdf[:8], '<rdf:RDF')

    def test_csv(self):
        csv = self.play.csv
        self.assertIsInstance(csv, str)
        self.assertEqual(csv.split('\n')[0], 'Source,Type,Target,Weight')

    def test_gexf(self):
        gexf = self.play.gexf
        self.assertIsInstance(gexf, str)
        self.assertEqual(gexf.split('\n')[0], '<?xml version="1.0" encoding="UTF-8"?>')
    
    def test_relations_csv(self):
        relations_csv = self.play.relations_csv()
        self.assertIsInstance(relations_csv, str)
        relations_csv_entries = relations_csv.splitlines()
        self.assertEqual(len(relations_csv_entries),6)
        self.assertEqual(relations_csv_entries[0], 'Source,Type,Target,Label')
    
    def test_relations_gexf(self):
        relations_gexf = self.play.relations_gexf()
        self.assertIsInstance(relations_gexf, str)
        self.assertEqual(len(relations_gexf), 6326)
        self.assertTrue('?xml version' in relations_gexf)
    
    def test_relations_graphml(self):
        relations_graphml = self.play.relations_graphml()
        self.assertIsInstance(relations_graphml, str)
        self.assertEqual(len(relations_graphml), 4140)
        self.assertTrue('?xml version' in relations_graphml)

    def test_spoken_text(self):
        self.assertRaises(AssertionError, self.play.spoken_text, gender='unknown_gender')
        play_spoken_text = self.play.spoken_text()
        self.assertIsInstance(play_spoken_text, str)
        self.assertEqual(len(play_spoken_text.split('\n')), 935)
        self.assertEqual(len(self.play.spoken_text(gender='MALE').split('\n')), 577)
        self.assertEqual(len(self.play.spoken_text(gender='FEMALE').split('\n')), 355)
        self.assertEqual(len(self.play.spoken_text(gender='UNKNOWN').split('\n')), 2)

    def test_spoken_text_by_character(self):
        play_spoken_text_by_character = self.play.spoken_text_by_character()
        self.assertIsInstance(play_spoken_text_by_character, list)
        self.assertEqual(len(play_spoken_text_by_character), 16)
        self.assertIsInstance(play_spoken_text_by_character[0], dict)

    def test_stage_directions(self):
        play_stage_directions = self.play.stage_directions()
        self.assertIsInstance(play_stage_directions, str)
        self.assertEqual(len(play_stage_directions.split('\n')), 426)

    def test_stage_directions_with_speakers(self):
        play_stage_directions_with_speakers = self.play.stage_directions_with_speakers()
        self.assertIsInstance(play_stage_directions_with_speakers, str)
        self.assertEqual(len(play_stage_directions_with_speakers.split('\n')), 427)

    def test_summary(self):
        play_summary = self.play.summary()
        self.assertIsInstance(play_summary, dict)
        self.assertEqual(
            play_summary,
            {
                "id": play_summary['id'],
                "title": play_summary['title'],
                "subtitle": play_summary['subtitle'],
                "wikidata_id": play_summary['wikidata_id'],
                "authors": play_summary['authors'],
                "genre": play_summary['genre'],
                "libretto": play_summary['libretto'],
                "source": play_summary['source'],
                "original_source": play_summary['original_source'],
                "year_written": play_summary['year_written'],
                "year_printed": play_summary['year_printed'],
                "year_premiered": play_summary['year_premiered'],
                "year_normalized": play_summary['year_normalized']
            }
        )

    def test_str(self):
        self.assertEqual(
            str(self.play),
            f"Author(s): Островский, Александр Николаевич (Александр Николаевич Островский)\n"
            f"Title: Доходное место (rus000160, Q4167340)\n"
            f"Subtitle: Комедия в пяти действиях\n"
            f"Genre: Comedy\n"
            f"Libretto: False\n"
            f"Source: Библиотека Максима Мошкова (lib.ru) (http://az.lib.ru/o/ostrowskij_a_n/text_0050.shtml)\n"
            f'Original Source: Москва, Изд-во "ЭКСМО", 2004\n' 
            f"Year (written): 1856\n"
            f"Year (printed): 1856\n"
            f"Year (premiered): 1857\n"
            f"Year (normalized): 1856\n"
        )


class TestCharacterClass(unittest.TestCase):
    maxDiff = None
    character = Character('yakov', 'rus000138')

    def test_init(self):
        self.assertRaises(AssertionError, Character, 'nonexistent_character', 'rus000138')
        self.assertEqual(self.character.id, 'yakov')
        self.assertEqual(self.character.name, 'Яков')
        self.assertEqual(self.character.sex, 'MALE')
        self.assertEqual(self.character.gender, 'MALE')
        self.assertEqual(self.character.is_group, False)
        self.assertEqual(self.character.num_of_speech_acts, 192)
        self.assertEqual(self.character.num_of_scenes, 5)
        self.assertEqual(self.character.num_of_words, 2713)

    def test_summary(self):
        character_summary = self.character.summary()
        self.assertEqual(
            character_summary,
            {
                'id': 'yakov',
                'name': 'Яков',
                'sex': 'MALE',
                'gender': 'MALE',
                'is_group': False,
                'num_of_speech_acts': 192,
                'num_of_scenes': 5,
                'num_of_words': 2713
            }
        )

    def test_str(self):
        self.assertEqual(
            str(self.character),
            f"Id: yakov\n"
            f"Name: Яков\n"
            f"Sex: MALE\n"
            f"Gender: MALE\n"
            f"Is group: False\n"
        )


if __name__ == '__main__':
    unittest.main()
