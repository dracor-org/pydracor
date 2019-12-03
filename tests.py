import unittest

from dracor import DraCor, Corpus

CORPORA = sorted(['rus', 'ger', 'shake', 'rom', 'span', 'greek', 'swe', 'cal'])


class TestDraCorClass(unittest.TestCase):
    maxDiff = None
    dracor = DraCor()

    def test_lowerCamelCase_to_snake_case(self):
        f = self.dracor.lowerCamelCase_to_snake_case
        self.assertEqual(f('abCdEfghiJkl'), 'ab_cd_efghi_jkl')

    def test_snake_case_to_lowerCamelCase(self):
        f = self.dracor.snake_case_to_lowerCamelCase
        self.assertEqual(f('ab_cd_efghi_jkl'), 'abCdEfghiJkl')

    def test_dracor_info(self):
        self.assertEqual(self.dracor.dracor_info(), {
            "name": "DraCor API",
            "status": "beta",
            "existdb": "4.7.0",
            "version": "0.57.1"
        })

    def test_corpora(self):
        corpora = self.dracor.corpora()
        self.assertEqual(type(corpora), list)
        self.assertEqual(len(corpora), 8)
        self.assertEqual(type(corpora[0]), dict)
        self.assertEqual(
            {corpus['name'] for corpus in corpora},
            set(CORPORA)
        )

        self.assertRaises(AssertionError, self.dracor.corpora, 'nonexistent_include')

        corpora = self.dracor.corpora(include='metrics')
        self.assertEqual(type(corpora), list)
        self.assertEqual(len(corpora), 8)
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
                for corpus in ['rus', 'ger', 'shake', 'rom', 'span', 'greek', 'swe', 'cal']
            }
        )

    def test_corpus_name_to_title(self):
        self.assertEqual(
            self.dracor.corpus_name_to_field('title'),
            {
                corpus: f'{lang} Drama Corpus'
                for corpus, lang in
                zip(CORPORA, ['Calderón', 'German', 'Greek', 'Roman', 'Russian', 'Shakespeare', 'Spanish', 'Swedish'])
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
        # print(self.dracor.sparql('SELECT * WHERE {?s ?p ?o} LIMIT 1'))
        self.assertEqual(
            self.dracor.sparql('SELECT * WHERE {?s ?p ?o} LIMIT 1'),
            """<sparql xmlns="http://www.w3.org/2005/sparql-results#">
    <head>
        <variable name="s"/>
        <variable name="p"/>
        <variable name="o"/>
    </head>
    <results>
        <result>
            <binding name="s">
                <uri>https://dracor.org/id/rus000137</uri>
            </binding>
            <binding name="p">
                <uri>http://www.w3.org/2002/07/owl#sameAs</uri>
            </binding>
            <binding name="o">
                <uri>http://www.wikidata.org/entity/Q59355429</uri>
            </binding>
        </result>
    </results>
</sparql>"""
        )

class TestCorpusClass(unittest.TestCase):
    maxDiff = None
    corpus = Corpus('rus')
    num_of_plays = 210

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
        self.assertEqual(dct['rus000138'], 1913)

    def test_premiere_years(self):
        dct = self.corpus.premiere_years()
        self.assertEqual(set(dct), set(self.corpus.play_ids()))
        self.assertEqual(dct['rus000138'], 1913)

    def test_print_years(self):
        dct = self.corpus.print_years()
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
        self.assertEqual(lst[166]['numOfSpeakersMale'], 5)

    def test_filter(self):
        lst = self.corpus.filter(written_year__eq=1913, network_size__lt=20)
        self.assertEqual(set(lst), {'rus000137', 'rus000046'})


if __name__ == '__main__':
    unittest.main()
