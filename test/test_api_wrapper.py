#!/usr/bin/env python 

import unittest

from pydracor import DraCorAPI, Corpus, Play, Wikidata, DTS, DownloadFormat, CorpusNotFound, PlayNotFound, InvalidParameterCombination
from pydracor_base.models.corpus_in_corpora import CorpusInCorpora


# TODO: port is hardcoded, change?
class TestDracorAPI(unittest.TestCase):
    def setUp(self):
        self.dracor = DraCorAPI(host="http://localhost:8088/api/v1")

    def test_get_info(self):
        info = self.dracor.get_info()
        self.assertIsNotNone(info)
        self.assertEqual(info.name, "DraCor API v1")
        self.assertEqual(info.status, "stable")
        self.assertEqual(info.existdb, "6.4.0")
        self.assertEqual(info.base, "http://localhost:8088/api/v1")

    def test_get_corpora(self):
        corpora = self.dracor.get_corpora()
        self.assertIsInstance(corpora, list)
        self.assertEqual(len(corpora), 1)
        self.assertEqual(type(corpora[0]), CorpusInCorpora)

        corpus = corpora[0]
        self.assertEqual(corpus.name, 'test')
        self.assertEqual(corpus.title, 'Test Drama Corpus')
        self.assertEqual(corpus.acronym, 'TestDraCor')
        self.assertEqual(corpus.uri, 'http://localhost:8088/api/v1/corpora/test')

        corpora_metrics = self.dracor.get_corpora(include="metrics")
        self.assertIsInstance(corpora_metrics, list)
        self.assertEqual(len(corpora_metrics), 1)

        corpus_metric = corpora_metrics[0].metrics
        self.assertIsNotNone(corpus_metric)
        self.assertEqual(corpus_metric.characters, 93)
        self.assertEqual(corpus_metric.female, 15)
        self.assertEqual(corpus_metric.male, 52)
        self.assertEqual(corpus_metric.wordcount.text, 73868)

    def test_get_corpus(self):
        corpus_name = "test"
        corpus = self.dracor.get_corpus(corpus_name)
        # Corpus is a self-defined type
        self.assertIsInstance(corpus, Corpus)
        self.assertEqual(len(corpus.to_dict()), 9)
        self.assertEqual(corpus.name, corpus_name)
        self.assertEqual(corpus.title, 'Test Drama Corpus')
        self.assertEqual(corpus.acronym, 'TestDraCor')
        self.assertEqual(len(corpus.plays), 4)
        with self.assertRaises(CorpusNotFound):
            self.dracor.get_corpus("testy")

    def test_get_play(self):
        corpus_name = "test"
        play_name = "gogol-revizor"
        play = self.dracor.get_play(corpus_name, play_name)
        self.assertEqual(len(play.to_dict()), 24)
        self.assertEqual(len(play.segments), 53)
        self.assertEqual(len(play.characters), 31)
        self.assertEqual(play.name, play_name)
        self.assertEqual(play.year_normalized, 1836)
        
        with self.assertRaises(PlayNotFound):
            self.dracor.get_play(corpus_name, "testy")

    def test_get_resolve_play_id(self):
        play_id = "test000001"
        result = self.dracor.get_resolve_play_id(play_id)
        self.assertIsNone(result)

    def test_get_plays_with_character_by_id(self):
        wrong_character_id = "Q43718"
        character_id = "Q10322723"
        result = self.dracor.get_plays_with_character_by_id(character_id)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 1)
        entry = result[0]
        self.assertEqual(entry.title,'Macbeth')
        self.assertEqual(entry.character_name,'Macbeth')
        self.assertEqual(entry.id,'test000003')
        self.assertIsInstance(entry.authors, list)
        empty_result = self.dracor.get_plays_with_character_by_id(wrong_character_id)
        self.assertIsInstance(empty_result, list)
        self.assertEqual(len(empty_result), 0)


