import unittest
from phase4 import check_sentence_spelling, get_suggestions_for_word

class TestSpellingChecker(unittest.TestCase):

    def test_correct_spelling(self):
        correct_sentences = [
            "hello there",
            "the apple is red",
            "how are you doing",
            "this is a simple sentence"
        ]

        for sentence in correct_sentences:
            print(f"Testing sentence: '{sentence}'")
            result, misspelled_words, feedback = check_sentence_spelling(sentence)
            self.assertTrue(result, f"Expected sentence to be spelled correctly, but got misspelled words: {misspelled_words}")

    def test_incorrect_spelling(self):
        incorrect_sentences = {
            "helo there": ["helo"],
            "the applee is red": ["applee"],
            "howw are you doing": ["howw"],
            "this is a simmple sentence": ["simmple"]
        }

        for sentence, expected_misspellings in incorrect_sentences.items():
            print(f"Testing sentence: '{sentence}'")
            result, misspelled_words, feedback = check_sentence_spelling(sentence)
            self.assertFalse(result, f"Expected sentence to have misspellings, but got correctly spelled.")
            for word in expected_misspellings:
                self.assertIn(word, misspelled_words, f"Expected '{word}' to be in misspelled words, but it wasn't.")

    def test_suggestions(self):
        test_sentences = {
            "helo and applee": {
                "helo": ["hello"],
                "applee": ["apple"]
            },
            "this is a simmple sentencee": {
                "simmple": ["simple"],
                "sentencee": ["sentence"]
            }
        }

        for sentence, expected_suggestions in test_sentences.items():
            print(f"Testing sentence: '{sentence}' for suggestions")
            _, misspelled_words, feedback = check_sentence_spelling(sentence)
            for word, expected_suggests in expected_suggestions.items():
                suggestions = get_suggestions_for_word(word)
                for expected_suggest in expected_suggests:
                    self.assertIn(expected_suggest, suggestions, f"Expected '{expected_suggest}' to be suggested for word '{word}', but it wasn't.")

if __name__ == '__main__':
    unittest.main()
