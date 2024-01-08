import unittest
from pathlib import Path

from pydracor import Wikidata

ARTIFACTS_DIR = Path(__file__).parent/"test_artifacts"

class TestWikidataClass(unittest.TestCase):
    wikidata = Wikidata()

    def test_get_author_info_by_id(self):
        self.assertEqual(
        self.wikidata.get_author_info_by_id("Q34628"),
        {
          "birth_date": "1729-01-22T00:00:00Z",
          "gender": "male",
          "birth_place": "Kamenz",
          "death_place": "Brunswick",
          "name": "Gotthold Ephraim Lessing",
          "image_url": "http://commons.wikimedia.org/wiki/Special:FilePath/Gotthold%20Ephraim%20Lessing%20Kunstsammlung%20Uni%20Leipzig.jpg",
          "gender_uri": "http://www.wikidata.org/entity/Q6581097",
          "death_date": "1781-02-15T00:00:00Z"
        }
        )

    def test_mixnmatch(self):
        mixnmatch_response = (ARTIFACTS_DIR / "mixnmatch.csv").read_text()
        self.assertEqual(self.wikidata.mixnmatch(), mixnmatch_response)