class TestCorpus(unittest.TestCase):
    def setUp(self):
        self.dracor = DraCorAPI(host="http://localhost:8088/api/v1")
        self.corpus_name = "test"
        self.corpus = self.dracor.get_corpus(self.corpus_name)

    def test_get_metadata(self):
        result = self.corpus.get_metadata()
        self.assertEqual(len(result), 4)
        self.assertEqual(result[1].title,'Emilia Galotti')
        play_metadata = result[1]
        self.assertDictEqual(
            play_metadata.to_dict(),
            {'id': 'test000002',
            'name': 'lessing-emilia-galotti',
            'title': 'Emilia Galotti',
            'subtitle': 'Ein Trauerspiel in fünf Aufzügen',
            'wikidataId': 'Q782653',
            'firstAuthor': 'Lessing',
            'yearNormalized': 1772,
            'yearPremiered': '1772',
            'yearPrinted': '1772',
            'datePremiered': '1772-03-13',
            'normalizedGenre': 'Tragedy',
            'libretto': False,
            'density': 0.3717948717948718,
            'digitalSource': 'http://www.textgridrep.org/textgrid:rksp.0',
            'averageClustering': 0.5174603174603175,
            'averageDegree': 4.461538461538462,
            'averagePathLength': 1.7820512820512822,
            'diameter': 3,
            'maxDegree': 9,
            'maxDegreeIds': 'marinelli',
            'numOfL': 0,
            'numConnectedComponents': 1,
            'numEdges': 29,
            'numOfActs': 5,
            'numOfCoAuthors': 0,
            'numOfP': 835,
            'numOfPersonGroups': 0,
            'numOfSegments': 43,
            'numOfSpeakers': 13,
            'numOfSpeakersMale': 10,
            'numOfSpeakersFemale': 3,
            'numOfSpeakersUnknown': 0,
            'size': 13,
            'wikipediaLinkCount': 16,
            'wordCountSp': 20809,
            'wordCountStage': 1332,
            'wordCountText': 21136,
            'yearWritten': None,
            'originalSourceNumberOfPages': None,
            'originalSourcePubPlace': None,
            'originalSourcePublisher': None,
            'originalSourceYear': None})

    def test_get_metadata_csv(self):
        result = self.corpus.get_metadata_csv()
        self.assertIsInstance(result, str)
        self.assertTrue(result.startswith("name"))
        self.assertEqual(len(result), 2008)

    # calls same function as in DraCor, test again here?
    def test_get_play(self):
        play_name = "gogol-revizor"
        result = self.corpus.get_play(play_name)
        self.assertIsInstance(result, Play)
        
        with self.assertRaises(PlayNotFound):
            self.corpus.get_play("testy")

    
class TestPlay(unittest.TestCase):

    def setUp(self):
        self.dracor = DraCorAPI(host="http://localhost:8088/api/v1")
        self.corpus_name = 'test'
        self.play_name = 'lessing-emilia-galotti'
        self.play = self.dracor.get_play(self.corpus_name, self.play_name)
        self.assertEqual(len(self.play.to_dict()), 23)
        self.assertEqual(len(self.play.segments), 43)
        self.assertEqual(len(self.play.characters), 13)

    def test_get_metrics(self):
        result = self.play.get_metrics()
        self.assertEqual(len(result.to_dict()), 15)
        self.assertEqual(len(result.nodes), 13)

    def test_get_tei(self):
        result = self.play.get_tei()
        self.assertIsInstance(result, str)
        self.assertEqual(len(result), 242843)
        self.assertTrue(result.startswith("<?xml-model"))

    def test_get_txt(self):
        result = self.play.get_txt()
        self.assertIsInstance(result, str)
        self.assertEqual(len(result), 132335)
        self.assertTrue(result.startswith("Gotthold Ephraim Lessing"))

    def test_get_characters(self):
        result = self.play.get_characters()
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 13)

    def test_get_characters_csv(self):
        result = self.play.get_characters_csv()
        self.assertIsInstance(result, str)
        self.assertEqual(len(result), 1619)
        self.assertTrue(result.startswith("id"))

    
    def test_get_networkdata(self):
        for format in [DownloadFormat.csv, DownloadFormat.gexf, DownloadFormat.graphml]:
            result = self.play.get_networkdata(format)
            self.assertIsInstance(result, str)
            if format == DownloadFormat.csv:
                self.assertEqual(len(result), 895)
            elif format == DownloadFormat.gexf:
                self.assertEqual(len(result), 7252)
            else:
                self.assertEqual(len(result), 7355)
    
    def test_get_relations(self):
        for format in [DownloadFormat.csv, DownloadFormat.gexf, DownloadFormat.graphml]:
            result = self.play.get_relations(format)
            self.assertIsInstance(result, str)
            if format == DownloadFormat.csv:
                self.assertEqual(len(result), 186)
            elif format == DownloadFormat.graphml:
                self.assertEqual(len(result), 3382)
            else:
                self.assertEqual(len(result), 5222)

    def test_get_spoken_text(self):
        result = self.play.get_spoken_text()
        self.assertIsInstance(result, str)
        self.assertEqual(len(result), 112933)
        self.assertTrue(result.startswith('Klagen, nichts als Klagen!'))
        
        result_sex = self.play.get_spoken_text(sex="FEMALE")
        self.assertIsInstance(result_sex, str)
        self.assertEqual(len(result_sex), 32501)

        # as no roles exist, result should be an empty string
        result_role = self.play.get_spoken_text(role="test")
        self.assertIsInstance(result_role, str)
        self.assertEqual(len(result_role), 0)

        # as no undirected relations exist, result should be an empty string
        result_relation = self.play.get_spoken_text(relation="spouses")
        self.assertIsInstance(result_relation, str)
        self.assertEqual(len(result_relation), 0)

        result_relation_active = self.play.get_spoken_text(relation_active="parent_of")
        self.assertIsInstance(result_relation_active, str)
        self.assertEqual(len(result_relation_active), 24220)

        result_relation_passive = self.play.get_spoken_text(relation_passive="parent_of")
        self.assertIsInstance(result_relation_passive, str)
        self.assertEqual(len(result_relation_passive), 10017)

        result_sex_relation = self.play.get_spoken_text(sex="female", relation_active="parent_of")
        self.assertIsInstance(result_sex_relation, str)
        self.assertEqual(len(result_sex_relation), 9629)
        

    def test_get_spoken_text_by_character(self):
        result = self.play.get_spoken_text_by_character()
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 13)
        entry = result[0]
        self.assertEqual(entry.label, 'Der Prinz')
        self.assertEqual(len(entry.text), 157)

    def test_get_stage_directions(self):
        result = self.play.get_stage_directions()
        self.assertIsInstance(result, str)
        self.assertEqual(len(result), 8314)

    def test_get_stage_directions_with_speakers(self):
        result = self.play.get_stage_directions_with_speakers()
        self.assertIsInstance(result, str)
        self.assertEqual(len(result), 9169)

