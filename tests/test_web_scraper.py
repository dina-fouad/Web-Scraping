from web_scraper import __version__


def test_version():
    assert __version__ == '0.1.0'

from web_scraper.scraper import get_citations_needed_count ,  get_citations_needed_report



def test_get_citations_needed_count():
    URL = "https://en.wikipedia.org/wiki/History_of_Mexico"
    assert get_citations_needed_count(URL) ==1


def test_get_citations_needed_report():
    URL = "https://en.wikipedia.org/wiki/History_of_Mexico"
    expected = open("citation.txt", "r")
    assert get_citations_needed_report(URL) == expected.read()