import unittest
import warnings

from pydracor import Play


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
        self.assertEqual(play.normalized_genre, 'Comedy')
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
        self.assertTrue(hasattr(play, 'characters'))
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
        self.assertEqual(play_info['normalized_genre'], 'Comedy')
        self.assertEqual(play_info['authors'], [{'name': 'Островский, Александр Николаевич',
  'fullname': 'Александр Николаевич Островский',
  'shortname': 'Островский',
  'refs': [{'ref': 'Q171976', 'type': 'wikidata'}],
  'fullname_en': 'Alexander Ostrovsky',
  'name_en': 'Ostrovsky, Alexander',
  'shortname_en': 'Ostrovsky',
  'also_known_as': ['Alexander Ostrovsky']}])
        self.assertEqual(play_info['year_printed'], '1856')
        self.assertTrue('characters' in play_info)
        self.assertTrue('authors' in play_info)
        self.assertTrue('source' in play_info)
        self.assertTrue('year_printed' in play_info)
        self.assertTrue('original_source' in play_info)

    def test_metrics(self):
        metrics = self.play.metrics()
        self.assertIsInstance(metrics, dict)
        self.assertTrue('nodes' in metrics)
        self.assertEqual(len(metrics['nodes']), 16)

    def test_get_characters(self):
        play_characters = self.play.get_characters()
        self.assertIsInstance(play_characters, list)
        self.assertEqual(len(play_characters), 16)

    def test_characters_csv(self):
        play_characters_csv = self.play.characters_csv()
        self.assertIsInstance(play_characters_csv, str)
        play_characters_csv_entries = play_characters_csv.splitlines()
        self.assertEqual(len(play_characters_csv_entries), 17)
        self.assertEqual(play_characters_csv_entries[0], ("id,name,gender,isGroup,numOfScenes,"
                                                    "numOfSpeechActs,numOfWords,wikidataId,degree,"
                                                    "weightedDegree,betweenness,closeness,eigenvector"))

    def test_num_of_male_characters(self):
        self.assertEqual(self.play.num_of_male_characters, 11)

    def test_num_of_female_characters(self):
        self.assertEqual(self.play.num_of_female_characters, 5)

    def test_num_of_unknown_characters(self):
        self.assertEqual(self.play.num_of_unknown_characters, 0)

    def test_tei(self):
        self.assertIsInstance(self.play.tei(), str)

    def test_csv(self):
        csv = self.play.csv()
        self.assertIsInstance(csv, str)
        self.assertEqual(csv.split('\n')[0], 'Source,Type,Target,Weight')

    def test_gexf(self):
        gexf = self.play.gexf()
        self.assertIsInstance(gexf, str)
        self.assertEqual(gexf.split('\n')[0], '<?xml version="1.0" encoding="UTF-8"?>')

    def test_graphml(self):
        graphml = self.play.graphml()
        self.assertIsInstance(graphml, str)
        self.assertEqual(len(graphml), 11054)
        self.assertTrue('?xml version' in graphml)

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
        self.assertEqual(len(self.play.spoken_text(gender='UNKNOWN').split('\n')), 1)

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
                "id": 'rus000160',
                "title": 'Доходное место',
                "subtitle": 'Комедия в пяти действиях',
                "wikidata_id": 'Q4167340',
                "authors": [
                    {
                    'name': 'Островский, Александр Николаевич',
                    'fullname': 'Александр Николаевич Островский',
                    'shortname': 'Островский',
                    'refs': [{'ref': 'Q171976', 'type': 'wikidata'}],
                    'fullname_en': 'Alexander Ostrovsky',
                    'name_en': 'Ostrovsky, Alexander',
                    'shortname_en': 'Ostrovsky',
                    'also_known_as': ['Alexander Ostrovsky']
                    }
                ],
                "normalized_genre": 'Comedy',
                "libretto": False,
                "source": {
                    'name': 'Библиотека Максима Мошкова (lib.ru)',
                    'url': 'http://az.lib.ru/o/ostrowskij_a_n/text_0050.shtml'
                    },
                "original_source": 'Москва, Изд-во "ЭКСМО", 2004',
                "year_written": '1856',
                "year_printed": '1856',
                "year_premiered": '1857',
                "year_normalized": 1856,
                "date_premiered": None
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
            f"Date (premiered): None\n"
        )

