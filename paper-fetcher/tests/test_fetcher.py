import pytest
from paper_fetcher.fetcher import Fetcher

def test_fetch_papers():
    fetcher = Fetcher()
    papers = fetcher.fetch_papers()
    assert isinstance(papers, list)
    assert len(papers) > 0  # Assuming there are papers to fetch

def test_parse_paper_data():
    fetcher = Fetcher()
    sample_data = {
        'title': 'Sample Paper',
        'authors': ['Author One', 'Author Two'],
        'year': 2023
    }
    parsed_data = fetcher.parse_paper_data(sample_data)
    assert 'title' in parsed_data
    assert 'authors' in parsed_data
    assert 'year' in parsed_data
    assert parsed_data['title'] == 'Sample Paper'