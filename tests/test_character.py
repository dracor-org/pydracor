import unittest

from pydracor import Character


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
