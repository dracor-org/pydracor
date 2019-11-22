import unittest

from dracor import DraCor

CORPORA = sorted(['rus', 'ger', 'shake', 'rom', 'span', 'greek', 'swe', 'cal'])


class TestDraCorClass(unittest.TestCase):
    maxDiff = None
    dracor = DraCor()

    def test_lowerCamelCase_to_snake_case(self):
        f = self.dracor.lowerCamelCase_to_snake_case
        self.assertEqual(f('abCdEfghiJkl'), 'ab_cd_efghi_jkl')

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


if __name__ == '__main__':
    unittest.main()
