import unittest

from pydracor import Corpus


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
        self.assertEqual(len(self.corpus.plays), self.num_of_plays)
        self.assertEqual(self.corpus.num_of_plays, self.num_of_plays)

    def test_corpus_info(self):
        dct = self.corpus.corpus_info()
        self.assertEqual(dct['name'], 'rus')
        self.assertEqual(dct['title'], 'Russian Drama Corpus')
        self.assertEqual(dct['repository'], 'https://github.com/dracor-org/rusdracor')
        self.assertEqual(len(dct['plays']), self.num_of_plays)

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

    def test_years_written(self):
        dct = self.corpus.years_written()
        self.assertEqual(set(dct), set(self.corpus.play_ids()))
        self.assertEqual(dct['rus000138'], '1913')

    def test_years_premiered(self):
        dct = self.corpus.years_premiered()
        self.assertEqual(set(dct), set(self.corpus.play_ids()))
        self.assertEqual(dct['rus000138'], '1913')

    def test_years_printed(self):
        dct = self.corpus.years_printed()
        self.assertEqual(set(dct), set(self.corpus.play_ids()))
        self.assertEqual(dct['rus000138'], '1913')

    def test_years_normalized(self):
        dct = self.corpus.years_normalized()
        self.assertEqual(set(dct), set(self.corpus.play_ids()))
        self.assertEqual(dct['rus000138'], 1913)

    def test_dates_premiered(self):
        dct = self.corpus.dates_premiered()
        self.assertEqual(set(dct), set(self.corpus.play_ids()))
        self.assertIsNone(dct['rus000138'])

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
        self.assertEqual(metadata_csv_entries[0], ("name,id,wikidataId,firstAuthor,numOfCoAuthors,title,"
                                              "subtitle,normalizedGenre,digitalSource,originalSourcePublisher,"
                                              "originalSourcePubPlace,originalSourceYear,originalSourceNumberOfPages,"
                                              "yearNormalized,size,libretto,averageClustering,density,averagePathLength,"
                                              "maxDegreeIds,averageDegree,diameter,datePremiered,yearPremiered,yearPrinted,maxDegree,"
                                              "numOfSpeakers,numOfSpeakersFemale,numOfSpeakersMale,numOfSpeakersUnknown,"
                                              "numOfPersonGroups,numConnectedComponents,numEdges,yearWritten,numOfSegments,"
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
        lst = self.corpus.filter(year_written__eq=1913, network_size__lt=20)
        self.assertEqual(set(lst), {'rus000137', 'rus000046'})

        lst = self.corpus.filter(
            year_printed__lt=1850, source__icontains='lib.ru', year_premiered__gt=1845,
        )
        self.assertEqual(set(lst), {'rus000007', 'rus000189'})
        lst = self.corpus.filter(
            id__in=frozenset(f"rus000{num:03d}" for num in range(0, 250, 2)),
            subtitle__icontains='комедия',
            authors__name__contains='Крылов'
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
                'Number of plays in the corpus': 212,
                'Normalized years' : [1747, 1947],
                'Premiere dates' : ["-", "-"]
            }
        )

    def test_str(self):
        self.assertEqual(
            str(self.corpus),
            f'Written years: 1747 - 1940\n'
            f'Premiere years: 1750 - 1992\n'
            f'Premiere dates: - - -\n'
            f'Years of the first printing: 1747 - 1986\n'
            f'Normalized years: 1747 - 1947\n'
            f'212 plays in Russian Drama Corpus\n'
            f'Corpus id: rus\n'
            f'repository: https://github.com/dracor-org/rusdracor\n'
        )