class TestWikidata(unittest.TestCase):
    def setUp(self):
        self.wikidata = Wikidata()

    def test_get_author_info(self):
        wikidata_id = "Q43718"
        result = self.wikidata.get_author_info(wikidata_id)
        # TODO: but returns an object!
        self.assertIsInstance(result, dict)
        self.assertEqual(len(result), 8)
        self.assertEqual(result["name"], 'Nikolai Gogol')

    def test_get_mixnmatch(self):
        result = self.wikidata.get_mixnmatch()
        self.assertIsInstance(result, str)
        self.assertTrue(result.startswith("id"))
    

class TestDTS(unittest.TestCase):

    def setUp(self):
        self.dts = DTS(host="http://localhost:8088/api/v1")

    def test_get_dts(self):
        result = self.dts.get_dts()
        self.assertIsNotNone(result)
        self.assertEqual(len(result.to_dict()), 7)
        self.assertEqual(result.id, 'http://localhost:8088/api/v1/dts')

    def test_get_collection(self):
        collection_id = "test"
        result = self.dts.get_collection(collection_id)
        self.assertIsInstance(result, dict)
        self.assertEqual(len(result), 9)
        self.assertTrue('member' in result)
        self.assertEqual(len(result["member"]), 4)
        self.assertEqual(result["title"], 'Test Drama Corpus')

    def test_get_navigation(self):
        resource = "test000001"
        reference = "body/div[1]"
        start = "body/div[2]/div[1]"
        end = "body/div[2]/div[3]"
        result = self.dts.get_navigation(resource, reference, None, None)
        self.assertIsInstance(result, dict)
        self.assertEqual(len(result), 6)
        self.assertTrue('ref' in result)

        with self.assertRaises(InvalidParameterCombination):
            self.dts.get_navigation(resource, reference, start, None)
        
        result = self.dts.get_navigation(resource, None, start, end)
        self.assertIsInstance(result, dict)
        self.assertEqual(len(result), 8)

    def test_get_document(self):
        resource = "test000001"
        reference = "body/div[1]"
        start = "body/div[2]/div[1]"
        end = "body/div[2]/div[3]"

        result = self.dts.get_document(resource, reference)
        self.assertIsInstance(result, str)
        self.assertEqual(len(result), 42755)

        with self.assertRaises(InvalidParameterCombination):
            self.dts.get_document(resource, reference, start, None)
        
        result = self.dts.get_document(resource, None, start, end)
        self.assertIsInstance(result, str)
        self.assertEqual(len(result), 9062)

if __name__ == "__main__":
    unittest.main()


