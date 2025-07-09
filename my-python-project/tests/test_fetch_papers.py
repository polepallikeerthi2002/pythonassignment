import unittest
from papers.fetch_papers import fetch_papers

class TestFetchPapers(unittest.TestCase):

    def test_fetch_papers(self):
        results = fetch_papers("cancer", max_results=2)
        self.assertIsInstance(results, list)
        if results:
            self.assertIn("PubmedID", results[0])

if __name__ == '__main__':
    unittest.main()